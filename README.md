# Machine Learning with Python

A hands-on repository for learning Python-based Machine Learning, data handling, and Streamlit app development.

## Repository Structure

```text
Machine-Learning-with-Python/
├── Data Gathering & File Handling/
│   ├── Read CSV File For ML.ipynb
│   ├── Read JSON and SQL in ML.ipynb
│   ├── f1_podiums_1950_2026.csv
│   ├── file.tsv
│   ├── test.csv
│   ├── train (1).json
│   └── world.sql
├── ML/
│   ├── End_to_End_ML.ipynb
│   ├── model.pkl
│   └── placement.csv
└── StreamLit/
    ├── app.py
    ├── Tutorials.py
    ├── File_upload.py
    ├── login.py
    ├── Startup.ipynb
    ├── requirements.txt
    ├── startup_cleaned.csv
    └── startup_funding.csv
```

## What This Repository Covers

- **Data gathering and file handling** with CSV, TSV, JSON, and SQL examples
- **Machine Learning workflow** notebooks and model artifacts
- **Streamlit mini-projects** for interactive Python data apps

## Streamlit Apps

Inside the `StreamLit/` folder:

- `Tutorials.py` — Streamlit components and widget demos
- `File_upload.py` — CSV upload and quick summary analysis
- `login.py` — basic login form demo
- `app.py` — startup funding analysis dashboard

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/aayushmanz/Machine-Learning-with-Python.git
   cd Machine-Learning-with-Python
   ```

2. **Install dependencies (Streamlit apps)**
   ```bash
   pip install -r StreamLit/requirements.txt
   ```

3. **Run any Streamlit app**
   ```bash
   streamlit run StreamLit/app.py
   ```
   You can also run:
   - `streamlit run StreamLit/Tutorials.py`
   - `streamlit run StreamLit/File_upload.py`
   - `streamlit run StreamLit/login.py`

## Tech Stack

- Python 3
- Streamlit
- Pandas
- Matplotlib
- Jupyter Notebook

## License

This project is licensed under the [LICENSE](LICENSE) file.
