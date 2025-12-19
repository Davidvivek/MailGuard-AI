# 🛡️ MailGuard AI
**MailGuard AI** is a full-stack intelligent email assistant designed to declutter your inbox and automate response workflows. By leveraging the **Google Gemini API**, it goes beyond simple spam filtering to understand the *context* and *intent* of your messages.

---

## 🚀 Key Features

### 🧠 Intelligent Analysis
* **Spam vs. Genuine Classification:** Uses semantic analysis to detect sophisticated spam that traditional keyword filters might miss.
* **Tonal Context Detection:** Automatically tags emails with context labels (e.g., `🔴 Urgent`, `🔵 Informative`, `🟡 Reminder`) to help you prioritize critical attention.

### ⚡ Real-Time Interaction
* **Instant Summarization:** Condenses long, complex email threads into concise 3-bullet executive summaries.
* **Context-Aware Drafts:** Generates polite, professionally tone-matched reply drafts automatically, ready for you to review and send.
* **Zero-Reload Experience:** Built with **Asynchronous JavaScript (Fetch API)** to provide instant feedback without refreshing the page.

### ⚙️ Performance & Architecture
* **Optimized API Usage:** Implements backend logic to sanitize inputs and manage token limits, ensuring cost-effective and low-latency performance.
* **Modular Design:** Clean separation of concerns (Backend Logic vs. API Integration vs. Frontend) to support easy scaling and future cloud deployment.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask (REST API)
* **AI Engine:** Google Gemini Pro API
* **Frontend:** HTML5, Tailwind CSS 
* **Scripting:** JavaScript (ES6+)

---
```bash
git clone [https://github.com/davidvivek/MailGuard-AI.git](https://github.com/davidvivek/MailGuard-AI.git)
cd MailGuard-AI
