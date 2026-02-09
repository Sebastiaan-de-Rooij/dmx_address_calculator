```markdown
# Tutorial: Deploying a Python Script as a Web App (Streamlit)

If you want to turn a Python script into a functional website without touching a single line of HTML, CSS, or JavaScript, the standard industry tool is **Streamlit**. It is an open-source framework designed to create web apps using only Python code.

---

## 1. Environment Setup
Ensure you have Python installed, then install the Streamlit library via your terminal or command prompt:

```bash
pip install streamlit

```

## 2. Create Your Script

Streamlit replaces standard terminal interactions (like `input()` or `print()`) with web widgets. Create a file named `app.py` and add the following code:

```python
import streamlit as st

# Website Header
st.title("My Python Web App")

# Text Input Widget
name = st.text_input("Enter your name:")

# Button Logic
if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! Your Python script is now a website.")
    else:
        st.error("Please enter a name.")

```

## 3. Launch Your App Locally

To view your website on your machine, run the following command in your terminal:

```bash
streamlit run app.py

```

A browser tab will automatically open at `http://localhost:8501`.

---

## 4. Deploying to the Internet (Fast & Free)

To make your script accessible to the public, use **Streamlit Community Cloud**:

1. **GitHub**: Upload your `app.py` to a public GitHub repository.
2. **Requirements**: Add a file named `requirements.txt` to the same folder containing only the word `streamlit`.
3. **Connect**: Sign in to [Streamlit Cloud](https://share.streamlit.io/) using your GitHub account.
4. **Deploy**: Select your repository and click **Deploy**. Your app will be live at a custom URL (e.g., `your-app.streamlit.app`).

---

## Essential Python Web Commands

* `st.header()` / `st.subheader()`: For organizing text.
* `st.number_input()`: For capturing numerical data.
* `st.file_uploader()`: To allow users to upload files for your script to process.
* `st.dataframe()`: To display Excel or CSV data in an interactive table.

**Summary:** This method provides a professional web interface while keeping 100% of your logic in Python, bypassing the need for frontend languages entirely.

```

```
