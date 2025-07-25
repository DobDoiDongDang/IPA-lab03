import paramiko
import time
import os

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
""" pkey=key, look_for_keys=True """
ssh.connect(hostname='172.31.38.1', username='admin', key_filename="C:\\Users\\darks\\Desktop\\KEY\\opensshadmin",allow_agent=False,look_for_keys=False)
ssh.close()