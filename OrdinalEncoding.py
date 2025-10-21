import pandas as pd

data = {
    'Book' : ['NCERT' , 'RD Sharma' , 'Cengage' , 'Pearson' , 'RD Sharma' , 'NCERT' , 'Cengage' , 'RD Sharma']
}

frame = pd.DataFrame(data)
#Initially Data looks like this
print(frame)
print()

uniqueV = []
for value in frame['Book']:
    if value not in uniqueV:
        uniqueV.append(value)
#Now identified unique books and put them on a list
print('Unique values are')
print(uniqueV)
print()

encoding_map = {}
for i, category in enumerate(uniqueV):
    encoding_map[category] = i
#Made the mapping for unique values

encoded_column = []
for value in frame['Book']:
    encoded_column.append(encoding_map[value])
#Created new column of encoded values

frame['Book Code'] = encoded_column
#Added that column to original dataframe

print("Ordinal Encoded Data:")
print(frame)