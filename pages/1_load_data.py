import streamlit as st
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

st.title('Upload your data')

uploaded_files = st.file_uploader(
    'Choose a csv file',
    accept_multiple_files=False,
    type=['csv']
)

if uploaded_files:
    df = pd.read_csv(uploaded_files)
    print(df)
    dfs = {
        "Male": df[df['customer_gender']=='female'],
        "Female": df[df['customer_gender']!='female']
    }
    
    for title, data in dfs.items():
        data.drop(columns='customer_gender', inplace=True)
        st.subheader(f'{title} data:')
        st.dataframe(data)

    fig, ax = plt.subplots()

    # st.subheader('Male Age')
    # ax.hist(dfs['Male']['customer_age'])
    # ax.set_title('Male Age')
    # ax.set_xlabel('Male count')
    # ax.set_ylabel('Age')

    # st.pyplot(fig)
    # st.bar_chart(data=dfs['Male'], x='country', y='customer_age')

    df_female = dfs['Female']
    st.subheader('Female revenue for Age')
    st.line_chart(data=df_female[df_female['revenue']>2000], x='customer_age', y='revenue')


