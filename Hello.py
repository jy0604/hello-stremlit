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

# display the data 
st.write("1.Here is a display of the toy dataframe:")
st.dataframe(df)

# Add some space between the charts
st.write("")

# Part2.Add an interactive element (slider)
st.set_option('deprecation.showPyplotGlobalUse', False)
selected_variable = st.selectbox("2.Select a Variable for Analysis", df.columns)

# Display a description of the selected variable
st.write(f"Description of {selected_variable}:")
st.write(df[selected_variable].describe())

# Add a slider to select the number of bins for the histogram
num_bins = st.slider("Select the Number of Bins for the Histogram", min_value=5, max_value=50, value=20)

# Create a histogram of the selected variable with the specified number of bins
st.write(f"Histogram of {selected_variable}:")
plt.hist(df[selected_variable], bins=num_bins)
st.pyplot()

# Add some space between the charts
st.write("")

# Part3: Select a gender to display (using a sidebar)
selected_gender = st.sidebar.selectbox("Select Gender", gen_med['Gender'].unique())

# Filter data for the selected gender
filtered_data = gen_med[gen_med['Gender'] == selected_gender]

# Create a bar plot for the selected gender
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

st.write("3.Here is a histogram:")
# Display the plot in Streamlit
st.pyplot(fig)

# Filter data for the other gender
other_gender = 'Female' if selected_gender == 'Male' else 'Male'
other_data = gen_med[gen_med['Gender'] == other_gender]

# Create a separate bar plot for the other gender
fig2, ax2 = plt.subplots(figsize=(10, 5))
x_pos2 = np.arange(len(other_data))

# Plot the data
ax2.bar(x_pos2, other_data['count'], width=0.4, label=other_gender, color='orange')
ax2.set_xticks(x_pos2)
ax2.set_xticklabels(other_data['City'], rotation=45, horizontalalignment='right')

# Customize the plot
ax2.set_xlabel("City")
ax2.set_ylabel("Average Income")
ax2.set_title(f"Average Income for {other_gender} in Each City")
ax2.legend()

fig = plt.figure()
plt.pie(gen_med['count'], labels = gen_med['City'])

# show plot
plt.show()

# Display the plot for the other gender in Streamlit
st.pyplot(fig2)

#comments
st.write("There are some Observations from bar graph.")
st.write('1.The highest average income belongs to "Mountain View" and the lowest average income belongs to "Dallas"')
st.write('2.Gender does not affect the overall trend in average income.')
st.write('3.The average income of "Austin" is close to "Boston". ')

# Part4: Add some space between the charts
st.write("")

st.write("4.Here is a Pie Chart:")
# Pie chart to show the distribution of data by city
fig3 = plt.figure(figsize=(10, 5))
plt.pie(gen_med['count'], labels=gen_med['City'], autopct='%1.1f%%')
plt.title("Income Distribution by City")
st.pyplot(fig3)

#comments
st.write("Observations from Pie Chart：")
st.write('There are significant differences in income between genders across cities.')
