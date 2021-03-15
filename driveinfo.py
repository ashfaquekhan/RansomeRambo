import os
print (os.popen("fsutil fsinfo drives").readlines())