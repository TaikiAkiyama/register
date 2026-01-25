# register
2025ロボットシステム学 課題2

![test](https://github.com/TaikiAkiyama/register/actions/workflows/test.yml/badge.svg)

ROS2で動作する、バーコードレジのシミュレーターシステムです。
## 必要なソフトウェア
- Python
- ROS 2 Jazzy 
## テスト環境
- Ubuntu 24.04 LTS
## ノード
`scanner`
- ユーザーからのキーボード入力を受けて、商品IDとしてトピックを送信(パブリッシュ)します。

`display`
- 商品IDのトピックを受信(サブスクライブ)します。
- データベースと照合し、該当する商品名と価格を画面に表示します。
- 登録されていないIDを受信した場合はエラーメッセージを表示します。
## トピック
`/scanned_id`(`std_msgs/msg/String`)
- 商品IDを文字列で送受信するためのトピックです。
## インストール
launchファイルを使用する場合は`xterm`をインストールして下さい。
```
$ sudo apt install xterm
```

## 実行方法 
launchファイルを使用してシステムを起動します。コマンドを実行すると、`xterm`が立ち上がります。
```
$ ros2 launch register scan_display.launch.py
```
`xterm`ウィンドウに数値を入力してEnterキーを押すとlaunchコマンドを実行した元の端末で結果が表示されます。
## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- © 2025 Taiki Akiyama
