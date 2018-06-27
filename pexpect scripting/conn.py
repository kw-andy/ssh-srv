"""
27/06/18:

The aim of the code is to generalize the methods written here, to build a library.
For info, you will need to set a public key on your remote server and use your private
key, to connect and run the methods below.

"""

from pexpect import pxssh
import pexpect

# uptime_conn is a function that does a connect to remote server and run an uptime

def uptime_conn(ip_addr,username,priv_keys):
    try:
        s = pxssh.pxssh()
        s.login(ip_addr, username,ssh_key=priv_keys)
        s.sendline('uptime')   # run a command
        s.prompt()             # match the prompt
        print(s.before.decode())        # print everything before the prompt.
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)


# cre_file_conn is is a function that connects to a remote server and
# create a file on the remote server


def cre_file_conn(ip_addr,username,priv_keys):
    try:
        cmd = ("ssh -i {} {}{}{}").format(priv_keys,username,"@",ip_addr)
        child = pexpect.spawn(cmd)
        child.expect(username)
        child.sendline('touch 123toto.txt')
        child.expect(username) 
        child.sendline('exit')
    except Exception as e:
        print(str(e))       
  
if __name__ == '__main__':
    uptime_conn()
    cre_file_conn()        
        
