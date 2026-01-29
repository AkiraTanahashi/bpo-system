import requests
import time
import sys

# あなたのWordPressのAPI URL
url = "https://colorfulum.com/ikigai-project/wp-json/wp/v2/posts?per_page=3"

print("="*40)
print("📡 WordPress接続診断ツール起動")
print(f"ターゲット: {url}")
print("="*40)

try:
    print("接続を試みています...（最大10秒待ちます）")
    start_time = time.time()
    
    # ユーザーエージェント（身分証）を設定して、ブラウザのふりをします
    # ※サーバーによってはPythonからのアクセスを拒否する場合があるため
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    end_time = time.time()
    
    duration = round(end_time - start_time, 2)
    
    print(f"\n⏱️ 応答時間: {duration}秒")
    print(f"📊 ステータスコード: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ 【成功】 {len(data)} 件の記事データが見つかりました！")
        print("-" * 20)
        for post in data:
            print(f"・{post['title']['rendered']}")
        print("-" * 20)
        print("結論: 通信は正常です。Django側の設定を見直しましょう。")
    elif response.status_code == 403:
        print("🚫 【拒否】 サーバーからアクセスを拒否されました (403 Forbidden)。")
        print("原因: WAF（セキュリティ）やレンタルサーバーの設定で、海外IPやBotをブロックしている可能性があります。")
    elif response.status_code == 404:
        print("❓ 【不明】 URLが間違っているか、REST APIが無効化されています (404 Not Found)。")
    else:
        print(f"⚠️ 【その他】 想定外の応答です: {response.status_code}")

except requests.exceptions.Timeout:
    print("\n⏰ 【タイムアウト】 10秒以内に応答がありませんでした。")
    print("原因: サーバーがCloud Shellからの通信を無視しているか、非常に重いです。")
except requests.exceptions.ConnectionError:
    print("\n🔌 【接続エラー】 サーバーが見つからないか、DNSの問題です。")
except Exception as e:
    print(f"\n❌ 【エラー】 詳細: {e}")

print("="*40)