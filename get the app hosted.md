---
title: "Hosting Your Streamlit App on Streamlit Community Cloud"
author: "Sebastiaan de Rooij"
date: "2026-02-07"
---

# Hosting Your Streamlit App on Streamlit Community Cloud

This guide provides clear, step-by-step instructions for hosting your Streamlit app online using Streamlit Community Cloud.

---

## Prerequisites
- A GitHub account ([sign up here](https://github.com/))
- Your `app.py` file ready

---

## Step 1: Upload Your Code to GitHub

1. **Create a new repository:**
   - Log in to your GitHub account.
   - Click the **+** icon in the top-right corner and select **New repository**.
   - Name your repository (e.g., `my-streamlit-app`).
   - Leave other settings as default and click **Create repository**.

2. **Upload your `app.py` file:**
   - On the repository page, click **Upload files**.
   - Drag and drop your `app.py` file into the upload area.
   - Click **Commit changes**.

---

## Step 2: Deploy on Streamlit Community Cloud

1. **Go to Streamlit Community Cloud:**
   - Visit [Streamlit Community Cloud](https://streamlit.io/cloud).
   - Click **Sign in** and log in with your GitHub account.

2. **Create a new app:**
   - Click **New app**.
   - Select the repository (`my-streamlit-app`) and the branch (`main` or `master`).
   - For the **Main file path**, enter `app.py`.
   - Click **Deploy**.

3. **Wait for deployment:**
   - Your app will be live in a few minutes.
   - Streamlit will provide a public URL (e.g., `https://your-app-name.streamlit.app`).

---

## Why This Works for You
- **No cost**: Free tier is sufficient for personal projects.
- **No server management**: Streamlit handles everything.
- **Direct and simple**: Matches your preference for clear, no-nonsense solutions.

---

## Support
- If you’re new to GitHub, follow the steps above or ask for help.
- Once deployed, share the URL with anyone to give them access to your app.

---
**Note:** This guide is designed for beginners. Let me know if you need further clarification or run into issues!
