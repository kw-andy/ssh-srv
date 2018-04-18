from pexpect import pxssh
conn = pxssh.pxssh()
if not conn.login ('192.168.1.30', 'pi', 'raspberry'):
    print("SSH session failed on login.")
    print(str(conn))
else:
    print("SSH session login successful")
    conn.sendline('\ls -l')
    conn.prompt()         # match the prompt
    print(conn.before)     # print everything before the prompt.
    conn.logout()
    conn.close()
