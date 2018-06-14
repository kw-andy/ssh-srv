from pexpect import pxssh
#import pdb
conn = pxssh.pxssh()
if not conn.login ('192.168.79.165', 'miaou', 'Zaerty01'):
    print("SSH session failed on login.")
    print(str(conn))
else:
    print("SSH session login successful")
    conn.sendline('ls -l')
    #the prompt helps to display the command line
    conn.prompt()
    #putting the conn.before in a variable
    conn.before.decode()
    conn.logout()
    conn.close()
