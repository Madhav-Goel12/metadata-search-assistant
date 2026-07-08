import streamlit as st
import requests
import pandas as pd

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Metadata Search Assistant",
    page_icon="🔍",
    layout="wide"
)

# -------------------------------------------------------
# Helper Functions
# -------------------------------------------------------

def get_json(endpoint):
    try:
        response = requests.get(f"{API_URL}{endpoint}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Unable to connect to FastAPI.\n\n{e}")
        st.stop()


# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title("🔍 Metadata Search Assistant")
st.write("Search and explore metadata extracted from Kaggle datasets.")

# -------------------------------------------------------
# Dashboard Statistics
# -------------------------------------------------------

stats = get_json("/stats")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Databases", stats["databases"])

with col2:
    st.metric("Tables", stats["tables"])

with col3:
    st.metric("Columns", stats["columns"])

st.divider()

# -------------------------------------------------------
# Layout
# -------------------------------------------------------

left, center, right = st.columns([1, 2, 2])

# =======================================================
# LEFT PANEL
# =======================================================

with left:

    st.subheader("📂 Database Explorer")

    databases = get_json("/databases")

    selected_database = st.radio(
        "Choose Database",
        databases
    )

    tables = get_json(f"/databases/{selected_database}")

    selected_table = st.selectbox(
        "Choose Table",
        tables
    )

    st.divider()

    st.subheader("⚙️ Catalog")

    if st.button(
        "🔄 Refresh Catalog",
        use_container_width=True
    ):

        with st.spinner("Refreshing metadata catalog..."):

            try:

                response = requests.post(
                    f"{API_URL}/refresh"
                )

                if response.status_code == 200:

                    st.success("Catalog refreshed successfully!")

                    st.rerun()

                else:

                    st.error("Refresh failed.")

            except Exception as e:

                st.error(str(e))

# =======================================================
# CENTER PANEL
# =======================================================

with center:

    st.subheader("🔍 Search Metadata")

    search_text = st.text_input(
        "Enter database, table or column name"
    )

    search_button = st.button(
        "Search",
        use_container_width=True
    )

    results = []

    if search_button and search_text:

        response = requests.get(
            f"{API_URL}/search",
            params={
                "keyword": search_text
            }
        )

        if response.status_code == 200:

            results = response.json()

    if search_button:

        st.divider()

        st.subheader("📋 Search Results")

        if len(results) == 0:

            st.warning("No matching metadata found.")

        else:

            for result in results:

                with st.expander(
                    f"{result['column_name']} ({result['table_name']})"
                ):

                    st.write(f"**Database:** {result['database_name']}")
                    st.write(f"**Table:** {result['table_name']}")
                    st.write(f"**Column:** {result['column_name']}")
                    st.write(f"**Data Type:** {result['data_type']}")

# =======================================================
# RIGHT PANEL
# =======================================================

with right:

    st.subheader("📄 Metadata Details")

    metadata = get_json(
        f"/databases/columns/{selected_table}"
    )

    df = pd.DataFrame(metadata)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=600
    )

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.divider()

st.caption(
    "Metadata Search Assistant | FastAPI • Streamlit • SQLite • Kaggle"
)