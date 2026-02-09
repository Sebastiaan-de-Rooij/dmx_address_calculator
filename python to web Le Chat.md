

# volgens mij is dit alleen hoe ik een webapp maak, niet hoe ik em host!!!!

---
title: "Streamlit Guide: Run Python Scripts as Webpages"
author: "Sebastiaan de Rooij"
date: "2026-02-06"
---

# Streamlit Guide: Run Python Scripts as Webpages

This guide is designed for beginners who want to run Python scripts as webpages using Streamlit, without needing to know HTML or JavaScript.

---

## Prerequisites
- A Mac with Terminal access
- Python 3 installed (check with `python3 --version`)

---

## Step 1: Install Streamlit

1. Open **Terminal**.
2. Run the following command to install Streamlit:
   ```bash
   pip3 install streamlit
   ```
3. If you encounter a permission error, use:
   ```bash
   pip3 install --user streamlit
   ```
4. If `pip3` doesn’t work, try:
   ```bash
   python3 -m pip install streamlit
   ```

---

## Step 2: Verify Installation

Check if Streamlit is installed by running:
```bash
streamlit --version
```
You should see a version number (e.g., `1.29.0`).

---

## Step 3: Create Your Python Script

1. Open a text editor (e.g., TextEdit or VS Code).
2. Create a new file named `app.py`.
3. Add the following code to `app.py`:
   ```python
   import streamlit as st

   st.title("My First Web App")
   st.write("Hello, Sebastiaan! This is your Python script running as a webpage.")
   ```
4. Save the file in a folder of your choice.

---

## Step 4: Run Your Script as a Webpage

1. In **Terminal**, navigate to the folder where you saved `app.py`. For example:
   ```bash
   cd ~/Documents
   ```
2. Run your script with:
   ```bash
   streamlit run app.py
   ```
3. A new tab will open in your browser, displaying your webpage.

---

## Step 5: Customize Your Webpage (Optional)

You can edit `app.py` to add more features. For example:
```python
import streamlit as st

name = st.text_input("What's your name?")
st.write(f"Hello, {name}! This is your webpage.")
```
Save the file, and the webpage will update automatically.

---

## Troubleshooting

- If you get a "command not found" error, ensure Python and pip are installed:
  ```bash
  python3 --version
  pip3 --version
  ```
- If you need help, feel free to ask for clarification or support!

---

## Next Steps

- Experiment with adding more Python code to make your webpage interactive.
- If you want to share your webpage, consider deploying it for free using [Streamlit Community Cloud](https://streamlit.io/cloud).

---

**Note:** This guide is designed for beginners. Let me know if you’d like to explore more advanced features or have any questions!
