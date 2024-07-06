import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load and display histogram with legend
def show_histogram(df):
    fig, ax = plt.subplots()
    df['Values'].hist(ax=ax)
    ax.legend(['Values'])
    st.pyplot(fig)

# Function to load and display pie chart with legend
def show_pie_chart(df):
    fig, ax = plt.subplots()
    pie = df.groupby('Category')['Frequency'].sum().plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.legend(pie.get_label(), loc="best")
    st.pyplot(fig)

# Main script
st.sidebar.title('Options')
page = st.sidebar.selectbox('Select page', ['Histogram', 'Pie Chart'])

st.title('Upload your Excel file')

uploaded_file = st.file_uploader('Choose an XLSX file', type='xlsx')

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    if page == 'Histogram':
        show_histogram(df)
    elif page == 'Pie Chart':
        show_pie_chart(df)
else:
    st.write("Please upload an Excel file to proceed.")
