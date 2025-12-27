# register
2025ロボットシステム学 課題2

![test](https://github.com/TaikiAkiyama/register/actions/eorkflows/test.yml/badge.svg)

ROS2で動作する、バーコードレジのシミュレーターシステムです。
入力されたIDに基づいて商品情報を照会し、結果を表示します。
## 必要なソフトウェア
- Python
- ROS 2 Humble 
## テスト環境
- Ubuntu 24.04 LTS
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
端末1: スキャン側
```
$ ros2 run register scanner
1
```
端末2: 表示側
```
$ ros2 run register display
Apple 150
```

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- © 2025 Taiki Akiyama
