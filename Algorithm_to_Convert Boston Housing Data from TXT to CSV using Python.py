import pandas as pd

def convert_txt_to_csv(input_file, output_file):
    # Open and read the lines of the text file
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Identify the starting point of data
    start_index = next(i for i, line in enumerate(lines) if "CRIM" in line) + 1
    
    # Concatenate every two lines to form a complete row of data
    concatenated_data = [' '.join([lines[i].strip(), lines[i+1].strip()]) for i in range(start_index, len(lines), 2) if i+1 < len(lines)]
    
    # Define the column names based on the dataset description
    column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    
    # Convert the concatenated data into a DataFrame
    df = pd.DataFrame([x.split() for x in concatenated_data], columns=column_names)
    
    # Save DataFrame to CSV
    df.to_csv(output_file, index=False)

# Example usage
convert_txt_to_csv('boston.txt', 'boston_house_prices.csv')
