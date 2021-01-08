# 課題2
## 概要
第10回の授業で作成したtwice.pyに手を加え、2倍になった数字と3倍になった数字が交互に表示されるようにしました。

## 動作環境
- Ubuntu 20.04 LTS
- ROS "focal"
## 動画リンク
- https://youtu.be/0hDLD_rjXrQ

## インストール方法
以下のコマンドを実行して、パッケージをクローンしてください。
~~~
cd ~/catkin_ws/src
git clone https://github.com/rensho215/mypkg.git
~~~

次に、catkin_wsの下でcatkin_makeをしてビルドしてください。
~~~
cd ~/catkin_ws
catkin_make
source ~/.bashrc
~~~

## 使用方法
~~~ 
roscore & 
~~~
を実行してroscoreをバックグラウンドで起動してください。
そして、新たなターミナルを開きcount.pyを起動してください。
~~~
rosrun mypkg count.py
~~~
次に、もう一つターミナルを開きtwo-three.pyを起動してください。
~~~
rosrun mypkg two-three.py
~~~
この状態で
~~~
rostopic echo /two-three
~~~
を実行することで2倍された数字と3倍された数字が交互に表示されます。

## ライセンス
- BSD 3-Clause License
