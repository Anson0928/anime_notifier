# 📺 Anime1 自動追番通知器 | Auto Anime Episode Notifier

用 Python 寫的小型 Side Project，能自動追蹤 [anime1.me](https://anime1.me) 上的動畫更新，  
一有新的一集，就會透過 Email 自動通知你 📧

A small Python side project that automatically tracks anime updates on [anime1.me].  
Whenever a new episode is released, it sends you an Email instantly.

---

## 🚀 功能 Features

- ✅ 自動從 anime1 搜尋你喜歡的動畫  
  
- ✅ 發現新的一集就自動發 Email 通知（支援 Gmail 或其他 SMTP 信箱）  
  
- ✅ 支援多部動畫同時追蹤  
  
- ✅ 記得已經通知過的集數（不會重複寄信）  
  
- ✅ 可搭配排程自動執行（如 GitHub Actions 或 VPS）  
  
- ✅ 關機或電腦不運作時，也能自動通知  
  
---

- ✅ Automatically search for your favorite anime from anime1

- ✅ Instantly send an Email when a new episode is found

- ✅ Track multiple anime at the same time

- ✅ Remembers what episodes have already been notified (avoids duplicates)

- ✅ Can be scheduled to run automatically (e.g., via GitHub Actions or VPS)

- ✅ Works even if your computer is off, thanks to GitHub Actions

<!--
## 🛠️ 使用方法 How to Use

### 1. 設定 Email Secrets（GitHub Actions）
如果使用 GitHub Actions 自動執行程式，需要將 Email 設定放到 GitHub Secrets：

| Secret 名稱      | 說明 |
|-----------------|------------------|
| `EMAIL_ADDRESS`  | 你的 Gmail 帳號 |
| `EMAIL_PASSWORD` | Gmail App 密碼（需開啟兩步驟驗證） |
| `EMAIL_RECEIVER` | 收信信箱 |

設定步驟：

1. 到你的 GitHub 專案 → **Settings → Secrets and Variables → Actions → New repository secret**  
2. 新增三個 Secrets，名稱與值對應上表  
3. Workflow 會自動讀取這些 Secrets 作為環境變數

> ⚠️ 如果想在本地測試，也可以建立 `.env` 檔案，但正式自動化建議使用 GitHub Secrets。

---

### 1. Configure Email Secrets (GitHub Actions)

If you are using GitHub Actions to run the script automatically, you need to store your email credentials as GitHub Secrets.

| Secret Name       | Description |
|------------------|-------------|
| `EMAIL_ADDRESS`   | Your Gmail address |
| `EMAIL_PASSWORD`  | Gmail App Password (2-Step Verification required) |
| `EMAIL_RECEIVER`  | Recipient email address |

**Setup steps:**

1. Go to your GitHub repository → **Settings → Secrets and Variables → Actions → New repository secret**  
2. Add the three secrets listed above, making sure the names and values match exactly  
3. The workflow will automatically load these secrets as environment variables

> ⚠️ For local testing, you may create a `.env` file. However, for production automation, using GitHub Secrets is strongly recommended.

---
-->
