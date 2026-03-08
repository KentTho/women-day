# 💐 Happy 8/3 – Romantic Greeting Card Web App

A beautiful animated greeting card for International Women's Day, built with Flask + pure HTML/CSS/JS.

---

## 📁 Project Structure

```
womens-day/
├── app.py              ← Flask backend (just 10 lines!)
├── requirements.txt    ← Python dependencies
├── render.yaml         ← Render.com deployment config
├── Procfile            ← Railway / Heroku config
├── README.md           ← This file
└── templates/
    └── index.html      ← Everything: HTML + CSS + JS animations
```

---

## 🏃 Run Locally (to preview before sending)

```bash
# 1. Install Python 3.10+ if not already installed
# 2. Open terminal in this folder, then:

pip install flask gunicorn

python app.py

# 3. Open http://localhost:5000 in your browser
```

---

## 🚀 Deploy to Render (FREE – recommended, easiest)

> You'll get a public link like: `https://womens-day-card.onrender.com`

### Steps:

1. **Create a GitHub account** at https://github.com if you don't have one.

2. **Create a new repository** on GitHub:
   - Click ➕ > New repository
   - Name it `womens-day-card`
   - Set to **Public**
   - Click **Create repository**

3. **Upload your files** to the repo:
   - Drag and drop all project files (app.py, requirements.txt, render.yaml, templates/ folder) into the GitHub repo page
   - Click **Commit changes**

4. **Create a Render account** at https://render.com (free, sign in with GitHub)

5. **Deploy:**
   - Click **New +** → **Web Service**
   - Connect your GitHub repo `womens-day-card`
   - Render will auto-detect the `render.yaml` config
   - Click **Create Web Service**
   - Wait ~2 minutes for the build to complete ✅

6. **Copy your live URL** (shown at the top of the Render dashboard) and send it to your girlfriend! 🎉

---

## 🚀 Deploy to Railway (FREE alternative)

1. Go to https://railway.app and sign in with GitHub
2. Click **New Project** → **Deploy from GitHub repo**
3. Select your `womens-day-card` repo
4. Railway auto-detects the Procfile and deploys
5. Click **Generate Domain** to get your public URL

---

## 🚀 Deploy to Replit (easiest for beginners)

1. Go to https://replit.com and create a free account
2. Click **Create Repl** → choose **Python** template
3. Upload your files or paste the code
4. In `main.py`, paste the contents of `app.py`
5. In Shell: `pip install flask`
6. Click the green **Run** button
7. Replit gives you a public URL instantly! Share it 💌

---

## ✏️ Customize the Card Message

Open `templates/index.html` and find this section (~line 180):

```html
<p class="card-message">
  Chúc em một ngày <em>8/3</em> thật hạnh phúc.<br/><br/>
  ...
</p>
```

Edit the text to add your own personal message! 💕

---

## 🎨 Customize Colors

At the top of `templates/index.html`, find the `:root` CSS variables:

```css
:root {
  --rose:      #f472b6;   /* main pink */
  --deep-rose: #be185d;   /* dark rose */
  --lilac:     #c4b5fd;   /* purple accent */
  ...
}
```

Change hex codes to adjust the color scheme.

---

Made with ❤️ for International Women's Day 🌸
