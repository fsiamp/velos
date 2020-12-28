#!/usr/bin/python

import random
import decimal
import time
from random import randint
attack = ['attempted-admin','attempted-user','inappropriate-content','policy-violationn','shellcode-detect','successful-admin','successful-user', 'trojan-activity','unsuccessful-user','web-application-attack','attempted-dos','attempted-recon','bad-unknown','default-login-attempt','denial-of-service','misc-attack','non-standard-protocol','rpc-portmap-decode','successful-dos','successful-recon-largescale', 'successful-recon-limited','suspicious-filename-detect','suspicious-login','system-call-detect','unusual-client-port-connection','web-application-activity','icmp-event','misc-activity','network-scan','not-suspicious','protocol-command-decode','string-detect','unknown','tcp-connection', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal']

protocol = [ 'tcp', 'udp','icmp']
service = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u', 'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest', 'hostnames', 'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell', 'ldap', 'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i', 'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time', 'urh_i', 'urp_i', 'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50'] 
flag = [ 'OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH' ]

counter2 = randint(100,2000)


print '\r'
var = randint(3000,8000)
print 'Generating Dataset ...'
print '\r'
time.sleep(1)

count = 1 

file1 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file2 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file3 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file4 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file5 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file6 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file7 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file8 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file9 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")
file10 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789")

f = open('datasets/' + file1 + file2 + file3 + file4 + file5 + file6 + file7 + file8 + file9 + file10 + '.data','w')


   
while (count <= var):
       duration = str(randint(0,255))
       src_bytes = str(randint(0,255))
       dst_bytes = str(randint(0,255))
       land = str(randint(0,1))
       wrong_fragment = str(randint(0,255))
       urgent = str(randint(0,255))
       hot = str(randint(0,255))
       num_failed_logins = str(randint(0,255))
       logged_in = str(randint(0,1))
       num_compromised = str(randint(0,255))
       root_shell = str(randint(0,155))
       su_attempted = str(randint(0,99255))
       num_root = str(randint(0,99255))
       num_file_creations = str(randint(0,99255))
       num_shells = str(randint(0,99255))  
       num_access_files = str(randint(0,99255))  
       num_outbound_cmds = str(randint(0,700))  
       is_host_login = str(randint(0,1))  
       is_guest_login = str(randint(0,1)) 
       countz= str(randint(0,1000)) 
       srv_count = str(randint(0,1000)) 
       serror_rate = str(randint(0,100)/100)
       srv_serror_rate = str(decimal.Decimal(random.randrange(100))/100)
       rerror_rate = str(decimal.Decimal(random.randrange(100))/100)
       srv_rerror_rate = str(decimal.Decimal(random.randrange(100))/100)
       src_port= str(randint(0,65535))
       dst_port= str(randint(0,65535)) 
       average_rtt = str(randint(0,500))
       iplen = str(randint(0,400)) 
       ethlen = str(randint(0,400)) 
       stan_dev_rtt = str(randint(0,500))  
       same_srv_rate = str(decimal.Decimal(random.randrange(100))/100)
       diff_srv_rate = str(decimal.Decimal(random.randrange(100))/100)
       srv_diff_host_rate = str(decimal.Decimal(random.randrange(100))/100)
       dst_host_count = str(randint(0,1000))
       dst_host_srv_count = str(randint(0,1000))
       dst_host_same_srv_rate = str(decimal.Decimal(random.randrange(100))/100)
       dst_host_diff_srv_rate = str(decimal.Decimal(random.randrange(100))/100) 
       dst_host_same_src_port_rate = str(decimal.Decimal(random.randrange(100))/100)
       dst_host_srv_diff_host_rate = str(decimal.Decimal(random.randrange(100))/100)
       dst_host_serror_rate = str(decimal.Decimal(random.randrange(100))/100)
       dst_host_srv_serror_rate = str(decimal.Decimal(random.randrange(100))/100)
       dst_host_rerror_rate = str(decimal.Decimal(random.randrange(100))/100)
       dst_host_srv_rerror_rate = str(decimal.Decimal(random.randrange(100))/100)

       capture = duration + ',' + random.choice(protocol) + ',' + random.choice(flag) + ',' + src_bytes + ',' + dst_bytes + ',' + land + ',' + wrong_fragment + ',' + urgent + ',' + hot + ',' + num_failed_logins + ',' + logged_in + ',' + num_compromised + ',' + root_shell + ',' + su_attempted + ',' + random.choice(service) + ',' +  num_root + ',' + num_file_creations + ',' + num_shells + ',' + num_access_files + ',' + num_outbound_cmds + ',' + is_host_login + ',' + is_guest_login + ',' + countz + ',' + srv_count + ',' + serror_rate + ',' + srv_serror_rate + ',' + rerror_rate + ',' + srv_rerror_rate + ',' + src_port + ',' + dst_port + ',' + average_rtt + ',' + iplen + ',' + ethlen + ',' + stan_dev_rtt + ',' + same_srv_rate + ',' + diff_srv_rate + ',' + srv_diff_host_rate + ',' + dst_host_count + ',' + dst_host_srv_count + ',' + dst_host_same_srv_rate + ',' + dst_host_diff_srv_rate + ',' + dst_host_same_src_port_rate + ',' + dst_host_srv_diff_host_rate + ',' + dst_host_serror_rate + ',' + dst_host_srv_serror_rate + ',' + dst_host_rerror_rate + ',' + dst_host_srv_rerror_rate + ',' + random.choice(attack)
       
       f.write(capture + '\n') 
       count = count + 1
 

print 'New dataset was exported successfully to',file1 + file2 + file3 + file4 + file5 + file6 + file7 + file8 + file9 + file10 + '.data'

f.close() 
print '\r'

