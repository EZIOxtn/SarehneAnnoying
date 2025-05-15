import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import math
import random
import threading
############################
UseProxies = False    #####   Set this to true if you wanna use proxies
##################################
name = input("the profile link  (look like this 'sarhne.sarahah.pro/USERNAME')  :")
def encrypt_message(message: str, viewport_content: str) -> str:
    
    key_iv_raw = viewport_content[:16].encode('utf-8')
    
    cipher = AES.new(key_iv_raw, AES.MODE_CBC, iv=key_iv_raw)
    encrypted = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    
    
    return base64.b64encode(encrypted).decode('utf-8')

def randomString():
    st = "azer ty uiopqs  dfghjklmwxcvbn,;:ù!^$"
    initializer = ""
    for i in range (20):
        initializer += st[random.randint(0,len(st)-1)]
    return initializer


def serialize_txt():
    proxies = []

    try:
        with open("http_proxiess.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    proxies.append(line) 
    except Exception as e:
        print("Error reading proxy file:", str(e))

    return proxies
def get_random_proxy():
    proxy_list = serialize_txt()
    if not proxy_list:
        return None

    chosen = random.choice(proxy_list)
    return {
        "http": f"http://{chosen}",
        "https": f"http://{chosen}"
    }

def repmain():


    viewport = 'width=device-width, initial-scale=1'  
    message = str(int(math.floor(random.random())))    


    session = requests.Session()
    p = get_random_proxy()
    prx = p if p != None  else exit(1)
    try:






        session.headers.update({
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'origin': 'https://sarhne.sarahah.pro',
    'referer': 'https://sarhne.sarahah.pro/',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="136", "Brave";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
})


        options_headers_t = {
    'accept': '*/*',
    'access-control-request-headers': 'content-type',
    'access-control-request-method': 'POST',
    'sec-fetch-dest': 'empty',
}
        resp = session.options('https://api.sarhne.com/t', headers=options_headers_t, proxies = prx if UseProxies else None, timeout = 20)
       
        print(f"\n[Step 1] OPTIONS /t -> Status: {resp.status_code}")


        post_headers_t = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en;q=0.7',
    'content-type': 'application/json',
    'sec-fetch-dest': 'empty'
}
        payload_t = {
    'k': 'C17MajwdyCzFpgsIgdNFgw=='
}
        resp = session.post('https://api.sarhne.com/t', headers=post_headers_t, json=payload_t, proxies = prx if UseProxies else None, timeout = 20)
        print(f"\n[Step 2] POST /t -> Status: {resp.status_code}")
    #print(resp.json())
        needit = resp.json()


        options_headers_ssend =    {
    'accept': '*/*',
    'access-control-request-headers': 'content-type',
    'access-control-request-method': 'POST',
    'sec-fetch-dest': 'empty',
}
        resp = session.options('https://www.sarhne.com/ajax/messages/ssend.html', headers=options_headers_ssend, proxies = prx if UseProxies else None, timeout = 20)
        print(f"\n[Step 3] OPTIONS /ssend.html -> Status: {resp.status_code}")


        post_headers_ssend = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en;q=0.7',
    'content-type': 'application/json',
    'sec-fetch-dest': 'empty'
}
        RandomTextToSendToTheSarehneApiToMakeThemFeelEeeeh = randomString()
        payload_ssend = {
    "_k": encrypt_message(needit["k"], viewport),
    "msg": RandomTextToSendToTheSarehneApiToMakeThemFeelEeeeh,
    "is_secret": "on",
    "i": "null",
    "trc": "c54a0fa98683f9bf",
    "_u": "mmvKm2xC/o7zMKADF8ZCxg==",
    "_i": "null"
}
        resp = session.post('https://www.sarhne.com/ajax/messages/ssend.html', headers=post_headers_ssend, json=payload_ssend, proxies = prx if UseProxies else None, timeout = 20)
        print(f"\n[Step 4] POST /ssend.html -> Status: {resp.status_code}")
    #print(resp.text)
        print("success" if "succ        Text sent :" + RandomTextToSendToTheSarehneApiToMakeThemFeelEeeeh in resp.text else "error max api tries reached")

        url = 'https://sarhne.sarahah.pro/amroahmadali'

        headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-GB,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://sarhne.sarahah.pro',
    'priority': 'u=0, i',
    'referer': 'https://sarhne.sarahah.pro/amroahmadali',
    'sec-ch-ua': '"Chromium";v="136", "Brave";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}


        cookies = {
    'tr': 'c54a0fa98683f9bf',
    'trc': 'c54a0fa98683f9bf'
}


        data = {
    'processing': ''
}

        response = session.post(url, headers=headers, cookies=cookies, data=data, proxies = prx if UseProxies else None, timeout = 20)

    #print(f"Status Code processing: {response.status_code}")



        post_headers_push = {
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-fetch-dest': 'empty'
}
        data_push = {
    'link': name.split("/")[1]
}
        resp = session.post('https://www.sarhne.com/ajax/messages/push.html', headers=post_headers_push, data=data_push, proxies = prx if UseProxies else None, timeout = 20)
        print(f"\n[Step 5] POST /push.html -> Status: {resp.status_code}")
    #print(resp.text)
    except Exception as e:
        print("errors" + str(e))
def main():
    for i in range (20):
        repmain()
main()
#t = threading.Thread(target= main).start()
#t2 = threading.Thread(target=main).start()

    