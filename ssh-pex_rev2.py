from pexpect import pxssh
import getpass
try:
    s = pxssh.pxssh()
    hostname = '192.168.79.165'
    username = 'miaou'
    password = 'Zaerty01'
    s.login(hostname, username, password)
    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before.decode())        # print everything before the prompt.
    s.sendline('ls -l')
    s.prompt()
    print(s.before.decode())
    s.sendline('df')
    s.prompt()
    print(s.before.decode())
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
