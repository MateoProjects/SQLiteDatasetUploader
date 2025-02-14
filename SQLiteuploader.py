import streamlit as st 
import sqlite3
import pandas as pd

if 'file_uploaded' not in st.session_state:
    st.session_state['file_uploaded'] = False

def main():
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.title("Dataset Uploader")
    
    if not st.session_state.file_uploaded:
        st.session_state.uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

        if st.session_state.uploaded_file is not None:
            if st.button("Processing"):
                st.session_state['file_uploaded'] = True
                st.rerun()
    
    if st.session_state.get('file_uploaded'):
        try:
            if 'data' not in st.session_state:
                st.session_state.data = pd.read_csv(st.session_state.uploaded_file)
            columns = st.session_state.data.columns.tolist()
            # disply first 5 rows of the data withoud index
            st.write(st.session_state.data.head())
            selected = st.selectbox("Select the column to be used as class label", columns)
            name_table = st.text_input(label="Insert the name of the table", value=st.session_state.uploaded_file.name.split(".")[0])
            if st.button("Process"):
                st.write("Adding to db")
                st.success("Data added to db")
        except pd.errors.EmptyDataError:
            st.error("The uploaded file is empty. Please upload a valid CSV file.")
        except Exception as e:
            print("im here why?")
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()