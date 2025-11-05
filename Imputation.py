import pandas as pd
import numpy as np

data = {
    'Student' : ['A', 'B', 'C', 'D', 'E', 'F'],
    'Marks' : [85, np.nan, 78, np.nan, 92, 88]
}

frame = pd.DataFrame(data)
print(frame , "\n")
#Initially Data looks like this

marks = frame['Marks']
#Selecting marks values into separate list

valid_val = []
for value in marks:
    if not np.isnan(value):
        valid_val.append(value)
if (len(valid_val) > 0):
    mean_value = sum(valid_val) / len(valid_val)
    print('Valid values are' , valid_val , "\n")
#Collected the existing values in the dataframe
else:
    print("No data in marks")
#Took mean for the imputation (doing mean value imputation)

filled_values = []
for value in marks:
    if np.isnan(value):
        filled_values.append(mean_value)
    else:
        filled_values.append(value)
#Performed mean value imputation on this dataset

frame['Marks (Imputed)'] = filled_values
#Added a new column with imputed values

print("Data after Mean Value Imputation:")
print(frame)
