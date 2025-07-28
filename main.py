import requests
from time import sleep

# بيانات تويتر
headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
}
username = "MohamK260283"

# بيانات تليجرام
bot_token = "8464662513:AAEvuovMD7n4BhtFQhCLjIoWz8zcNu4yT6k"
chat_id = "-1001977172268"
alert_link = "https://candidature.1337.ma/users/sign_in"

# رابط API تويتر
url = f"https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}&count=1"

# استعلام لتغريدة واحدة
try:
    print("Checking tweets...")
    response = requests.get(url, headers=headers)
    tweet = response.json()[0]['text'].lower()

    print(f"Latest tweet: {tweet}")

    if any(keyword in tweet for keyword in ["piscine", "pool", "place"]):
        message = f"🔥⚡🔥 P001 I5 L04DIN9 !!! {alert_link} 🔥⚡🔥"
        requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}")
        print("Alert sent!")
    else:
        print("No relevant keywords found.")
except Exception as e:
    print("Error:", e)
