'''

input_data:
  backup_interval_check: 20
  backup_timeout: 7200
  bash_profile_name: bash_profile.txt
  disksize: 2048
  disktype: thin
  hdd_volumepath: /dev/sdb
  sleep_interval: 90
  supported_version: [5.1,5.5,6.0]
  volumereq: 1

if above is yml file and you have to modify  the supported version to only 5.1

'''

import io
import yaml
#with io.FileIO("/operate.yml", "r") as file:
#    data = file.read()
#    file.close()

#print data
#print type(data)

fh1 = open("/operate.yml", 'r+')  # open the file in read mode
data = yaml.safe_load(fh1)        #load the data
fh1.close()
print data
print type(data)
print data['input_data']['supported_version']

fname = "/operate.yml"
#dct = {'input_data': {'supported_version' : "[5.1]"}}
data['input_data']['supported_version'] = "[5.1]"   #modify only that value in the data
with open(fname, "w") as f: #open the file in write mode
    yaml.dump(data, f)      #dump whole data

with open(fname) as f:
    newdct = yaml.load(f)   #load the data in dictionary

print newdct # this will print the dictionary
