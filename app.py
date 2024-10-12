import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np  # Import numpy
from io import BytesIO
import streamlit.components.v1 as components
# Add Google Analytics tracking code
def add_google_analytics(ga_id):
    analytics_script = f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-FXEFNWY86D"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-FXEFNWY86D');
    </script>
    """
    components.html(analytics_script, height=0)
# Function to generate 2D sample data and return as a DataFrame
# Main script
GA_TRACKING_ID = "G-FXEFNWY86D"  # Replace with your own Google Analytics Tracking ID
add_google_analytics(GA_TRACKING_ID)
def generate_sample_data_2d():
    np.random.seed(42)
    categories = ['A', 'B', 'C', 'D', 'E']
    data = {
        'Category': np.random.choice(categories, size=100),
        'Values': np.random.randint(10, 100, size=100),
        'Frequency': np.random.randint(1, 10, size=100)
    }
    return pd.DataFrame(data)

# Function to generate 3D sample data and return as a DataFrame
def generate_sample_data_3d():
    np.random.seed(42)
    categories = ['A', 'B', 'C', 'D', 'E']
    data = {
        'Category': np.random.choice(categories, size=100),
        'Values': np.random.randint(10, 100, size=100),
        'Frequency': np.random.randint(1, 10, size=100),
        'Depth': np.random.randint(1, 50, size=100)  # Adding a new 'Depth' column for 3D visualization
    }
    return pd.DataFrame(data)

# Function to download DataFrame as an Excel file
def download_excel_file(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()  # Use writer.close() instead of writer.save()
    processed_data = output.getvalue()
    return processed_data

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

# Function to load and display 3D scatter plot
def show_3d_scatter_plot(df):
    fig = px.scatter_3d(df, x='Values', y='Frequency', z='Depth', color='Category', title='3D Scatter Plot of Values, Frequency, and Depth')
    st.plotly_chart(fig)

# Main script
st.sidebar.title('Options')
menu = st.sidebar.selectbox('Select menu', ['Generate 2D Sample Data', 'Generate 3D Sample Data', '2D Visualization', '3D Visualization'])

if menu == 'Generate 2D Sample Data':
    if st.sidebar.button('Generate and Download 2D Sample Data'):
        df = generate_sample_data_2d()
        st.sidebar.write("2D Sample data generated. Click below to download.")
        st.sidebar.download_button(
            label="Download 2D Sample Data",
            data=download_excel_file(df),
            file_name="sample_data_2d.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

elif menu == 'Generate 3D Sample Data':
    if st.sidebar.button('Generate and Download 3D Sample Data'):
        df = generate_sample_data_3d()
        st.sidebar.write("3D Sample data generated. Click below to download.")
        st.sidebar.download_button(
            label="Download 3D Sample Data",
            data=download_excel_file(df),
            file_name="sample_data_3d.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

else:
    page_type = st.sidebar.selectbox('Select visualization type', ['2D Visualization', '3D Visualization'])

    if page_type == '2D Visualization':
        page = st.sidebar.selectbox('Select page', ['Histogram', 'Pie Chart', 'Bar Chart', 'Line Chart', 'Scatter Plot'])
    else:
        page = st.sidebar.selectbox('Select page', ['3D Scatter Plot'])

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
        elif page == '3D Scatter Plot':
            show_3d_scatter_plot(df)
    else:
        st.write("Please upload an Excel file to proceed.")
