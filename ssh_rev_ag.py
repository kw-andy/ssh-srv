import pexpect
import os

os.system('ssh-agent -s; ssh-add /home/miaou/priv_keys; ssh-agent bash')
#exec ssh-agent bash
#ssh-add /home/miaou/priv_keys
#child = pexpect.spawn('eval `ssh-agent -s`')
child = pexpect.spawn('ftp test.rebex.net')
#child = pexpect.spawn('exec ssh-agent bash')
#child.expect('toto :')
#child.sendline('ssh-add /home/miaou/priv_keys')

child.expect('Name .*: ')
child.sendline('demo')
child.expect('Password:')
child.sendline('password')
child.expect('ftp> ')
child.sendline('get readme.txt')
child.expect('ftp> ')
child.sendline('bye')
