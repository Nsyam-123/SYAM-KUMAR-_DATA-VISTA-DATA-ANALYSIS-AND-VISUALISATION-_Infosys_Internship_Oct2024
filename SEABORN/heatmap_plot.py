# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Select only numeric columns for correlation
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
correlation_matrix = numeric_data.corr()

# Set the figure size
plt.figure(figsize=(8, 6))

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", 
            square=True, cbar_kws={"shrink": 0.8}, 
            linewidths=0.5, linecolor='black')

# Add titles and labels
plt.title("Heatmap of Feature Correlations in the Iris Dataset")
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.yticks(rotation=0)    # Keep y labels horizontal

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
