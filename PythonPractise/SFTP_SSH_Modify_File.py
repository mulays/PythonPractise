'''
cat /operate.yml
input_data:
  backup_interval_check: 20
  backup_timeout: 7200
  sleep_interval: 90
  supported_version: [5.1,5.5,6.0]
  test_createvm_input_file: /opt/product/config/input.yml
  test_createvm_input_file_path: /opt/product/config/
  test_password: password
  volumereq: 1

above is yml file on the server change value [[5.1,5.5,6.0] to NA
'''

import paramiko
import yaml

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("IP", username="stack", password="stack")

stdin, stdout, stderr = ssh.exec_command("cat /operate.yml")
data1 = yaml.safe_load(stdout.read())
version = data1['input_data']['supported_version']
data1['input_data']['supported_version'] = [5.1]
ftp = ssh.open_sftp()
file=ftp.file('/operate.yml', "w", -1)
file.write(yaml.safe_dump(data1))
file.flush()
ftp.close()
ssh.close()
