
from os import system
import subprocess
vlocal = "v1.4.0-msft-1"
vremote = "v1.4.2-rc.1"

if len(vlocal.split('-')) > 2 and vlocal.split('-')[-2] == 'msft':
    vlocal = '-'.join(vlocal.split('-')[:-2])

print(vlocal)

if vlocal != vremote:
    command = f"git pull upstream {vremote}"
    exitcode = subprocess.call(command,shell=True)
    if exitcode != 0:
        system.exit(1)