"""
To run this program, the file ``ssh_host_key`` must exist with an SSH
private key in it to use as a server host key. An SSH host certificate
can optionally be provided in the file ``ssh_host_key-cert.pub``.
12/06/18:
creating a ssh server with asyncssh
"""
import asyncio, asyncssh, crypt, sys

passwords = {'guest': '',                 # guest account with no password
             'user123': 'qVb54q5rAVoEQ'   # crypt password for 'uuu'
            }


def handle_client(process):
    process.stdout.write('Welcome to my SSH server, %s!\n' %
                         process.channel.get_extra_info('username'))
    process.exit(0)


async def run_client():
    async with asyncssh.connect('174.138.12.81', username='andykw',client_keys=['resources/priv_keys']) as conn:
        result = await conn.run('ls .', check=True)
        print(result.stdout, end='')


class MySSHServer(asyncssh.SSHServer):
    def connection_made(self, conn):
        print('SSH connection received from %s.' %
                  conn.get_extra_info('peername')[0])

    def connection_lost(self, exc):
        if exc:
            print('SSH connection error: ' + str(exc), file=sys.stderr)
        else:
            print('SSH connection closed.')

    def begin_auth(self, username):
        # If the user's password is the empty string, no auth is required
        return passwords.get(username) != ''

    def password_auth_supported(self):
        return True

    def validate_password(self, username, password):
        pw = passwords.get(username, '*')
        return crypt.crypt(password, pw) == pw
'''
    async def run_client(self):
        async with asyncssh.connect('174.138.12.81', username='andykw', client_keys=['/home/miaou/priv_keys']) as conn:
            result = await conn.run('ls .', check=True)
            print(result.stdout, end='')

'''
async def start_server():
    await asyncssh.create_server(MySSHServer, '', 8022,
                                 server_host_keys=['resources/priv_keys'],
                                 process_factory=handle_client)

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(start_server())
except (OSError, asyncssh.Error) as exc:
    sys.exit('Error starting server: ' + str(exc))

loop.run_forever()
