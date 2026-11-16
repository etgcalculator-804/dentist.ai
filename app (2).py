from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Dentist Outreach Tracker", layout="wide")

# Make the page use the full width and remove the default top padding
st.markdown(
    """
    <style>
      .block-container {padding-top: 1rem; padding-bottom: 0; max-width: 1100px;}
      header[data-testid="stHeader"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

BASE = Path(__file__).parent


def find_html() -> Path | None:
    """Use tracker.html if present, otherwise the first .html file in the repo."""
    preferred = BASE / "tracker.html"
    if preferred.exists():
        return preferred
    files = sorted(BASE.glob("*.html"))
    return files[0] if files else None


html_file = find_html()

if html_file is None:
    st.error(
        "Koi .html file nahi mili. Repo mein tracker.html upload karein "
        "(app.py ke saath, same folder mein)."
    )
else:
    html = html_file.read_text(encoding="utf-8")
    if hasattr(st, "iframe"):
        # Newer Streamlit versions
        st.iframe(html, height=2400)
    else:
        # Older Streamlit versions
        components.html(html, height=2400, scrolling=True)
