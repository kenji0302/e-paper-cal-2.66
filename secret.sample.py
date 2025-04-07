import urequests

WIFI_SSID = 'Wifiのアクセスポイント'
WIFI_PASSWORD = 'Wifiのパスワード'
GOOGLE_CLIENT_ID = "クライアントID"
GOOGLE_CLIENT_SECRET = "クライアントシークレット"
GOOGLE_CALENDAR_ID = "カレンダーID"

def get_google_refresh_token():

    url = 'https://192.168.0.1/cal2.66/token.dat'   # リフレッシュトークンをローカルネットワークから取得できるようにした場合
    response = urequests.get(url)
    token = response.text
    response.close()

    return token