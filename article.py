import random

#記事の辞書登録。美しくない。
articles = [
    {"ABST":"お金をかけずにプログラミングを学ぶ方法をまとめた記事。",
     "URL":"https://t-chemkunfu-y.com/program/lowp-and-highq-method/", 
     "HASH_TAG":"#駆け出しエンジニアとつながりたい"},
    {"ABST":"kaggle始めるなら、ここら辺が役立つよなって本を集めた記事。",
     "URL":"https://t-chemkunfu-y.com/data-science/kaggle_book/", 
     "HASH_TAG":"#kaggle本"},
    {"ABST":"個人的にオススメなデータサイエンス数学やり直し本をまとめた記事。",
     "URL":"https://t-chemkunfu-y.com/data-science/math-book-for-ds/",
     "HASH_TAG":"#データサイエンスのための数学"},
    {"ABST":"GCEとVScodeのつなぎ方。備忘録の意味も込めてまとめた記事。", 
     "URL":"https://t-chemkunfu-y.com/program/gce-vscode/", 
     "HASH_TAG":"#GCE #VScode"},
    {"ABST":"コンテナ技術を世界一わかりやすく解説した記事。",
     "URL":"https://t-chemkunfu-y.com/program/docker-container/",
     "HASH_TAG":"#Docker"},
    {"ABST":"時間が無くても独学・短期間でExcelVBAを身に着ける方法論をまとめた記事",
     "URL":"https://t-chemkunfu-y.com/excel/vba-dokugaku/",
     "HASH_TAG":"#ExcelVBA"},
    {"ABST":"コードの実行時間を記録できるloggerの使い方をまとめた記事。",
     "URL":"https://t-chemkunfu-y.com/program/use-logging/",
     "HASH_TAG":"#python"},
    {"ABST":"Twitter API活用のためのPythonライブラリtweepyを使用するまでの流れを解説。",
     "URL":"https://t-chemkunfu-y.com/program/control-twitter-by-python/",
     "HASH_TAG":"#python"},
    {"ABST":"スクリプトを定時実行するために必要なcronの設定方法をまとめた記事。",
     "URL":"https://t-chemkunfu-y.com/program/cron-auto-script/",
     "HASH_TAG":"#Linux"},
    {"ABST":"GCP登録→仮想サーバー立ち上げ→ローカルマシンからのSSH接続をまとめた記事。",
     "URL":"https://t-chemkunfu-y.com/program/vm-on-local/",
     "HASH_TAG":"#Google Cloud Platform"},
    {"ABST":"仮想サーバーとVSCodeをSSH接続して、ローカルから編集する方法をまとめた記事。",
     "URL":"https://t-chemkunfu-y.com/program/gce-vscode/",
     "HASH_TAG":"#Visual Studio Code"},
    {"ABST":"仮想サーバー、TwitterAPI、cron設定を用いた過去記事ツイートbotの作り方を解説した記事。",
     "URL":"https://t-chemkunfu-y.com/program/article-tweet-bot/",
     "HASH_TAG":"#python自動化"}    
]


#数値をランダムで取得。indexに格納。
index = random.randint(0,11)


#取得したindexを用いて、リストの中から辞書を取得。
pick_up_article = articles[index]
