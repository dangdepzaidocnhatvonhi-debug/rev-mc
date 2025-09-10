from flask import Flask
import threading,requests,time,os
app = Flask(__name__)
url = "https://www.mcserverhost.com/api/servers/b864f512/subscription"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.mcserverhost.com",
    "Referer": "https://www.mcserverhost.com/servers/b864f512/dashboard",
    "Connection": "keep-alive",
}

cookies = {
    "_ga": "GA1.1.2020002270.1757239723",
    "twk_idm_key": "A56eQywm-8n9sz12S36GB",
    "__stripe_mid": "8b7e9386-7706-4a33-938f-b40f084ef728bc7af1",
    "mcserverhost": "770af250-b198-4318-95e4-7f836f82879b",
    "_ga_SRYKCFQGK0": "GS2.1.s1757478646$o10$g0$t1757478646$j60$l0$h0",
    "TawkConnectionTime": "0",
    "twk_uuid_674201982480f5b4f5a2f121": "%7B%22uuid%22%3A%221.2Bj8fhK2pexAmPAmzbhPLqbXlluONByRVihSTDc6qMZG0K9znke06TUMaMP5ipdJaoWxMO98Q9fHVUT6osCQuWJlOidqhcopgJVhkmyx0rZDOaNvRMpgrudvu54%22%2C%22version%22%3A3%2C%22domain%22%3A%22mcserverhost.com%22%2C%22ts%22%3A1757478649053%7D",
    "__stripe_sid": "094cd6ed-4075-497f-a37e-2d70de4cfe15cda1d9"
}
def background_task():
    while True:
        response = requests.post(url, headers=headers, cookies=cookies)
        if response.status_code == 200 :
            print("Đã renew server thành công vào lúc:", time.strftime('%H:%M:%S %Y-%m-%d'))
        time.sleep(3000)
@app.route("/")
def index():
    return "Bot is running!"

if __name__ == "__main__":

    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
