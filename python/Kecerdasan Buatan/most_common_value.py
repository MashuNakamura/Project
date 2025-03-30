# Import Library
import pandas as pd 

# Membaca Data 
data = pd.read_csv('/media/ntfs/KULIAH/Semester 4/Kecerdasan/data.csv')

# Mengisi nilai yang hilang dengan nilai yang paling sering muncul dalam kolom tertentu
data['Department'] = data['Department'].fillna(data['Department'].value_counts().idxmax())

# Menyimpan hasil ke CSV
data.to_csv('/media/ntfs/KULIAH/Semester 4/Kecerdasan/most_common_value_cleaned.csv', index=False)
