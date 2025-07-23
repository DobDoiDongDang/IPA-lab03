import paramiko
import time

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('172.31.38.4', username='admin', key_filename='"C:\Users\darks\Desktop\KEY\admin.ppk"')

stdin, stdout, stderr = ssh.exec_command('ls')

print stdout.readlines()
ssh.close()