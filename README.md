# Camera_slack
slackで指定のワードを指定したチャンネルに送ると写真を撮ってslackに上げます<br>
部室で誰が居るのか知りたいという要望で、サイトを頼りにUSB式のWEBカメラを用いて監視カメラのようなものを作成しました。<br>
使用機器<br>
・RaspberryPi 3B+<br>
・Webカメラ<br>

ディレクトリ構造<br>
slackbot         # プログラムをまとめるディレクトリ。名前はなんでも良い<br>
├─ run.py        # このプログラムを実行することで、ボットを起動する<br>
├─ slackbot_settings.py   # botに関する設定を書くファイル<br>
└─ plugins                # botの機能はこのディレクトリに追加する<br>
&nbsp;&nbsp;├─ __init__.py         # モジュールを示すためのファイル。空で良い<br>
&nbsp;&nbsp;└─ my_mention.py       # 機能を各ファイル。任意の名前で良い<br>

今回の制作を行うにあたり、以下のサイトを参考しました。この場を借りてお礼申し上げます。<br>
PythonのslackbotライブラリでSlackボットを作る<br>
URL: https://qiita.com/sukesuke/items/1ac92251def87357fdf6<br>
ラズパイでwebカメラ画像撮影 fswebcam<br>
URL: https://qiita.com/Bashi50/items/e408909225b283a2c8f7<br>
はじめてのRaspberry PIで監視カメラを作ってみた。<br>
URL: https://qiita.com/kinpira/items/bf1df2c1983ba79ba455<br>
