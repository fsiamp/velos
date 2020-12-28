# VELOS - IDS Evaluation Dataset Generator

![alt tag](https://github.com/SecDOOM/velos/raw/master/logo.png)

VELOS is a tool that helps you generate and export intrusion evaluation datasets. 

Basically, it automates the extraction process by applying a simulation environment of network intrusion detection systems. 

During dataset creation, VELOS uses 48 attributes many of which are used also on KDD Cup 99.


# Dataset Attributes

```duration

protocol{'tcp', 'udp','icmp'}

flag {'OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH'}

src_bytes

dst_bytes 

land 
wrong_fragment

urgent

hot

num_failed_logins

logged_in

num_compromised

root_shell

su_attempted

service {'aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u', 'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest', 'hostnames', 'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell', 'ldap', 'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i', 'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time', 'urh_i', 'urp_i', 'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50'}

num_root
num_file_creations 

num_shells
num_access_files

num_outbound_cmds

is_host_login 
is_guest_login

count

srv_count

serror_rate

srv_serror_rate

rerror_rate

srv_rerror_rate

src_port
dst_port

average_rtt

iplen

ethlen

stan_dev_rtt

same_srv_rate

diff_srv_rate

srv_diff_host_rate

dst_host_count

dst_host_srv_count

dst_host_same_srv_rate

dst_host_diff_srv_rate

dst_host_same_src_port_rate

dst_host_srv_diff_host_rate

dst_host_serror_rate

dst_host_srv_serror_rate

dst_host_rerror_rate

dst_host_srv_rerror_rate

class {'attempted-admin','attempted-user','inappropriate-content','policy-violationn','shellcode-detect','successful-admin','successful-user', 'trojan-activity','unsuccessful-user','web-application-attack','attempted-dos','attempted-recon','bad-unknown','default-login-attempt','denial-of-service','misc-attack','non-standard-protocol','rpc-portmap-decode','successful-dos','successful-recon-largescale', 'successful-recon-limited','suspicious-filename-detect','suspicious-login','system-call-detect','unusual-client-port-connection','web-application-activity','icmp-event','misc-activity','network-scan','not-suspicious','protocol-command-decode','string-detect','unknown','tcp-connection'}
