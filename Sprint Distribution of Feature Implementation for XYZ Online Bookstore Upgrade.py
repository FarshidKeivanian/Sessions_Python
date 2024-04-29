import pandas as pd

# Define the data
data = {
    'Feature': [
        'Improve navigation, search, checkout',
        'Mobile-friendly website',
        'Enhanced search functionality',
        'Tailored book suggestions',
        'Rewards system',
        'Social media integration',
        'Interactive book previews'
    ],
    'Sprint': ['1', '1', '2', '2', '3', '3', '4']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
