import requests

# ターゲットURL
url = "https://www.e-stat.go.jp"

try:
  # サイトにアクセスしてレスポンス
  response = requests.get(url)
  
  # 200以外はエラーを発生させる
  response.raise_for_status()
  
  # 成功したログ
  print(f"アクセス成功しました")
  print(f"ステータスコード: {response.status_code}")
except requests.exceptions.RequestException as e:
  # アクセス失敗のログ
  print(f"アクセスに失敗しました")
  print(f"エラー内容: {e}")

