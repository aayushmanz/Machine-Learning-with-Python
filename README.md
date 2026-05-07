# Machine Learning with Python

A hands-on learning journey through Machine Learning and Python-based data tools.

---

## Repository Structure

```
Machine-Learning-with-Python/
│
└── StreamLit/
    ├── Tutorials.py       # Streamlit UI components & layout tutorial
    ├── File_upload.py     # CSV file uploader with summary stats
    ├── login.py           # Simple login form demo
    └── image.png          # Sample image used in tutorials
```

---

## Projects

### StreamLit

Hands-on demos exploring the [Streamlit](https://streamlit.io/) library for building interactive web apps with Python.

| File | Description |
|---|---|
| `Tutorials.py` | Covers Streamlit essentials: text elements, dataframes, media, layouts, status messages, a progress bar, and user input widgets |
| `File_upload.py` | Lets users upload a CSV file and instantly view summary statistics via `df.describe()` |
| `login.py` | A basic login form with email/password validation and gender selection |

---

## Setup & Running

1. **Clone the repository**
   ```bash
   git clone https://github.com/aayushmanz/Machine-Learning-with-Python.git
   cd Machine-Learning-with-Python
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas
   ```

3. **Run a Streamlit app**
   ```bash
   streamlit run StreamLit/Tutorials.py
   ```

---

## Technologies Used

- **Python 3**
- **Streamlit** – interactive web apps
- **Pandas** – data manipulation & analysis

---

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

