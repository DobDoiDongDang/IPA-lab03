from netmiko import ConnectHandler
from dotenv import load_dotenv

import os
#import logging
#logging.basicConfig(filename="ssh_log", level=logging.DEBUG) Just for loggin authen dont worry
def createdevice(ip):#Create template for all device
    load_dotenv()
    privatekey = os.getenv("PRIVATE_PATH")
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'use_keys': True,
        'key_file': privatekey, #Dont worry only ai i use in this lab is just gimini in google search
        "disabled_algorithms":dict(pubkeys=['rsa-sha2-512', 'rsa-sha2-256'])
    }
    return device


network = str(input("your network example : 172.31.30. \n"))
last_num = str(input("device ip last number example : 4 \n"))
device1 = createdevice(network+last_num)
interface = str(input("interface example : g0/1 \n"))
up_down = str(input("up or down interface ? \n"))

up_config_commands = ["int "+interface, "no shut", "exit"]
down_config_commands = ["int "+interface, "shut", "exit"]
device_connnect = ConnectHandler(**device1)
if (up_down == "up"):
    output = device_connnect.send_config_set(up_config_commands)
    print(output)
elif (up_down == "down"):
    output = device_connnect.send_config_set(down_config_commands)
    print(output)
else:
    print("error pls type up or down only")
device_connnect.disconnect()

