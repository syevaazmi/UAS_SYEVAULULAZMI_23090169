import pandas as pd
data = [
    ["mahasiswa 1", 90, 80],
    ["mahasiswa 2", 50, 60],
    ["mahasiswa 3", 65, 70]
]


df = pd.DataFrame(data, columns=['Nama Mahasiswa', 'Algoritma dan struktur data 2', 'Matematika Numerik'])

print("Dataframe:")
print(df)

rata_nilai_matkul = df[['Algoritma dan struktur data 2', 'Matematika Numerik']].mean()
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(rata_nilai_matkul)

df['Rata-rata Nilai'] = df[['Algoritma dan struktur data 2', 'Matematika Numerik']].mean(axis=1)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(df[['Nama Mahasiswa', 'Rata-rata Nilai']])

