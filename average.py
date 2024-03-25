import pandas as pd

# Read the excel file
##You can read the file format whatever you want. For example excel file;

file path = "------------------.xlsx"  #
data = pd.read_excel

# To convert text values in the 'vsini' column to numeric values
data['Vsini'] = pd.to_numeric(data['Vsini'], errors='coerce')

# To group Spectral Type values and their corresponding vsini:
grouped_data = grouped_data('ST')['Vsini'].mean()

# To print the results:
print("Spectral Class and Avarege Vsini:")
print(grouped_data.to_string())
