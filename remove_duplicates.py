import pandas as pd

data = pd.read_excel('/Users/achaudhari/Desktop/Book Prediction New/Book2.xlsx')

#identify duplicate rows 
data.drop_duplicates(subset=['title','author'], inplace=True)

#creating a new excel sheet
data.to_excel('/Users/achaudhari/Desktop/Book Prediction New/duplicate_books.xlsx', index=False)