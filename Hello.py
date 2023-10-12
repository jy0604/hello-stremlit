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

# Select a gender to display (using a sidebar)
selected_gender = st.sidebar.selectbox("Select Gender", gen_med['Gender'].unique())

# Filter data for the selected gender
filtered_data = gen_med[gen_med['Gender'] == selected_gender]

# Create a bar plot for the selected gender
st.write(f"### Average Income for {selected_gender} in Each City")

fig, ax = plt.subplots(figsize=(10, 5))
x_pos = np.arange(len(filtered_data))
tick_labels = filtered_data['City']

# Plot the data
ax.bar(x_pos, filtered_data['count'], width=0.4, label=selected_gender)
ax.set_xticks(x_pos)
ax.set_xticklabels(tick_labels, rotation=45, horizontalalignment='right')

# Customize the plot
ax.set_xlabel("City")
ax.set_ylabel("Average Income")
ax.set_title(f"Average Income for {selected_gender} in Each City")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Filter data for the other gender
other_gender = 'Female' if selected_gender == 'Male' else 'Male'
other_data = gen_med[gen_med['Gender'] == other_gender]

# Create a separate bar plot for the other gender
st.write(f"### Average Income for {other_gender} in Each City")

fig2, ax2 = plt.subplots(figsize=(10, 5))
x_pos2 = np.arange(len(other_data)

# Plot the data
ax2.bar(x_pos2, other_data['count'], width=0.4, label=other_gender, color='orange')
ax2.set_xticks(x_pos2)
ax2.set_xticklabels(other_data['City'], rotation=45, horizontalalignment='right')

# Customize the plot
ax2.set_xlabel("City")
ax2.set_ylabel("Average Income")
ax2.set_title(f"Average Income for {other_gender} in Each City")
ax2.legend()

# Display the plot for the other gender in Streamlit
st.pyplot(fig2)

# Pie chart
st.write(f"### Pie Chart: Average Income Distribution in All Cities")
fig = plt.figure()
plt.pie(gen_med['count'], labels=gen_med['City'], autopct='%1.1f%%', startangle=140)

# Display the pie chart in Streamlit
st.pyplot(fig)
