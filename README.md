## Google Calendar を Raspberry Pi Pico W と e-paer で表示する（2.66 インチ用の e-paper 用）

https://github.com/kenji0302/e-paper-google-calendar-213 を元に開発しているため基本的に同じ。

画面表示には https://github.com/kenji0302/pico-epaper-2.66-b を利用。

ただ、実運用しているのは 2.66 インチなので機能追加はこちらが早いかも。

### 設定箇所

1. secret.samply.py を自分の環境に合わせて変更 secret.py にリネームして保存する。
2. index.php を自分の環境に併せて変更し実行。取得したリフレッシュトークンをローカルネットワーク設置。