# Import Library
import pandas as pd 

# Membaca Data 
data = pd.read_csv('/media/ntfs/KULIAH/Semester 4/Kecerdasan/data.csv')

# Ubah data menjadi ke Numeric
numerical_cols = data.select_dtypes(include=['number']).columns
data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median())

data.to_csv('/media/ntfs/KULIAH/Semester 4/Kecerdasan/mean_or_median_cleaned.csv', index=False)
