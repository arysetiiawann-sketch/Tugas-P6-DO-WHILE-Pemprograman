print("PROGRAM PERULANGAN KELOMPOK 3 - ARY SETIAWAN & DAVIN WIRYANA A.")

while True:
    try: 
        jumlah_barang = int(input("Berapa banyak jenis barang? (minimal 1): "))
        if jumlah_barang > 0:
            break
        print("Minimal harus ada 1 barang ya!")
    except ValueError:
        print("Harus masukin angka bulat!")

print("\n2. Input Harga Tiap Barang")
total_bayar = 0
for i in range(1, jumlah_barang + 1):
    while True:
        try:
            input_harga = input(f"Harga barang ke-{i}: Rp ")
            harga_bersih = input_harga.replace(".", "").replace(",", ".")
            harga = float(harga_bersih)
            if harga >= 0:
                break
            print("Harga gak boleh minus!")
        except ValueError:
            print("Format angka salah, coba lagi.")
    total_bayar += harga

total_formatted = f"{total_bayar:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(f"\nTotal yang harus dibayar: Rp {total_formatted}")

print("\n3. Cetak Struk (While Loop)")
countdown = 3
while countdown > 0:
    print(f"Lagi nyetak struk dalam {countdown} detik...")
    countdown -= 1

print("Struk udah Keluar! Terima Kasih Banyak.")