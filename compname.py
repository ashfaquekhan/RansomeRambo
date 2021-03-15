import os
from uuid import getnode as get_mac
mac = get_mac()
pc=os.getenv('COMPUTERNAME')
print(pc)
print(mac)