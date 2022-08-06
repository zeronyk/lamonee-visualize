import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://app.lamonee.de/',
    'Origin': 'https://app.lamonee.de',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://api.lamonee.de/sanctum/csrf-cookie', headers=headers)


for c in response.cookies:
    print(c.name, c.value)

xsrf = response.cookies['XSRF-TOKEN']

print(xsrf)

print("kkkkkkkkkkkkk")

lamonee_api_session = response.cookies['lamonee_api_session']

print(lamonee_api_session)



cookies = {
    'XSRF-TOKEN': 'eyJpdiI6ImJJS3ZBOHh6bDlqd3FtUi9vVndCWGc9PSIsInZhbHVlIjoiTURCV1Z0dWJ0T2pXb3h5NjlOSVk1bWwzRDJZNlFvM25HQ2Q0U2hYaktBTTErNDR1V2x3ejdBVnJLV2VBaHZDK2tiZ1lnQjdldlpqMTdCOExMSjdieVlZazFFV0ZMRHF6eVBPR3lCSjNEMmhlS3dwZzhkaHBFMG92UjVXTjVZR1MiLCJtYWMiOiJkMWJkNWUzZGY5NTYwYjVhYTczM2U0ZDJiNjA1MmJhNzBmMGJjZGQ3NTczNTVmZjE3MmI1NjA0MmIxMjRhNTdiIiwidGFnIjoiIn0%3D',
    'lamonee_api_session': 'eyJpdiI6IkJ5TlpzeFhDY1NiZEVnNTNjeXBzaWc9PSIsInZhbHVlIjoieEZIMmwzMSt4SytmRGhRaVp3bi9ySkZuejdqc005NHVZVW1mczdna0pTZVNZdHBSMk9mZmRiKzRKN3VJSEhQK2szSTRBRGprMHlsRUNqZ1ltTDlLcUwrdTFJMm1aQ1dJSktUWVBVbDNOR053TjFzdSs4aEFhb0w1VGNzSWh0dzYiLCJtYWMiOiI2ZDNjMDBiNzg0MWZlYzAyMmU3MjkzMmI2YjQwYTdjNDkzMDY4NTA5MzJhZmU4YjA2ZTc5MDA4MDAyYjMxMWQ1IiwidGFnIjoiIn0%3D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6ImJJS3ZBOHh6bDlqd3FtUi9vVndCWGc9PSIsInZhbHVlIjoiTURCV1Z0dWJ0T2pXb3h5NjlOSVk1bWwzRDJZNlFvM25HQ2Q0U2hYaktBTTErNDR1V2x3ejdBVnJLV2VBaHZDK2tiZ1lnQjdldlpqMTdCOExMSjdieVlZazFFV0ZMRHF6eVBPR3lCSjNEMmhlS3dwZzhkaHBFMG92UjVXTjVZR1MiLCJtYWMiOiJkMWJkNWUzZGY5NTYwYjVhYTczM2U0ZDJiNjA1MmJhNzBmMGJjZGQ3NTczNTVmZjE3MmI1NjA0MmIxMjRhNTdiIiwidGFnIjoiIn0=',
    'Origin': 'https://app.lamonee.de',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Referer': 'https://app.lamonee.de/',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6ImJJS3ZBOHh6bDlqd3FtUi9vVndCWGc9PSIsInZhbHVlIjoiTURCV1Z0dWJ0T2pXb3h5NjlOSVk1bWwzRDJZNlFvM25HQ2Q0U2hYaktBTTErNDR1V2x3ejdBVnJLV2VBaHZDK2tiZ1lnQjdldlpqMTdCOExMSjdieVlZazFFV0ZMRHF6eVBPR3lCSjNEMmhlS3dwZzhkaHBFMG92UjVXTjVZR1MiLCJtYWMiOiJkMWJkNWUzZGY5NTYwYjVhYTczM2U0ZDJiNjA1MmJhNzBmMGJjZGQ3NTczNTVmZjE3MmI1NjA0MmIxMjRhNTdiIiwidGFnIjoiIn0%3D; lamonee_api_session=eyJpdiI6IkJ5TlpzeFhDY1NiZEVnNTNjeXBzaWc9PSIsInZhbHVlIjoieEZIMmwzMSt4SytmRGhRaVp3bi9ySkZuejdqc005NHVZVW1mczdna0pTZVNZdHBSMk9mZmRiKzRKN3VJSEhQK2szSTRBRGprMHlsRUNqZ1ltTDlLcUwrdTFJMm1aQ1dJSktUWVBVbDNOR053TjFzdSs4aEFhb0w1VGNzSWh0dzYiLCJtYWMiOiI2ZDNjMDBiNzg0MWZlYzAyMmU3MjkzMmI2YjQwYTdjNDkzMDY4NTA5MzJhZmU4YjA2ZTc5MDA4MDAyYjMxMWQ1IiwidGFnIjoiIn0%3D',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'email': 'mxxxxxxxxxxxx',
    'password': 'xxxxxxxxxxxx',
}

response = requests.post('https://api.lamonee.de/login', cookies=cookies, headers=headers, json=json_data)