import requests
from lib.commands.decrypt import decrypt

URL = "https://login.index-if.jp//Auth/gatein.php"
BODY = '{"market":1,"cl_ver":"6.3.0"}'

def download():
    data = requests.post(URL, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }, data=BODY)

    resp = data.json()

    print(resp)

    if (resp['res_code'] == 0):
        res_url = resp['resource_url']
        patch_ver = resp['patch_version']

        data = requests.get(f'{res_url}ios/{patch_ver}')

        blob = data.content
        decrypt(blob, "test.unity3d", "./bin/keys-2.bin")

    else:
        Exception("res_code is not 0")


if __name__ == "__main__":
    download()