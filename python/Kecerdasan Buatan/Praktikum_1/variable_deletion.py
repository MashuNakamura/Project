# Import Library
import pandas as pd 

# Membaca Data 
data = pd.read_csv('/media/ntfs/KULIAH/Semester 4/Kecerdasan/data.csv')

# Untuk menentukan data missing , contoh 20%
threshold = 0.2

# Kalau data yang hilang melebihi threshold (20%) maka akan di hapus
data = data[data.columns[data.isnull().mean() < threshold]]

data.to_csv('/media/ntfs/KULIAH/Semester 4/Kecerdasan/variable_deletion_cleaned.csv', index=False)
