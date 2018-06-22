from pexpect import pxssh
import pexpect
#import getpass

# conn_up is a function for connecting to a remote server and doing an uptime.

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

# os.system('ssh-agent -s; ssh-add /home/miaou/priv_keys; ssh-agent bash')

# conn_wr is a function for connecting to a remote server and create a file 123toto.txt
# on the remote server
# this method is for programs like sftp or ssh, which needs some human interactions

def conn_wr():
    child = pexpect.spawn('ssh pi@192.168.1.32')
    child.expect('password:')
    child.sendline('XXX')
    child.expect('pi')
    child.sendline('touch 123toto.txt')
    child.expect('pi') 
    child.sendline('exit')    
        
        

if __name__ == '__main__':
    conn_up()
    conn_wr()

