import pandas as pd
import numpy as np

data = {
    'Book' : ['NCERT' , 'RD Sharma' , 'Cengage' , 'Pearson' , 'RD Sharma' , 'NCERT' , 'Cengage' , 'RD Sharma']
}

frame = pd.DataFrame(data)
print(frame , "\n")
#Initially Data looks like this

uniqueV = []
for value in data['Book']:
    if value not in uniqueV:
        uniqueV.append(value)
print('Unique values are' , uniqueV , "\n")
#Now identified unique books and put them on a list

rows = len(frame)
cols = len(uniqueV)
one_hot_matrix = np.zeros((rows, cols), dtype=int)
#Created empty matrix of zeros with rows = total values and cols = unique values

for i in range(rows):
    book_name = frame.loc[i, 'Book']
    col_index = uniqueV.index(book_name)
    one_hot_matrix[i, col_index] = 1
#Marked 1 where the category matched

one_hot_frame = pd.DataFrame(one_hot_matrix, columns = uniqueV)
final = pd.concat([frame, one_hot_frame], axis=1)
#Converted matrix into a dataframe and joined it with original dataframe

print("One Hot Encoded Data:")
print(final)
