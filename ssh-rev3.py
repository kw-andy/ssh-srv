from pexpect import pxssh
#import getpass

# conn_up is a function for connecting and doing an uptime.

def conn_up():
    try:
        s = pxssh.pxssh()
        hostname = '174.138.12.81'
        username = 'andykw'
        s.login(hostname, username,ssh_key='/home/miaou/priv_keys')
        s.sendline('uptime')   # run a command
        s.prompt()             # match the prompt
        print(s.before.decode())        # print everything before the prompt.
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

if __name__ == '__main__':
    conn_up()

