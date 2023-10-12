import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your CSV data
df = pd.read_csv('toy_dataset.csv')

# Group the data
gen_med = df.groupby('Gender')['Income'].mean().reset_index(name='count')

# Create a Streamlit app
st.title("Average Income by Gender")

# Create a bar plot for gender
fig, ax = plt.subplots(figsize=(8, 6))
x_pos = np.arange(len(gen_med))
tick_labels = gen_med['Gender']

# Plot the data
ax.bar(x_pos, gen_med['count'], width=0.4, color='blue')
ax.set_xticks(x_pos)
ax.set_xticklabels(tick_labels)

# Customize the plot
ax.set_xlabel("Gender")
ax.set_ylabel("Average Income")
ax.set_title("Average Income by Gender")

# Display the plot in Streamlit
st.pyplot(fig)
