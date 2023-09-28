import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your CSV data
df = pd.read_csv('toy_dataset.csv')

# Group the data
gen_med = df.groupby(['City', 'Gender'])['Income'].mean().reset_index(name='count')

# Create a Streamlit app
st.title("Average Income Per City by Gender")

# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 5))
x_pos = np.arange(len(gen_med['City'].unique()))
tick_labels = gen_med['City'].unique()

# Plot the data for both genders
female_data = gen_med[gen_med['Gender'] == 'Female']
male_data = gen_med[gen_med['Gender'] == 'Male']

ax.bar(x_pos - 0.2, female_data['count'], width=0.4, label='Female')
ax.bar(x_pos + 0.2, male_data['count'], width=0.4, label='Male')
ax.set_xticks(x_pos)
ax.set_xticklabels(tick_labels, rotation=45, horizontalalignment='right')

# Customize the plot
ax.set_xlabel("City")
ax.set_ylabel("Average Income")
ax.set_title("Average Income Per City by Gender")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

