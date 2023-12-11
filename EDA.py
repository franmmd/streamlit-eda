# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

st.set_page_config(
    page_title="EDA Exploratory Data Analysis",
    page_icon="📃",
)

def run():

    st.write("✉️franmmd@gmail.com")

    # Upload CSV data
with st.sidebar.header('Upload your data file'):
    uploaded_file = st.sidebar.file_uploader("Data file", type=["csv", "xls", "xlsx", "xlsm"])
    separator = st.sidebar.text_input(
            "CSV Delimiter",
            value=",",
            max_chars=1,
            help="How your CSV values are separated (doesn't matter for excel)",
        )
    decimal = st.sidebar.text_input(
            "CSV Decimal point",
            value=".",
            max_chars=1,
            help="Character to recognize as decimal point (e.g., use ‘,’ for European data).",
        )
    use_sample = False
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")
 
st.write("# Exploratory Data Analysis! 📃")
# Pandas Profiling Report
if uploaded_file is not None:
  
    st.write("**File**:",uploaded_file.name)
    st.write("Type:", uploaded_file.type)
    st.write("Size:", uploaded_file.size)

   # @st.cache_data
    def read_csv_or_excel(data, sep, decimal):
        try:
            raw_df = pd.read_csv(data, sep=sep,decimal=decimal)
        except UnicodeDecodeError:
            try:
                raw_df = pd.read_excel(data)
            except Exception as e:
                raise e
        return raw_df


    df = read_csv_or_excel(uploaded_file, separator, decimal)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    pr = ProfileReport(df, explorative=True)
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for data file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

    st.markdown(
        """
         **👈 Select a file from the sidebar** 
        This is base on the work of [Data Professor]
        """
    )


if __name__ == "__main__":
    run()
