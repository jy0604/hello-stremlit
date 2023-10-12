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

# Create a sidebar with interactive elements
selected_gender = st.sidebar.selectbox("Select Gender", gen_med['Gender'].unique())

# Filter data for the selected gender
filtered_data = gen_med[gen_med['Gender'] == selected_gender]

# Create a bar plot for both genders combined
fig, ax = plt.subplots(figsize=(10, 5))
x_pos = np.arange(len(filtered_data))
tick_labels = filtered_data['City']

# Plot the data
ax.bar(x_pos, filtered_data['count'], width=0.4, label=selected_gender, color='blue')
ax.set_xticks(x_pos)
ax.set_xticklabels(tick_labels, rotation=45, horizontalalignment='right')

# Customize the plot
ax.set_xlabel("City")
ax.set_ylabel("Average Income")
ax.set_title(f"Average Income for {selected_gender} in Each City")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Pie chart to show the distribution of data by gender
gender_data = gen_med.groupby('Gender')['count'].sum()
fig2 = plt.figure(figsize=(5, 5))
plt.pie(gender_data, labels=gender_data.index, autopct='%1.1f%%')
plt.title("Income Distribution by Gender")
st.pyplot(fig2)
