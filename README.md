# 🔎 Select Dataset Columns (Pandas loc & iloc)

Select specific rows and columns from a dataset using Pandas `loc` and `iloc`, with examples and output for each.

## Objective
Learn how to access specific parts of a DataFrame.

## Tools
- Python
- Pandas
- Jupyter Notebook
- Streamlit (for the deployed demo)

## Dataset
Sample Student Performance dataset (`student_performance.csv`, 20 rows, 7 columns):
`student_id, gender, hours_studied, attendance_pct, previous_score, final_score, result`
The notebook creates this file itself, so no download is needed.

## Project Structure
```
├── Select_Dataset_Columns.ipynb   # Main notebook
├── student_performance.csv        # Dataset
├── app.py                         # Streamlit web app
├── requirements.txt               # Dependencies
└── README.md
```

## loc vs iloc

| | `loc` | `iloc` |
|---|---|---|
| Based on | Labels / column names | Integer positions |
| Slice end | **Included** | **Excluded** |
| Example | `df.loc['S01':'S03', ['hours_studied', 'final_score']]` | `df.iloc[0:3, [1, 4]]` |

## What the Notebook Covers
- Selecting a single column and multiple columns
- `loc`: one row, many rows, row ranges, rows and columns, single value, conditions, column ranges
- `iloc`: first row, specific rows, row ranges, rows and columns, single value, last rows and first columns
- Side-by-side comparison of `loc` and `iloc`

## Run Locally
```bash
git clone https://github.com/<your-username>/pandas-loc-iloc-selection.git
cd pandas-loc-iloc-selection
pip install -r requirements.txt

jupyter notebook Select_Dataset_Columns.ipynb   # notebook
streamlit run app.py                            # web app
```

## Deploy (Streamlit Community Cloud)
1. Push this repo to GitHub (include `student_performance.csv`).
2. Go to share.streamlit.io and click **New app**.
3. Select the repo, branch `main`, main file `app.py`.
4. Click **Deploy**.

## Interview Questions
- **Difference between loc and iloc?** `loc` selects by labels and includes the slice end; `iloc` selects by integer position and excludes the slice end.
- **How do you select a single column?** `df['col']` returns a Series.
- **How do you select multiple columns?** `df[['col1', 'col2']]` returns a DataFrame.

## Author
Swetha, AI & ML Track, Veda Technology
