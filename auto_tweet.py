import tweepy
from credential import CONSUMER_KEY ,CONSUMER_SECRET ,ACCESS_TOKEN ,ACCESS_SECRET

#API使用認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#Twitterアカウント認証
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#APIインスタンス生成
api = tweepy.API(auth)


#article.pyから、要約・URL・ハッシュタグ、の入った辞書（pick_up_article）をインポート
from article import pick_up_article

#ピックアップしてきた記事（辞書）を変数に格納
article = pick_up_article

#辞書キーを指定して、値を取得
abst = article["ABST"]
url = article["URL"]
hashtag = article["HASH_TAG"]

#ツイート内容をtweet変数に格納。\nは改行を行う。
tweet = f"{abst}\n{url}\n{hashtag}\n#過去記事PickUp"

#ツイート
api.update_status(tweet)

