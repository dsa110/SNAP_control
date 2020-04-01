from __future__ import print_function
import threading
import Queue
import time
import logging

LOGGER = logging.getLogger(__name__)


def create_meta_dictionary(metalist):
    """
    Build a meta information dictionary from a provided raw meta info list.
    :param metalist: a list of all meta information about the system
    :return: a dictionary of device info, keyed by unique device name
    """
    meta_items = {}
    try:
        for name, tag, param, value in metalist:
            if name not in meta_items:
                meta_items[name] = {}
            try:
                if meta_items[name]['tag'] != tag:
                    raise ValueError(
                        'Different tags - %s, %s - for the same item %s' % (
                            meta_items[name]['tag'], tag, name))
            except KeyError:
                meta_items[name]['tag'] = tag
            meta_items[name][param] = value
    except ValueError as e:
        for ctr, contents in enumerate(metalist):
            print(ctr, end='')
            print(contents)
        raise e
    return meta_items


def parse_fpg(filename):
    """
    Read the meta information from the FPG file.
    :param filename: the name of the fpg file to parse
    :return: device info dictionary, memory map info (coreinfo.tab) dictionary
    """
    LOGGER.debug('Parsing file %s for system information' % filename)
    if filename is not None:
        fptr = open(filename, 'r')
        firstline = fptr.readline().strip().rstrip('\n')
        if firstline != '#!/bin/kcpfpg':
            fptr.close()
            raise RuntimeError('%s does not look like an fpg file we can '
                               'parse.' % filename)
    else:
        raise IOError('No such file %s' % filename)
    memorydict = {}
    metalist = []
    while True:
        line = fptr.readline().strip().rstrip('\n')
        if line.lstrip().rstrip() == '?quit':
            break
        elif line.startswith('?meta'):
            # some versions of mlib_devel may mistakenly have put spaces
            # as delimiters where tabs should have been used. Rectify that
            # here.
            if line.startswith('?meta '):
                LOGGER.warn('An old version of mlib_devel generated %s. Please '
                            'update. Meta fields are seperated by spaces, '
                            'should be tabs.' % filename)
                line = line.replace(' ', '\t')
            # and carry on as usual.
            line = line.replace('\_', ' ').replace('?meta', '')
            line = line.replace('\n', '').lstrip().rstrip()
            line_split = line.split('\t')
            name = line_split[0]
            tag = line_split[1]
            param = line_split[2]
            if len(line_split[3:]) == 1:
                value = line_split[3:][0]
            else:
                value = ' '.join(line_split[3:])
            # name, tag, param, value = line.split('\t')
            name = name.replace('/', '_')
            metalist.append((name, tag, param, value))
        elif line.startswith('?register'):
            if line.startswith('?register '):
                register = line.replace('\_', ' ').replace('?register ', '')
                register = register.replace('\n', '').lstrip().rstrip()
                name, address, size_bytes = register.split(' ')
            elif line.startswith('?register\t'):
                register = line.replace('\_', ' ').replace('?register\t', '')
                register = register.replace('\n', '').lstrip().rstrip()
                name, address, size_bytes = register.split('\t')
            else:
                raise ValueError('Cannot find ?register entries in '
                                 'correct format.')
            address = int(address, 16)
            size_bytes = int(size_bytes, 16)
            if name in memorydict.keys():
                raise RuntimeError('%s: mem device %s already in '
                                   'dictionary' % (filename, name))
            memorydict[name] = {'address': address, 'bytes': size_bytes}
    fptr.close()
    return create_meta_dictionary(metalist), memorydict


def pull_info_from_fpg(fpg_file, parameter):
    """
    Pull available parameters about x-engine or f-engine from .fpg file.
    Available options for x-engine: 'x_fpga_clock', 'xeng_outbits',
    'xeng_accumulation_len'
    Available options for f-engine: 'n_chans', 'quant_format', 'spead_flavour'
    :param fpg_file: bit file path
    :param parameter: parameter string
    :return: pattern value (string)
    """
    match = []
    fpg_dict = parse_fpg(fpg_file)
    if parameter == 'x_fpga_clock':
        match = str(int(fpg_dict[0]['XSG_core_config']['clk_rate'])*10**6)
    if parameter == 'xeng_outbits':
        match = fpg_dict[0]['sys0_vacc']['n_bits']
    if parameter == 'xeng_accumulation_len':
        match = fpg_dict[0]['sys0_xeng']['acc_len']
    if parameter == 'spead_flavour':
        match1 = fpg_dict[0]['pack_spead_pack0']['spead_msw']
        match2 = fpg_dict[0]['pack_spead_pack0']['spead_lsw']
        s = ','
        match = s.join([match1, match2])
    if parameter == 'quant_format':
        match1 = fpg_dict[0]['snap_quant0']['io_widths']
        match2 = fpg_dict[0]['snap_quant0']['io_bps']
        s = '.'
        match = s.join([match1[1], match2[1]])
    if parameter == 'n_chans':
        pfb_dict = fpg_dict[0]['pfb_fft_wideband_real_fft_biplex_real_4x']
        match1 = int(pfb_dict['fftsize'])
        match2 = int(pfb_dict['n_inputs'])
        match = match2*2**match1
    if match is []:
        errstr = 'Parameter %s does not match any field in fpg ' \
                 'file.' % parameter
        LOGGER.error(errstr)
        raise RuntimeError(errstr)
    return match


def check_changing_status(field_dict, data_function,
                          wait_time, num_checks):
    """
    Check a changing set of status fields.
    :param field_dict: field descriptions {name: (required, constant)}
    :param data_function: a function that will return a single value for the
    fields from field_dict
    :param wait_time: seconds to wait between calls to data_function
    :param num_checks: times to run data_function
    :return:
    """
    # fields = {
    #     # name, required, True=same|False=different
    #     'test_required_diff': (True, False),
    #     'test_required_same': (True, True),
    #     'test_diff': (True, False),
    #     'test_same': (True, True),
    # }
    #
    # def get_data():
    #     res = {}
    #     res['test_required_diff'] = time.time()
    #     res['test_required_same'] = 123456
    #     res['test_diff'] = time.time()
    #     res['test_same'] = 654321
    #     return res

    # check that required data fields are returned by the data function
    change_required = {}
    d = data_function()
    checked_fields = field_dict.copy()
    for f in checked_fields.keys():
        req = checked_fields[f][0]
        if f not in d.keys():
            if req:
                return False, 'required field %s not found' % f
            else:
                checked_fields.pop(f)
        else:
            if not checked_fields[f][1]:
                change_required[f] = False
    # collect data, checking fields while we're at it
    prev_data = [d]
    time.sleep(wait_time)
    for loop in range(num_checks-1):
        d = data_function()
        for f in checked_fields.keys():
            same_reqd = checked_fields[f][1]
            for pd in prev_data:
                value_the_same = pd[f] == d[f]
                if not value_the_same:
                    if same_reqd:
                        return False, '%s changing: %.3f > %.3f' % (
                            f, pd[f], d[f])
                    else:
                        change_required[f] = True
        prev_data.append(d)
        time.sleep(wait_time)
    # did the necessary fields change
    for f in change_required:
        if not change_required[f]:
            return False, '%s is not changing: %.3f' % (f, prev_data[0][f])
    return True, ''


def program_fpgas(fpga_list, progfile, timeout=10):
    """
    Program more than one FPGA at the same time.
    :param fpga_list: a list of objects for the FPGAs to be programmed
    :param progfile: string, the file used to program the FPGAs
    :param timeout: how long to wait for a response, in seconds
    :return: <nothing>
    """
    stime = time.time()
    new_dict = {}
    new_list = []
    for fpga in fpga_list:
        try:
            len(fpga)
        except TypeError:
            _tuple = (fpga, progfile)
        else:
            _tuple = (fpga[0], fpga[1])
        new_dict[_tuple[0].host] = _tuple[1]
        new_list.append(_tuple[0])

    def _prog_fpga(_fpga):
        _fpga.upload_to_ram_and_program(new_dict[_fpga.host])
    threaded_fpga_operation(fpga_list=new_list, timeout=timeout,
                            target_function=(_prog_fpga,))
    LOGGER.info('Programming %d FPGAs took %.3f seconds.' % (
        len(fpga_list), time.time() - stime))


def threaded_create_fpgas_from_hosts(host_list, fpga_class=None,
                                     port=7147, timeout=10):
    """
    Create KatcpClientFpga objects in many threads, Moar FASTAAA!
    :param fpga_class: the class to insantiate, usually CasperFpga
    :param host_list: a comma-seperated list of hosts
    :param port: the port on which to do network comms
    :param timeout: how long to wait, in seconds
    :return:
    """
    if fpga_class is None:
        from casperfpga import CasperFpga
        fpga_class = CasperFpga

    num_hosts = len(host_list)
    result_queue = Queue.Queue(maxsize=num_hosts)
    thread_list = []

    def makehost(hostname):
        result_queue.put_nowait(fpga_class(hostname, port))

    for host_ in host_list:
        thread = threading.Thread(target=makehost, args=(host_,))
        thread.daemon = True
        thread.start()
        thread_list.append(thread)
    for thread_ in thread_list:
        thread_.join(timeout)
    fpgas = [None] * num_hosts
    hosts_missing = host_list[:]
    while True:
        try:
            result = result_queue.get_nowait()
            host_pos = host_list.index(result.host)
            fpgas[host_pos] = result
            hosts_missing.pop(hosts_missing.index(result.host))
        except Queue.Empty:
            break
    if hosts_missing:
        for host in hosts_missing:
            LOGGER.error('Could not create host %s.' % host)
        errstr = 'Given %d hosts, only made %d CasperFpgas.' % (
            num_hosts, len(fpgas))
        LOGGER.error(errstr)
        raise RuntimeError(errstr)
    return fpgas


def _check_target_func(target_function):
    """

    :param target_function:
    :return:
    """
    if isinstance(target_function, basestring):
        return target_function, (), {}
    try:
        len(target_function)
    except TypeError:
        return target_function, (), {}
    if len(target_function) == 3:
        return target_function
    elif len(target_function) == 1:
        target_function = (target_function[0], (), {})
    elif len(target_function) == 2:
        target_function = (target_function[0], target_function[1], {})
    else:
        raise RuntimeError('target_function tuple too long? - (name, (), {})')
    return target_function


def threaded_fpga_function(fpga_list, timeout, target_function):
    """
    Thread the running of any KatcpClientFpga function on a list of
    KatcpClientFpga objects. Much faster.
    :param fpga_list: list of KatcpClientFpga objects
    :param timeout: how long to wait before timing out
    :param target_function: a tuple with three parts:
                            1. string, the KatcpClientFpga function to
                               run e.g. 'disconnect' for fpgaobj.disconnect()
                            2. tuple, the arguments to the function
                            3. dict, the keyword arguments to the function
                            e.g. (func_name, (1,2,), {'another_arg': 3})
    :return: a dictionary of the results, keyed on hostname
    """
    target_function = _check_target_func(target_function)

    def dofunc(fpga, *args, **kwargs):
        try:
            rv = getattr(fpga, target_function[0])(*args, **kwargs)
            return rv
        except AttributeError:
            LOGGER.error('FPGA %s has no such function: %s' % (
                fpga.host, target_function[0]))
            raise
    return threaded_fpga_operation(
        fpga_list, timeout, (dofunc, target_function[1], target_function[2]))


def threaded_fpga_operation(fpga_list, timeout, target_function):
    """
    Thread any operation against many FPGA objects
    :param fpga_list: list of KatcpClientFpga objects
    :param timeout: how long to wait before timing out
    :param target_function: a tuple with three parts:
                            1. reference, the function object that must be
                               run - MUST take FPGA object as first argument
                            2. tuple, the arguments to the function
                            3. dict, the keyword arguments to the function
                            e.g. (func_name, (1,2,), {'another_arg': 3})
    :return: a dictionary of the results, keyed on hostname
    """
    target_function = _check_target_func(target_function)

    def jobfunc(resultq, fpga):
        rv = target_function[0](fpga, *target_function[1], **target_function[2])
        resultq.put_nowait((fpga.host, rv))

    num_fpgas = len(fpga_list)
    result_queue = Queue.Queue(maxsize=num_fpgas)
    thread_list = []
    for fpga_ in fpga_list:
        thread = threading.Thread(target=jobfunc, args=(result_queue, fpga_))
        thread.setDaemon(True)
        thread.start()
        thread_list.append(thread)
    for thread_ in thread_list:
        thread_.join(timeout)
        if thread_.isAlive():
            break
    returnval = {}
    hosts_missing = [fpga.host for fpga in fpga_list]
    while True:
        try:
            result = result_queue.get_nowait()
            returnval[result[0]] = result[1]
            hosts_missing.pop(hosts_missing.index(result[0]))
        except Queue.Empty:
            break
    if hosts_missing:
        errmsg = 'Ran \'%s\' on hosts. Did not get a response ' \
                 'from %s.' % (target_function[0].__name__, hosts_missing)
        LOGGER.error(errmsg)
    return returnval


def threaded_non_blocking_request(fpga_list, timeout, request, request_args):
    """
    Make a non-blocking KatCP request to a list of KatcpClientFpgas, using
    the Asynchronous client.
    :param fpga_list: list of KatcpClientFpga objects
    :param timeout: the request timeout
    :param request: the request string
    :param request_args: the arguments to the request, as a list
    :return: a dictionary, keyed by hostname, of result dictionaries containing
    reply and informs
    """

    raise DeprecationWarning

    num_fpgas = len(fpga_list)
    reply_queue = Queue.Queue(maxsize=num_fpgas)
    requests = {}
    replies = {}

    # reply callback
    def reply_cb(host, req_id):
        LOGGER.debug('Reply(%s) from host(%s)' % (req_id, host))
        reply_queue.put_nowait([host, req_id])

    # start the requests
    LOGGER.debug('Send request(%s) to %i hosts.' % (request, num_fpgas))
    lock = threading.Lock()
    for fpga_ in fpga_list:
        lock.acquire()
        req = fpga_.nb_request(request, None, reply_cb, *request_args)
        requests[req['host']] = [req['request'], req['id']]
        lock.release()
        LOGGER.debug('Request \'%s\' id(%s) to host(%s)' % (
            req['request'], req['id'], req['host']))

    # wait for replies from the requests
    timedout = False
    done = False
    while (not timedout) and (not done):
        try:
            it = reply_queue.get(block=True, timeout=timeout)
        except:
            timedout = True
            break
        replies[it[0]] = it[1]
        if len(replies) == num_fpgas:
            done = True
    if timedout:
        LOGGER.error('non_blocking_request timeout after %is.' % timeout)
        LOGGER.error(replies)
        raise RuntimeError('non_blocking_request timeout after %is.' % timeout)

    # process the replies
    returnval = {}
    for fpga_ in fpga_list:
        try:
            request_id = replies[fpga_.host]
        except KeyError:
            LOGGER.error(replies)
            raise KeyError(
                'Didn\'t get a reply for FPGA \'%s\' so the request \'%s\' '
                'probably didn\'t complete.' % (fpga_.host, request))
        reply, informs = fpga_.nb_get_request_result(request_id)
        frv = {'request': requests[fpga_.host][0],
               'reply': reply.arguments[0],
               'reply_args': reply.arguments}
        informlist = []
        for inf in informs:
            informlist.append(inf.arguments)
        frv['informs'] = informlist
        returnval[fpga_.host] = frv
        fpga_.nb_pop_request_by_id(request_id)
    return returnval

