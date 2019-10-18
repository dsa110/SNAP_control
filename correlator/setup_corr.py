import sys, subprocess, os
from time import sleep

big_nbytes = '402653184'
nbytes_many = '49152000'
nbytes_many2 = '943718400'
nbytes_final = '42240000'
#nbytes_final = '417792000'
nsamps = '49152'
nwait = '63000'
nn = '384'


# machine to set up
machine = sys.argv[1]

dbuffers=0
cbuffers=0
start_rx=0
start_tx=0
stop=0

# all in one start and stop
if (sys.argv[2]=='go'):
    cbuffers=1
    start_rx=1
    start_tx=1
if (sys.argv[2]=='halt'):
    stop=1
    dbuffers=1

if (sys.argv[2]=='destroy'):
    dbuffers=1
if (sys.argv[2]=='create'):
    cbuffers=1
if (sys.argv[2]=='start_rx'):
    start_rx=1
if (sys.argv[2]=='start_tx'):
    start_tx=1
if (sys.argv[2]=='stop'):
    stop=1
    
# create buffers

if cbuffers:
    print 'creating dada buffers on ',machine
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k caca -b 402653184 -l -p -c 0 -n 8"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k dbda -b 49152000 -l -p -c 0 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k dcda -b 49152000 -l -p -c 0 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k ddda -b 49152000 -l -p -c 0 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k ebda -b 49152000 -l -p -c 0 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k ecda -b 49152000 -l -p -c 0 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k adbd -b 49152000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k adcd -b 49152000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k addd -b 49152000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k aaaa -b 49152000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k aaba -b 49152000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bdad -b 98304000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bdcd -b 98304000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bddd -b 98304000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bbbb -b 98304000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bbab -b 98304000 -l -p -c 1 -n 4"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k eada -b 42240000 -l -p -c 1 -n 4"')


# processes


if machine=='dsamaster':
    capture = '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread -b 1 -f /mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt -k caca -i 10.10.5.1 -p 4011'
    dbnic1 = '/usr/local/dsaX/bin/dsaX_dbnic -k dbda -i 10.10.4.1 -p 7016 -c 3 -n '+nwait
    dbnic2 = '/usr/local/dsaX/bin/dsaX_dbnic -k dcda -i 10.10.4.2 -p 7016 -c 4 -n '+nwait
    dbnic3 = '/usr/local/dsaX/bin/dsaX_dbnic -k ddda -i 10.10.4.3 -p 7016 -c 5 -n '+nwait
    dbnic4 = '/usr/local/dsaX/bin/dsaX_dbnic -k ebda -i 10.10.4.4 -p 7016 -c 6 -n '+nwait
    dbnic5 = '/usr/local/dsaX/bin/dsaX_dbnic -k ecda -i 10.10.4.5 -p 7016 -c 7 -n '+nwait
    nicdb1 = '/usr/local/dsaX/bin/dsaX_nicdb -k adbd -p 7016 -c 8 -b '+nbytes_many+' -i 10.10.4.1'
    nicdb2 = '/usr/local/dsaX/bin/dsaX_nicdb -k adcd -p 7015 -c 9 -b '+nbytes_many+' -i 10.10.4.1'
    nicdb3 = '/usr/local/dsaX/bin/dsaX_nicdb -k addd -p 7014 -c 10 -b '+nbytes_many+' -i 10.10.4.1'
    nicdb4 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaaa -p 7013 -c 11 -b '+nbytes_many+' -i 10.10.4.1'
    nicdb5 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaba -p 7012 -c 12 -b '+nbytes_many+' -i 10.10.4.1'
    final = '/usr/local/dsaX/bin/dsaX_writevis -c 13 -f /home/user/data/run1/dsa0 -o 1487.27539 -i 10.10.1.1'
    
if machine=='dsa1':
    capture = '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread -b 1 -f /mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt -k caca -i 10.10.6.1 -p 4011'
    dbnic1 = '/usr/local/dsaX/bin/dsaX_dbnic -k dbda -i 10.10.4.1 -p 7015 -c 3 -n '+nwait
    dbnic2 = '/usr/local/dsaX/bin/dsaX_dbnic -k dcda -i 10.10.4.2 -p 7015 -c 4 -n '+nwait
    dbnic3 = '/usr/local/dsaX/bin/dsaX_dbnic -k ddda -i 10.10.4.3 -p 7015 -c 5 -n '+nwait
    dbnic4 = '/usr/local/dsaX/bin/dsaX_dbnic -k ebda -i 10.10.4.4 -p 7015 -c 6 -n '+nwait
    dbnic5 = '/usr/local/dsaX/bin/dsaX_dbnic -k ecda -i 10.10.4.5 -p 7015 -c 7 -n '+nwait
    nicdb1 = '/usr/local/dsaX/bin/dsaX_nicdb -k adbd -p 7016 -c 8 -b '+nbytes_many+' -i 10.10.4.2'
    nicdb2 = '/usr/local/dsaX/bin/dsaX_nicdb -k adcd -p 7015 -c 9 -b '+nbytes_many+' -i 10.10.4.2'
    nicdb3 = '/usr/local/dsaX/bin/dsaX_nicdb -k addd -p 7014 -c 10 -b '+nbytes_many+' -i 10.10.4.2'
    nicdb4 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaaa -p 7013 -c 11 -b '+nbytes_many+' -i 10.10.4.2'
    nicdb5 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaba -p 7012 -c 12 -b '+nbytes_many+' -i 10.10.4.2'
    final = '/usr/local/dsaX/bin/dsaX_writevis -c 13 -f /home/user/data/run1/dsa1 -o 1456.75781  -i 10.10.1.7'
    
if machine=='dsa2':
    capture = '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread -b 1 -f /mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt -k caca -i 10.10.7.1 -p 4011'
    dbnic1 = '/usr/local/dsaX/bin/dsaX_dbnic -k dbda -i 10.10.4.1 -p 7014 -c 3 -n '+nwait
    dbnic2 = '/usr/local/dsaX/bin/dsaX_dbnic -k dcda -i 10.10.4.2 -p 7014 -c 4 -n '+nwait
    dbnic3 = '/usr/local/dsaX/bin/dsaX_dbnic -k ddda -i 10.10.4.3 -p 7014 -c 5 -n '+nwait
    dbnic4 = '/usr/local/dsaX/bin/dsaX_dbnic -k ebda -i 10.10.4.4 -p 7014 -c 6 -n '+nwait
    dbnic5 = '/usr/local/dsaX/bin/dsaX_dbnic -k ecda -i 10.10.4.5 -p 7014 -c 7 -n '+nwait
    nicdb1 = '/usr/local/dsaX/bin/dsaX_nicdb -k adbd -p 7016 -c 8 -b '+nbytes_many+' -i 10.10.4.3'
    nicdb2 = '/usr/local/dsaX/bin/dsaX_nicdb -k adcd -p 7015 -c 9 -b '+nbytes_many+' -i 10.10.4.3'
    nicdb3 = '/usr/local/dsaX/bin/dsaX_nicdb -k addd -p 7014 -c 10 -b '+nbytes_many+' -i 10.10.4.3'
    nicdb4 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaaa -p 7013 -c 11 -b '+nbytes_many+' -i 10.10.4.3'
    nicdb5 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaba -p 7012 -c 12 -b '+nbytes_many+' -i 10.10.4.3'
    final = '/usr/local/dsaX/bin/dsaX_writevis -c 13 -f /home/user/data/run1/dsa2 -o 1426.24023  -i 10.10.1.8'
    
if machine=='dsa3':
    capture = '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread -b 1 -f /mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt -k caca -i 10.10.8.1 -p 4011'
    dbnic1 = '/usr/local/dsaX/bin/dsaX_dbnic -k dbda -i 10.10.4.1 -p 7013 -c 3 -n '+nwait
    dbnic2 = '/usr/local/dsaX/bin/dsaX_dbnic -k dcda -i 10.10.4.2 -p 7013 -c 4 -n '+nwait
    dbnic3 = '/usr/local/dsaX/bin/dsaX_dbnic -k ddda -i 10.10.4.3 -p 7013 -c 5 -n '+nwait
    dbnic4 = '/usr/local/dsaX/bin/dsaX_dbnic -k ebda -i 10.10.4.4 -p 7013 -c 6 -n '+nwait
    dbnic5 = '/usr/local/dsaX/bin/dsaX_dbnic -k ecda -i 10.10.4.5 -p 7013 -c 7 -n '+nwait
    nicdb1 = '/usr/local/dsaX/bin/dsaX_nicdb -k adbd -p 7016 -c 8 -b '+nbytes_many+' -i 10.10.4.4'
    nicdb2 = '/usr/local/dsaX/bin/dsaX_nicdb -k adcd -p 7015 -c 9 -b '+nbytes_many+' -i 10.10.4.4'
    nicdb3 = '/usr/local/dsaX/bin/dsaX_nicdb -k addd -p 7014 -c 10 -b '+nbytes_many+' -i 10.10.4.4'
    nicdb4 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaaa -p 7013 -c 11 -b '+nbytes_many+' -i 10.10.4.4'
    nicdb5 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaba -p 7012 -c 12 -b '+nbytes_many+' -i 10.10.4.4'
    final = '/usr/local/dsaX/bin/dsaX_writevis -c 13 -f /home/user/data/run1/dsa3 -o 1395.72266  -i 10.10.1.9'
    
if machine=='dsa4':
    capture = '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread -b 1 -f /mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt -k caca -i 10.10.9.1 -p 4011'
    dbnic1 = '/usr/local/dsaX/bin/dsaX_dbnic -k dbda -i 10.10.4.1 -p 7012 -c 3 -n '+nwait
    dbnic2 = '/usr/local/dsaX/bin/dsaX_dbnic -k dcda -i 10.10.4.2 -p 7012 -c 4 -n '+nwait
    dbnic3 = '/usr/local/dsaX/bin/dsaX_dbnic -k ddda -i 10.10.4.3 -p 7012 -c 5 -n '+nwait
    dbnic4 = '/usr/local/dsaX/bin/dsaX_dbnic -k ebda -i 10.10.4.4 -p 7012 -c 6 -n '+nwait
    dbnic5 = '/usr/local/dsaX/bin/dsaX_dbnic -k ecda -i 10.10.4.5 -p 7012 -c 7 -n '+nwait
    nicdb1 = '/usr/local/dsaX/bin/dsaX_nicdb -k adbd -p 7016 -c 8 -b '+nbytes_many+' -i 10.10.4.5'
    nicdb2 = '/usr/local/dsaX/bin/dsaX_nicdb -k adcd -p 7015 -c 9 -b '+nbytes_many+' -i 10.10.4.5'
    nicdb3 = '/usr/local/dsaX/bin/dsaX_nicdb -k addd -p 7014 -c 10 -b '+nbytes_many+' -i 10.10.4.5'
    nicdb4 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaaa -p 7013 -c 11 -b '+nbytes_many+' -i 10.10.4.5'
    nicdb5 = '/usr/local/dsaX/bin/dsaX_nicdb -k aaba -p 7012 -c 12 -b '+nbytes_many+' -i 10.10.4.5'
    final = '/usr/local/dsaX/bin/dsaX_writevis -c 13 -f /home/user/data/run1/dsa4 -o 1365.20508  -i 10.10.1.10'

fanout = '/usr/local/dsaX/bin/dsaX_correlator_fanout -c 2 -n '+nsamps
massager = '/usr/local/dsaX/bin/dsaX_fancy -c 14 -n '+nbytes_final

ar1 = '/usr/local/dsaX/bin/dsaX_single -k adbd -o bdad -c 24'
ar2 = '/usr/local/dsaX/bin/dsaX_single -k adcd -o bdcd -c 25'
ar3 = '/usr/local/dsaX/bin/dsaX_single -k addd -o bddd -c 26'
ar4 = '/usr/local/dsaX/bin/dsaX_single -k aaaa -o bbbb -c 27'
ar5 = '/usr/local/dsaX/bin/dsaX_single -k aaba -o bbab -c 28'

cpscr = '/usr/local/dsaX/bin/cpscr.bash '+machine

# start things up

if start_rx:

    print 'Starting cpscr'
    cpscr_log = open('/mnt/nfs/runtime/tmplog/cpscr_log_'+machine+'.log','w')
    cpscr_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+cpscr+'"', shell = True, stdout=cpscr_log, stderr=cpscr_log)
    sleep(0.1)
    
    print 'Starting final'
    final_log = open('/mnt/nfs/runtime/tmplog/final_log_'+machine+'.log','w')
    final_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+final+'"', shell = True, stdout=final_log, stderr=final_log)
    sleep(0.1)
    
    print 'Starting massager'
    massager_log = open('/mnt/nfs/runtime/tmplog/massager_log_'+machine+'.log','w')
    massager_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+massager+'"', shell = True, stdout=massager_log, stderr=massager_log)
    sleep(0.1)

    print 'Starting expands'
    ar1_log = open('/mnt/nfs/runtime/tmplog/ar1_log_'+machine+'.log','w')
    ar1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+ar1+'"', shell = True, stdout=ar1_log, stderr=ar1_log)
    sleep(0.1)
    ar2_log = open('/mnt/nfs/runtime/tmplog/ar2_log_'+machine+'.log','w')
    ar2_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+ar2+'"', shell = True, stdout=ar2_log, stderr=ar2_log)
    sleep(0.1)
    ar3_log = open('/mnt/nfs/runtime/tmplog/ar3_log_'+machine+'.log','w')
    ar3_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+ar3+'"', shell = True, stdout=ar3_log, stderr=ar3_log)
    sleep(0.1)
    ar4_log = open('/mnt/nfs/runtime/tmplog/ar4_log_'+machine+'.log','w')
    ar4_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+ar4+'"', shell = True, stdout=ar4_log, stderr=ar4_log)
    sleep(0.1)
    ar5_log = open('/mnt/nfs/runtime/tmplog/ar5_log_'+machine+'.log','w')
    ar5_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+ar5+'"', shell = True, stdout=ar5_log, stderr=ar5_log)
    sleep(0.1)
    
    print 'Starting nicdbs'
    ndb1_log = open('/mnt/nfs/runtime/tmplog/ndb1_log_'+machine+'.log','w')
    ndb1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+nicdb1+'"', shell = True, stdout=ndb1_log, stderr=ndb1_log)
    sleep(0.1)
    ndb2_log = open('/mnt/nfs/runtime/tmplog/ndb2_log_'+machine+'.log','w')
    ndb2_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+nicdb2+'"', shell = True, stdout=ndb2_log, stderr=ndb2_log)
    sleep(0.1)
    ndb3_log = open('/mnt/nfs/runtime/tmplog/ndb3_log_'+machine+'.log','w')
    ndb3_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+nicdb3+'"', shell = True, stdout=ndb3_log, stderr=ndb3_log)
    sleep(0.1)
    ndb4_log = open('/mnt/nfs/runtime/tmplog/ndb4_log_'+machine+'.log','w')
    ndb4_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+nicdb4+'"', shell = True, stdout=ndb4_log, stderr=ndb4_log)
    sleep(0.1)
    ndb5_log = open('/mnt/nfs/runtime/tmplog/ndb5_log_'+machine+'.log','w')
    ndb5_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+nicdb5+'"', shell = True, stdout=ndb5_log, stderr=ndb5_log)
    sleep(0.1)

if start_tx:
    
    print 'Starting dbnics'
    db1_log = open('/mnt/nfs/runtime/tmplog/db1_log_'+machine+'.log','w')
    db1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+dbnic1+'"', shell = True, stdout=db1_log, stderr=db1_log)
    sleep(0.1)
    db2_log = open('/mnt/nfs/runtime/tmplog/db2_log_'+machine+'.log','w')
    db2_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+dbnic2+'"', shell = True, stdout=db2_log, stderr=db2_log)
    sleep(0.1)
    db3_log = open('/mnt/nfs/runtime/tmplog/db3_log_'+machine+'.log','w')
    db3_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+dbnic3+'"', shell = True, stdout=db3_log, stderr=db3_log)
    sleep(0.1)
    db4_log = open('/mnt/nfs/runtime/tmplog/db4_log_'+machine+'.log','w')
    db4_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+dbnic4+'"', shell = True, stdout=db4_log, stderr=db4_log)
    sleep(0.1)
    db5_log = open('/mnt/nfs/runtime/tmplog/db5_log_'+machine+'.log','w')
    db5_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+dbnic5+'"', shell = True, stdout=db5_log, stderr=db5_log)
    sleep(0.1)
    
    print 'Starting fanout'
    fanout_log = open('/mnt/nfs/runtime/tmplog/fanout_log_'+machine+'.log','w')
    fanout_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+fanout+'"', shell = True, stdout=fanout_log, stderr=fanout_log)
    sleep(0.1)
    
    print 'Starting captures'
    capture_log = open('/mnt/nfs/runtime/tmplog/capture_log_'+machine+'.log','w')
    capture_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+capture+'"', shell = True, stdout=capture_log, stderr=capture_log)
    sleep(0.1)

    
if stop:

    print 'Killing everything'
    
    output0 = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_correlator_udpdb_thread"',shell=True)
    subprocess.Popen.wait(output0)

    output0 = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_correlator_fanout"',shell=True)
    subprocess.Popen.wait(output0)

    output0 = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_dbnic"',shell=True)
    subprocess.Popen.wait(output0)

    output0 = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_nicdb"',shell=True)
    subprocess.Popen.wait(output0)

    output0 = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_single"',shell=True)
    subprocess.Popen.wait(output0)

    output0 = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_fancy"',shell=True)
    subprocess.Popen.wait(output0) 

    output0 = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_writevis"',shell=True)
    subprocess.Popen.wait(output0)

    output0 = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; killall -q cpscr.bash"',shell=True)
    subprocess.Popen.wait(output0)

    
# dada buffers

if dbuffers:
    
    print 'destroying dada buffers on ',machine
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k dbda -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k dcda -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k ddda -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k ebda -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k ecda -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k adbd -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k adcd -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k addd -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k aaaa -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k aaba -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bdad -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bdcd -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bddd -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bbbb -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k bbab -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k eada -d"')
    os.system('ssh user@'+machine+' "source ~/.bashrc; dada_db -k caca -d"')
