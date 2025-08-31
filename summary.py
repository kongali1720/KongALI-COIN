import matplotlib.pyplot as plt

# Hitung jumlah sukses dan gagal
status_counts = df['Status'].value_counts()

# Grafik batang status transaksi
plt.figure(figsize=(6,4))
status_counts.plot(kind='bar', color=['green', 'red'])
plt.title("Jumlah Transaksi Sukses vs Gagal")
plt.ylabel("Jumlah")
plt.savefig("status_transaksi.png")
plt.close()

# Pie chart Value transaksi
plt.figure(figsize=(6,6))
df['Value_ETH'].plot(kind='pie', labels=df['Status'], autopct='%1.1f%%', startangle=90)
plt.title("Distribusi Value Transaksi (ETH)")
plt.ylabel("")
plt.savefig("value_transaksi.png")
plt.close()
