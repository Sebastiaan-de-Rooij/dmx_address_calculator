# Chat GPT:

Here is the **entire cheat sheet as one single Markdown block**, ready to copy:

````markdown
# 📊 Streamlit Cheat Sheet (Simple Scripts)

## 1. Run Your App
```bash
streamlit run app.py
````

---

## 2. Import Streamlit

```python
import streamlit as st
```

---

## 3. Basic Text Output

### Title & Headers

```python
st.title("My App")
st.header("Header")
st.subheader("Subheader")
```

### Text

```python
st.write("Hello, world!")
st.text("Plain text")
st.markdown("**Bold** *Italic*")
```

---

## 4. Display Data

### DataFrames

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
})

st.dataframe(df)
st.table(df)
```

### JSON

```python
st.json({"name": "Alice", "age": 25})
```

---

## 5. User Input Widgets

### Button

```python
if st.button("Click me"):
    st.write("Button clicked!")
```

### Text Input

```python
name = st.text_input("Your name")
```

### Number Input

```python
age = st.number_input("Your age", min_value=0)
```

### Slider

```python
value = st.slider("Pick a number", 0, 100)
```

### Checkbox

```python
agree = st.checkbox("I agree")
```

### Select Box

```python
option = st.selectbox("Choose", ["A", "B", "C"])
```

---

## 6. Layout

### Columns

```python
col1, col2 = st.columns(2)

with col1:
    st.write("Left")

with col2:
    st.write("Right")
```

### Sidebar

```python
st.sidebar.title("Menu")
choice = st.sidebar.selectbox("Pick", ["Home", "About"])
```

---

## 7. Images & Media

### Image

```python
from PIL import Image

img = Image.open("photo.jpg")
st.image(img, caption="My Photo")
```

### Audio / Video

```python
st.audio("sound.mp3")
st.video("video.mp4")
```

---

## 8. Charts

### Line Chart

```python
import pandas as pd

data = pd.DataFrame({
    "x": [1,2,3,4],
    "y": [10,20,15,30]
})

st.line_chart(data)
```

### Bar Chart

```python
st.bar_chart(data)
```

---

## 9. Forms

```python
with st.form("my_form"):
    name = st.text_input("Name")
    submit = st.form_submit_button("Submit")

if submit:
    st.write("Hello", name)
```

---

## 10. Status Messages

```python
st.success("Success!")
st.info("Info")
st.warning("Warning")
st.error("Error")
```

---

## 11. Caching (Performance)

```python
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")
```

---

## 12. Session State (Memory)

```python
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Add"):
    st.session_state.count += 1

st.write(st.session_state.count)
```

---

## 13. Simple App Template

```python
import streamlit as st

st.title("My First App")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.write("Hello,", name)
```

---

## 14. Stop / Rerun App

### Rerun

```python
st.rerun()
```

### Stop

```python
st.stop()
```

---

## 15. Helpful Commands

| Task          | Command                |
| ------------- | ---------------------- |
| Run app       | `streamlit run app.py` |
| Check version | `streamlit --version`  |
| Help          | `streamlit help`       |

---

## ✅ Tip

Start simple:

```python
import streamlit as st

st.title("Hello Streamlit")
st.write("It works!")
```

Then expand from there.

```

If you want, I can next compress this into a **one-page “printable” version** with only the most-used commands.
```
