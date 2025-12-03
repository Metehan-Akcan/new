# Temel veri analizi başlangıç şablonu

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Grafiklerin not defterinde gözüksün (Jupyter için, terminalden çalıştırıyorsan gerek yok)
# %matplotlib inline

# 1. Veri setini yükle
# Aynı klasöre "data.csv" koyduğunu varsayıyoruz
# Örnek bir CSV yapısı:
#   sepal_length,sepal_width,petal_length,petal_width,species
#   5.1,3.5,1.4,0.2,setosa
try:
    df = pd.read_csv("data.csv")
    print("Veri başarıyla yüklendi!")
except FileNotFoundError:
    print("data.csv bulunamadı. Aynı klasöre data.csv dosyası koymayı unutma.")
    df = pd.DataFrame()

# 2. İlk birkaç satırı göster
if not df.empty:
    print("\nİlk 5 satır:")
    print(df.head())

    # 3. Temel istatistikler
    print("\nTemel istatistikler:")
    print(df.describe())

    # 4. Eksik değer kontrolü
    print("\nEksik değer sayıları:")
    print(df.isnull().sum())

    # 5. Basit bir histogram (ilk sayısal sütun için)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        first_col = numeric_cols[0]
        plt.figure(figsize=(8, 4))
        df[first_col].hist(bins=20)
        plt.title(f"{first_col} için histogram")
        plt.xlabel(first_col)
        plt.ylabel("Frekans")
        plt.tight_layout()
        plt.show()
    else:
        print("Sayısal sütun bulunamadı, grafik çizilemiyor.")
else:
    print("DataFrame boş, analiz yapılamıyor.")
