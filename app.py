import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load and display histogram with legend
def show_histogram(df):
    fig, ax = plt.subplots()
    df['Values'].hist(ax=ax)
    ax.legend(['Values'])
    ax.set_title('Histogram of Values')
    st.pyplot(fig)

# Function to load and display pie chart with legend
def show_pie_chart(df):
    fig, ax = plt.subplots()
    pie = df['Category'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.set_ylabel('')
    ax.legend(pie.get_label(), loc="best")
    ax.set_title('Pie Chart of Category')
    st.pyplot(fig)

# Function to load and display bar chart
def show_bar_chart(df):
    fig, ax = plt.subplots()
    df.groupby('Category')['Values'].sum().plot(kind='bar', ax=ax)
    ax.set_title('Bar Chart of Values by Category')
    ax.set_ylabel('Values')
    st.pyplot(fig)

# Function to load and display line chart
def show_line_chart(df):
    fig, ax = plt.subplots()
    df.groupby('Category')['Values'].sum().plot(kind='line', ax=ax)
    ax.set_title('Line Chart of Values by Category')
    ax.set_ylabel('Values')
    st.pyplot(fig)

# Function to load and display scatter plot
def show_scatter_plot(df):
    fig, ax = plt.subplots()
    ax.scatter(df['Values'], df['Frequency'])
    ax.set_title('Scatter Plot of Values vs Frequency')
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Main script
st.sidebar.title('Options')
page = st.sidebar.selectbox('Select page', ['Histogram', 'Pie Chart', 'Bar Chart', 'Line Chart', 'Scatter Plot'])

st.title('Upload your Excel file')

uploaded_file = st.file_uploader('Choose an XLSX file', type='xlsx')

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    if page == 'Histogram':
        show_histogram(df)
    elif page == 'Pie Chart':
        show_pie_chart(df)
    elif page == 'Bar Chart':
        show_bar_chart(df)
    elif page == 'Line Chart':
        show_line_chart(df)
    elif page == 'Scatter Plot':
        show_scatter_plot(df)
else:
    st.write("Please upload an Excel file to proceed.")
