# register
2025ロボットシステム学 課題2

![test](https://github.com/TaikiAkiyama/register/actions/workflows/test.yml/badge.svg)

ROS2で動作する、バーコードレジのシミュレーターシステムです。
入力されたIDに基づいて商品情報を照会し、結果を表示します。
## 必要なソフトウェア
- Python
- ROS 2 Humble 
## テスト環境
- Ubuntu 24.04 LTS
## ノード
`scanner.py`
- ユーザーからのキーボード入力を受けて、商品IDとしてトピックを送信(パブリッシュ)します。

`display.py`
- 商品IDのトピックを受信(サブスクライブ)します。
- データベースと照合し、該当する商品名と価格を画面に表示します。
- 登録されていないIDを受信した場合はエラーメッセージを表示します。
## トピック
`/scanned_id`(型: `std_msgs/msg/String`)
- 商品IDを文字列で送受信するためのトピックです。
- `scanner.py`から`display.py`へ送信されます。
## インストール
ROS 2のワークスペースに移動してクローンし、ビルドします。
```
$ cd ~/ros2_ws/src
$ git clone https://github.com/TaikiAkiyama/register.git
$ cd ~/ros2_ws
$ colcon build
$ source ~/.bashrc
```
launchファイルを使用する場合は`xterm`をインストールして下さい。
```
$ sudo apt install xterm
```

## 使い方
端末を2つ開いて実行します。
- 端末1: スキャン側
```
$ ros2 run register scanner
1
```
- 端末2: 表示側
```
$ ros2 run register display
Apple 150
```

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- © 2025 Taiki Akiyama
