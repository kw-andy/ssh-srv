from pexpect import pxssh
import getpass
try:
    ssh_options = {'IdentityAgent': ''}
    s = pxssh.pxssh()
    hostname = '174.138.12.81'
    username = 'andykw'
    #ssh-key = '/home/miaou/priv_keys'
    s.login(hostname, username)
    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before.decode())        # print everything before the prompt.
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
