import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

# URL of the dataset
data_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
local_file_path = "D:/titanic.csv"  # Change this to your desired location

# Download the dataset
response = requests.get(data_url)
with open(local_file_path, 'wb') as f:
    f.write(response.content)

print(f"Dataset downloaded and saved as {local_file_path}")

# Load the dataset from the local file
df = pd.read_csv(local_file_path)

# Display the first few rows of the dataset
print(df.head())

# Visualize the distribution of ages
sns.histplot(df['Age'].dropna(), kde=True)
plt.title('Distribution of Ages')
plt.show()
