from sklearn.preprocessing import StandardScaler
import numpy as np

# 4 sampel/observasi dengan 2 fitur/variabel
data = np.array([[4, 1], [11, 1], [10, 4], [1, 11]])

# Membuat objek scaler
scaler = StandardScaler()

# Melatih dan mentransformasi data
scaled_data = scaler.fit_transform(data)

print(scaled_data)
