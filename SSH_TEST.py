from netmiko import ConnectHandler
device_ip = '172.31.38.'
username = 'admin'
password = 'cisco'
for i in range(1, 6):
    print("Start SSH to "+device_ip+str(i))
    device_params = {
        'device_type' : 'cisco_ios', 
        'ip': device_ip+str(i), 
        'username': username, 
        'password': password, }
    with ConnectHandler(**device_params) as ssh:
        result = ssh.send_command("sh run | grep hostname")
        print(result.strip())