# cat /tmp/sub.py
import subprocess
import collections
import shlex
def call_sub(c):
    subprocess.call(c)


a = call_sub("ifconfig") # it just executes the command so output is NONE
print "a : ",a


def cmd(c):
    CmdResult = collections.namedtuple('CmdResult',
        ['output', 'returncode'])
        #['stdout', 'stderr', 'returncode'])
    p = subprocess.Popen(c,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    o, e = p.communicate()
    return CmdResult(o, p.returncode)

a = cmd("ifconfig")  #it executes the command and stores output
print "a : ",a

def call_sub2(ip_addr):

    try :
        c=shlex.split("ping -c1 {}".format(ip_addr))
        subprocess.check_output(c)
        return True
    except :
        print "In except : "
        return False


a = call_sub2("177.20.249.5") # this ip is pingeable so should return True
print "a : ",a



# python /tmp/sub.py
eth0      Link encap:Ethernet  HWaddr 0D:5D:5A:9C:73:2C
          inet addr:177.20.249.5  Bcast:177.20.249.255  Mask:255.255.255.0
          inet6 addr: fe80::250:56ff:fe9c:732c/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:12130 errors:0 dropped:12 overruns:0 frame:0
          TX packets:9248 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:24433673 (23.3 Mb)  TX bytes:2027624 (1.9 Mb)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:32 errors:0 dropped:0 overruns:0 frame:0
          TX packets:32 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:2888 (2.8 Kb)  TX bytes:2888 (2.8 Kb)

a :  None
a :  CmdResult(output='eth0      Link encap:Ethernet  HWaddr 0D:5D:5A:9C:73:2C  \n          inet addr:177.20.249.5  Bcast:177.20.249.255  Mask:255.255.255.0\n          inet6 addr: fe80::250:56ff:fe9c:732c/64 Scope:Link\n          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\n          RX packets:12138 errors:0 dropped:12 overruns:0 frame:0\n          TX packets:9265 errors:0 dropped:0 overruns:0 carrier:0\n          collisions:0 txqueuelen:1000 \n          RX bytes:24434153 (23.3 Mb)  TX bytes:2030558 (1.9 Mb)\n\nlo        Link encap:Local Loopback  \n          inet addr:127.0.0.1  Mask:255.0.0.0\n          inet6 addr: ::1/128 Scope:Host\n          UP LOOPBACK RUNNING  MTU:65536  Metric:1\n          RX packets:32 errors:0 dropped:0 overruns:0 frame:0\n          TX packets:32 errors:0 dropped:0 overruns:0 carrier:0\n          collisions:0 txqueuelen:0 \n          RX bytes:2888 (2.8 Kb)  TX bytes:2888 (2.8 Kb)\n\n', returncode=0)
a :  True
