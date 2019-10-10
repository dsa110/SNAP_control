""" snap_util contains helper functions related to configuring and running
    SNAP boards.
"""
import yaml


def fpga_encode_helper(arr):
    ''' input integer array and return:
        arr[-1] * 2**0 + arr[-2] * 2**1 + ...
    '''
    val = 0
    pwr_coeff = 0
    for idx in range(len(arr) - 1, -1, -1):
        val += (int(arr[idx]) * (2 ** pwr_coeff))
        pwr_coeff += 8

    return val


def fpga_encode_ip(ip_addr):
    ''' encode ip_address of the form 1.1.1.1
    '''
    ip_arr = ip_addr.split('.')
    return fpga_encode_helper(ip_arr)


def fpga_encode_mac(mac_address):
    ''' encode mac_address of the form 11:11:11:11:11:11
        values represent hex numbers.
    '''
    mac_arr = mac_address.split(':')
    # convert ascii hex into int
    mac_int_arr = [int(v, 16) for v in mac_arr]
    return fpga_encode_helper(mac_int_arr)


def read_yaml(yml_fn):
    """Read a YAML formatted file.

    :param yml_fn: YAML formatted filename"
    :type yml_fn: String
    :return: Dictionary on success. None on error
    :rtype: Dictionary
    """

    with open(yml_fn, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            # TODO: log exception
            return None