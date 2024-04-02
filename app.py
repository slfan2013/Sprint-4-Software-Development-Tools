
import streamlit as st
import pandas as pd
import plotly.express as px


# read dataset
df = pd.read_csv("vehicles_us.csv")
df['model_year'] = df['model_year'].astype("Int64")
df['cylinders'] = df['cylinders'].astype("Int64")
df['is_4wd'] = df['is_4wd'].fillna("No")
df['is_4wd'] = df['is_4wd'].replace(1, "Yes")
df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')


# Header
st.header('Car Sales Advertisement Visualization')


# Checkbox to toggle the chart
column_to_plot_options = df.select_dtypes(include=['float', 'int']).columns.tolist()
column_to_plot_default_option = 'days_listed'
column_to_plot_default_index = column_to_plot_options.index(column_to_plot_default_option)
column_to_plot = st.selectbox('Select the column to plot against price:', column_to_plot_options, index=column_to_plot_default_index)

# Dropdown to select the type of plot
color_to_plot_options = df.select_dtypes(include=['object']).columns.tolist()
color_to_plot_default_option = 'fuel'
color_to_plot_default_index = color_to_plot_options.index(color_to_plot_default_option)
color_to_plot = st.selectbox('Select color group:', color_to_plot_options, index=color_to_plot_default_index)


fig_scatter = px.scatter(df, x=column_to_plot, y='price', color=color_to_plot, title=f"Price v.s. {column_to_plot}, color by {color_to_plot}", opacity=0.6)
st.plotly_chart(fig_scatter)





# select column to draw histogram
column_to_hist_options = df.select_dtypes(include=['float', 'int']).columns.tolist()
column_to_hist_default_option = 'price'
column_to_hist_default_index = column_to_hist_options.index(column_to_hist_default_option)
column_to_hist = st.selectbox('Select the column to draw Histogram:', column_to_hist_options, index=column_to_hist_default_index, key='column_to_hist')

    

# Dropdown to select the type of hist
color_to_hist_options = df.select_dtypes(include=['object']).columns.tolist()
color_to_hist_default_option = 'condition'
color_to_hist_default_index = color_to_hist_options.index(color_to_hist_default_option)
color_to_hist = st.selectbox('Select color group:', color_to_hist_options, index=color_to_hist_default_index, key='color_to_hist')


# Checkbox to toggle the chart
bar_mode = st.checkbox('Group Bar Mode', value=True)

if bar_mode:
    # Plotly Express histogram
    fig = px.histogram(df, x=column_to_hist, color=color_to_hist, barmode='group',
                   title=f'Histogram of {column_to_hist} with Different {color_to_hist} Colors', opacity=0.6) # This uses a predefined color sequence
else:
    # Plotly Express histogram
    fig = px.histogram(df, x=column_to_hist, color=color_to_hist, barmode='relative',
                   title=f'Histogram of {column_to_hist} with Different {color_to_hist} Colors', opacity=0.6) # This uses a predefined color sequence    



st.plotly_chart(fig)
