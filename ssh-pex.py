from pexpect import pxssh
conn = pxssh.pxssh()
if not conn.login ('174.138.12.81', 'myusername', 'mypassword'):
    print("SSH session failed on login.")
    print(str(conn))
else:
    print("SSH session login successful")
    conn.sendline('ls -l')
    conn.prompt()         # match the prompt
    print(conn.before)     # print everything before the prompt.
    conn.logout()
    conn.close()
