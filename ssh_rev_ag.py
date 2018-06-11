import pexpect
#import os

#os.system('ssh-agent -s; ssh-add /home/miaou/priv_keys; ssh-agent bash')

"""
 using a function to do the connection and creating a file *
 on the remote server
 10/06/18 : adding part of your prompt on it, the distant server 
 prompt is 
 [pi:/home/pi]$ 
 or using child.expect('pi')
"""


def conn_wr():
    child = pexpect.spawn('ssh pi@192.168.1.32')
    child.expect('password:')
    child.sendline('XXX')
    child.expect('pi')
    child.sendline('touch 123toto.txt')
    child.expect('pi') 
    child.sendline('exit')    


# the same (or almost) as above but without the function

child = pexpect.spawn('ssh pi@192.168.1.32')
child.expect('password:')
child.sendline('XXX')
child.sendline('touch 123toto.txt')
child.sendline('exit')    
