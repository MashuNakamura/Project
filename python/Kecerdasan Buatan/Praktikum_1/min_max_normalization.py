from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

# Object Array (Umur, Pengalaman, Gaji)
data = np.array([
    [25, 2, 5],  
    [30, 5, 10],  
    [35, 10, 20],  
    [40, 15, 35],  
    [45, 20, 50]
])

# Buat objek MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

# Lakukan scaling pada data
scaled_data = scaler.fit_transform(data)

# Tampilkan hasil dalam DataFrame agar lebih rapi
df_scaled = pd.DataFrame(scaled_data, columns=['Usia (scaled)', 'Pengalaman (scaled)', 'Gaji (scaled)'])
print(df_scaled)
