import requests
import time
import os
from dotenv import load_dotenv
from posts import posts  # ← imports post data

load_dotenv()

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")

def post_to_telegram(image_url, caption):
    telegram_api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'photo': image_url,
        'caption': caption
    }
    r = requests.post(telegram_api_url, data=payload)
    if r.status_code == 200:
        print("✅ Telegram post successful")
    else:
        print(f"❌ Telegram error: {r.text}")

def post_to_facebook(image_url, caption):
    fb_api_url = f"https://graph.facebook.com/{FACEBOOK_PAGE_ID}/photos"
    payload = {
        'url': image_url,
        'caption': caption,
        'access_token': FACEBOOK_ACCESS_TOKEN
    }
    r = requests.post(fb_api_url, data=payload)
    if r.status_code == 200:
        print("✅ Facebook post successful")
    else:
        print(f"❌ Facebook error: {r.text}")

# Cycle through posts
for index, post in enumerate(posts):
    print(f"\n🚀 Posting {index + 1}/{len(posts)}")
    post_to_telegram(post["image_url"], post["caption"])
    post_to_facebook(post["image_url"], post["caption"])
    
    if index < len(posts) - 1:
        print("⏳ Waiting 60 seconds before next post...")
        time.sleep(60)  # Change this to 86400 for 24 hours delay
