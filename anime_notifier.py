import requests
import json
import os
import smtplib
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -----------------------------------------
# Load local .env only for local testing
# GitHub Actions will provide secrets via environment variables
# -----------------------------------------
load_dotenv()

# Get environment variables (works for both local .env and GitHub Secrets)
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

NOTIFIED_FILE = "notified_titles.json"

# -----------------------------------------
# Safety check: alert if any variable is missing
# -----------------------------------------
if not EMAIL_ADDRESS or not EMAIL_PASSWORD or not EMAIL_RECEIVER:
    raise ValueError(
        "Email environment variables are not set properly. "
        "Check your .env for local testing or GitHub Secrets for Actions."
    )

# -----------------------------------------
# Load and save notified titles
# -----------------------------------------
def load_notified_titles():
    if os.path.exists(NOTIFIED_FILE):
        with open(NOTIFIED_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_notified_titles(data):
    with open(NOTIFIED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# -----------------------------------------
# Email sender
# -----------------------------------------
def send_email(subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain", "utf-8"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("📧 Email sent successfully")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# -----------------------------------------
# Anime update checker
# -----------------------------------------
def check_anime_update(keyword):
    url = f"https://anime1.me/?s={keyword.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.RequestException:
        return None, None

    if response.status_code != 200:
        return None, None

    soup = BeautifulSoup(response.text, "html.parser")
    latest_post = soup.select_one("h2.entry-title a")

    if latest_post:
        title = latest_post.text.strip()
        link = latest_post["href"]
        return title, link

    return None, None

# -----------------------------------------
# Load anime keywords
# -----------------------------------------
def load_anime_keywords(filename="anime_list.txt"):
    if not os.path.exists(filename):
        print(f"⚠️ Anime list file '{filename}' not found.")
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# -----------------------------------------
# Main checker
# -----------------------------------------
notified_titles = load_notified_titles()

def check_all_anime():
    anime_keywords = load_anime_keywords()
    if not anime_keywords:
        print("⚠️ No anime keywords to check.")
        return

    print("🔁 Checking anime updates...")
    for keyword in anime_keywords:
        title, link = check_anime_update(keyword)
        if not title:
            print(f"⚠️ No results found for '{keyword}'")
            continue

        if keyword not in notified_titles or notified_titles[keyword] != title:
            message = (
                f"New episode found!\n\n"
                f"Anime: {keyword}\n"
                f"Title: {title}\n"
                f"Link: {link}"
            )

            print(message)
            send_email(f"Anime Update: {keyword}", message)

            notified_titles[keyword] = title
            save_notified_titles(notified_titles)
        else:
            print(f"✅ No new episode for '{keyword}'")

# -----------------------------------------
# Run only if executed directly
# -----------------------------------------
if __name__ == "__main__":
    check_all_anime()
