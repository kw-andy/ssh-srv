from pexpect import pxssh
conn = pxssh.pxssh()
#changed the Ip address
if not conn.login ('192.18.1.11', 'pi', 'raspberry'):
    print("SSH session failed on login.")
    print(str(conn))
else:
    print("SSH session login successful")
    conn.sendline('\ls -l')
    conn.prompt()         # match the prompt
    print(conn.before)     # print everything before the prompt.
    conn.logout()
    conn.close()
