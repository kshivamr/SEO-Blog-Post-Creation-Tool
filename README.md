
⭐ **README – SEO Blog Post Creation Tool**

📌 **Overview**

This project is an **AI-based SEO Blog Post Creation Tool** that automates the entire workflow of:

1. Scraping trending products from Amazon
2. Generating SEO-friendly keywords
3. Creating a 150–200 word blog using Groq LLaMA AI
4. Publishing the blog directly to **Blogger** using Google OAuth

It works as a complete **end-to-end pipeline** with no manual intervention.

---

## 🚀 **Features**

* Scrapes best-selling products using BeautifulSoup
* Creates SEO keywords automatically
* Generates high-quality SEO blogs using **Groq API**
* Publishes blog posts directly to Blogger through the **Blogger API**
* Secure authentication using **Google OAuth**
* Uses fallback product when scraping fails
* Fully automated single-command execution

---

## 🛠 **Tech Stack**

* **Python**
* **BeautifulSoup** (Web Scraping)
* **Groq LLaMA 3 Model**
* **Google OAuth 2.0**
* **Blogger API v3**
* **dotenv** (Environment variables)

---

## 📂 **Project Structure**

```
SEO Blog Post Creation Tool/
│── main.py
│── scraper.py
│── keywords.py
│── blog_generator.py
│── publisher_blogger.py
│── requirements.txt
│── .env                 (NOT shared)
│── client_secret.json   (NOT shared)
│── token.json           (auto-created, NOT shared)
```

---

## 🔑 **Environment Variables**

Create a `.env` file:

```
GROQ_API_KEY=your_groq_key
BLOG_ID=your_blogger_blog_id
```

---

## 🔧 **Setup Instructions**

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Add environment variables

Create `.env` in project folder.

### 3️⃣ Add Google OAuth credentials

Place your downloaded file:

```
client_secret.json
```

in the project root.

### 4️⃣ Run the tool

```
python main.py
```

You will be asked to log in with Google and allow Blogger posting permissions.

---

## ⚙️ **How It Works (Pipeline)**

### **Step 1 → Scrape Amazon**

Fetches trending product details.
Uses fallback product if Amazon blocks scraping.

### **Step 2 → Generate SEO Keywords**

Creates 3–4 optimized keywords based on product name.

### **Step 3 → Generate Blog with AI**

Uses Groq LLaMA model to write a 150–200 word SEO content piece.

### **Step 4 → Publish to Blogger**

Authenticates with Google OAuth and posts the blog automatically.

---

## 🔐 **Security Notes**

Do **NOT** share:

* `.env`
* `client_secret.json`
* `token.json`
* API keys

These contain sensitive information.

---

## 📝 **Task Status**

* ✔ Task 2 Completed Successfully
* Fully working, tested, and automated pipeline
* Ready for submission


