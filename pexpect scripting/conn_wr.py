import pexpect
#import os

#os.system('ssh-agent -s; ssh-add /home/miaou/priv_keys; ssh-agent bash')

"""
 creating a function, conn_wr to do the connection and creating a file 123toto.txt
 on the remote server
 
 10/06/18 : adding part of your prompt on it, the distant server 
 prompt is 
 [pi:/home/pi]$ 
 or using child.expect('pi')
"""

# this method is for programs like sftp or ssh, which needs some human interactions

def conn_wr():
    child = pexpect.spawn('ssh pi@192.168.1.32')
    child.expect('password:')
    child.sendline('XXX')
    child.expect('pi')
    child.sendline('touch 123toto.txt')
    child.expect('pi') 
    child.sendline('exit')    
