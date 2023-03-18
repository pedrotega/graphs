import matplotlib.pyplot as plt
import numpy as np

# Create sample data
categories = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']
data = np.array([[20, 30, 50], [10, 40, 50], [30, 30, 40]])

# Convert data to percentages
data_percent = (data / data.sum(axis=1)[:, np.newaxis]) * 100

# Define custom colors for each group
colors = ['#007acc', '#e74c3c', '#27ae60']

# Create stacked horizontal bar chart with custom colors
fig, ax = plt.subplots()
ax.barh(categories, data_percent[:, 0], color=colors[0], label='Tester 1')
ax.barh(categories, data_percent[:, 1], left=data_percent[:, 0], color=colors[1], label='Tester 2')
ax.barh(categories, data_percent[:, 2], left=data_percent[:, 0] + data_percent[:, 1], color=colors[2], label='Tester 3')

# Add legend and axis labels
ax.legend()
ax.set_xlabel('Percentage')
ax.set_ylabel('Categories')

plt.show()
