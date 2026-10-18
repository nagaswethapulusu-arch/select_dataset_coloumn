import pandas as pd
import streamlit as st

st.set_page_config(page_title="Select Dataset Columns", page_icon="🔎", layout="wide")
st.title("🔎 Select Rows & Columns with loc and iloc")
st.caption("Upload a CSV or use the sample Student Performance dataset, then try label-based (loc) and position-based (iloc) selection.")

uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
try:
    df = pd.read_csv(uploaded) if uploaded is not None else pd.read_csv("student_performance.csv")
except Exception as e:
    st.error(f"Could not load the dataset: {e}")
    st.stop()

# Use the first column as the row label (e.g. student_id) so loc works with labels
df = df.set_index(df.columns[0])
st.write(f"Shape: **{df.shape[0]} rows × {df.shape[1]} columns** (row labels come from `{df.index.name}`)")
st.dataframe(df, use_container_width=True)

tab1, tab2 = st.tabs(["loc (labels)", "iloc (positions)"])

with tab1:
    st.markdown("`loc` selects by **row labels** and **column names**. The end of a slice is **included**.")
    rows = st.multiselect("Row labels", list(df.index), default=list(df.index[:3]))
    cols = st.multiselect("Column names", list(df.columns), default=list(df.columns[:2]), key="loc_cols")
    if rows and cols:
        st.code(f"df.loc[{rows}, {cols}]")
        st.dataframe(df.loc[rows, cols], use_container_width=True)

with tab2:
    st.markdown("`iloc` selects by **integer positions**. The end of a slice is **excluded**.")
    r1, r2 = st.slider("Row positions (start to end, end excluded)", 0, len(df), (0, min(5, len(df))))
    c1, c2 = st.slider("Column positions (start to end, end excluded)", 0, df.shape[1], (0, min(3, df.shape[1])))
    if r2 > r1 and c2 > c1:
        st.code(f"df.iloc[{r1}:{r2}, {c1}:{c2}]")
        st.dataframe(df.iloc[r1:r2, c1:c2], use_container_width=True)
    else:
        st.info("Choose a range that contains at least one row and one column.")

with st.expander("loc vs iloc cheat sheet"):
    st.markdown("""
| | `loc` | `iloc` |
|---|---|---|
| Based on | Labels / names | Integer positions |
| Slice end | Included | Excluded |
| Example | `df.loc['S01':'S03', 'final_score']` | `df.iloc[0:3, 4]` |
""")
