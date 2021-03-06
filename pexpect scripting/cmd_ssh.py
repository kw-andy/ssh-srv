"""
# 17/06/18
# this script is used as a test to connect and run command lines 
# a remote server
# this is a first attempt with pexpect
"""

from pexpect import pxssh
import getpass
try:
    s = pxssh.pxssh()
    hostname = '192.168.43.163'
    username = 'miaou'
    password = 'aaa'
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
    # adding a test line for using python within 
    # pexpect library
    s.sendline("python3 -c 'print(5+5)'")
    s.prompt()     
    print(s.before.decode())
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
