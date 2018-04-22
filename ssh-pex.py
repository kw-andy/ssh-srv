from pexpect import pxssh
#import pdb
conn = pxssh.pxssh()
if not conn.login ('192.168.1.10', 'pi', 'raspberry'):
    print("SSH session failed on login.")
    print(str(conn))
else:
    print("SSH session login successful")
    conn.sendline('\ls -l')
    conn.prompt()
    abc = conn.before
    print(abc.decode())
 #abc = str(conn.sendline('\ls -l'))
    #print(abc.encode('utf-8').decode('utf-8'))
    #print(abc.decode('utf-8'))
#    pipe_data = conn.sendline('LC_ALL=C ls -l');print(pipe_data.decode('utf-8'))
#    print(pipe_data)
#   print(pdb.pm('pipe_data()')) 
#    conn.sendline('LC_ALL=C ls -l')
#    pipe_data = conn.read()
#    print(pipe_data.decode('utf-8'))
    #conn.prompt()         # match the prompt
    #print(conn.before)     # print everything before the prompt.
    conn.logout()
    conn.close()
