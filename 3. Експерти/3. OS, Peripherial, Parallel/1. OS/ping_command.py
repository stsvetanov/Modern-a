import os
import subprocess

ip_address = "192.168.1.4"
hostname = ip_address
output = subprocess.Popen(["ping.exe", hostname], stdout=subprocess.PIPE).communicate()[0]
output = output.decode()
print(output)

if 'unreachable' in output:
    print("Offline")

#
# import pyping
# r = pyping.ping('google.com')
#
# if r.ret_code == 0:
#     print("Success")
# else:
#     print("Failed with {}".format(r.ret_code))