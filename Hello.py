import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your CSV data
df = pd.read_csv('toy_dataset.csv')

# Group the data
gen_med = df.groupby(['City', 'Gender'])['Income'].mean().reset_index(name='count')

# Create a Streamlit app
st.title("Some interesting data about toy")

# Create a bar plot for both genders combined
fig, ax = plt.subplots(figsize=(10, 5))
x_pos = np.arange(len(gen_med))
tick_labels = gen_med['City']

# Plot the data for both genders
ax.bar(x_pos, gen_med['count'], width=0.4, label='Combined', color='blue')
ax.set_xticks(x_pos)
ax.set_xticklabels(tick_labels, rotation=45, horizontalalignment='right')

# Customize the plot
ax.set_xlabel("City")
ax.set_ylabel("Average Income")
ax.set_title("Average Income for Both Genders in Each City")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Pie chart to show the distribution of data by gender
gender_data = gen_med.groupby('Gender')['count'].sum()
fig2 = plt.figure(figsize=(5, 5))
plt.pie(gender_data, labels=gender_data.index, autopct='%1.1f%%')
plt.title("Income Distribution by Gender")
st.pyplot(fig2)
