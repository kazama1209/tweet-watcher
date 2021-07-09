import tweepy
import textwrap
import os
from dotenv import load_dotenv
load_dotenv()

# 反応したいキーワード（複数指定可）
keywords = [
  'python',
  'docker',
  'twitter',
  'api'
]

class StreamListener(tweepy.StreamListener):
	# 対象のユーザーが新規にツイートをするたびにこの関数が走る
	def on_status(self, status):
		tweet_type = self.check_tweet_type(status)
		
		# 通常のツイート以外（リツイートやリプライ）だった場合はここで終了
		if tweet_type != 'normal_tweet': return
		
		# ツイートの本文を取得（大文字/小文字の区別が面倒なのでとりあえず小文字に変換）
		text = status.text.lower()

		# ツイートの本文にキーワードが含まれているかどうかチェック
		if any([keyword in text for keyword in keywords]):
			# 以下に行いたい処理を記述
			# 今回はサンプルなのでツイートの本文を出力してみる
			heredoc = textwrap.dedent('''
				-------------------------
				{user_name} tweeted!
				{text}
			''').format(user_name = status.user.name, text = status.text).strip()
			
			print(heredoc)

		else:
			# キーワードが含まれていなかった場合は何もしない
			pass

	# ツイートの種類をチェック（リツイート or リプライ or 通常のツイート）
	def check_tweet_type(self, status):
		# JSON内のキーに「retweeted_status」があればリツイート
		if 'retweeted_status' in status._json.keys():
			return 'retweet'
		
		# 「in_reply_to_user_id」がNoneでなかった場合はリプライ
		elif status.in_reply_to_user_id != None:
			return 'reply'

		# それ以外は通常のツイート
		else:
			return 'normal_tweet'

# 各認証情報を準備
api_key = os.getenv('TWITTER_API_KEY')
api_secret = os.getenv('TWITTER_API_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# API認証
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# リスナーを作成
stream_listener = StreamListener()
stream = tweepy.Stream(auth = auth, listener = stream_listener)

# 監視対象のユーザーID（https://idtwi.com/ ←で調べられる）
twitter_user_id = os.getenv('TWITTER_USER_ID')

# 監視スタート
print('Start watching tweets')

# ユーザーIDは配列で複数渡す事が可能
# もし別のスレッドで非同期処理を行わせたい場合はfilterの引数に「is_async = True」を渡す
stream.filter(follow=[twitter_user_id])
