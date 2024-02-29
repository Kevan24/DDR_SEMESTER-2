menu = {
    "Caffe Americano": 37000,
    "Caramel Macchiato": 59000,
    "Asian Dolce Latte": 55000,
    "Caramel Latte": 52000,
    "Vanilla Latte": 52000,
    "Caffe Latte": 48000,
    "Cappuccino": 48000,
    "Caffe Mocha": 55000,
}


def belanja():
    print("Selamat datang di caffe kepan!")
    print("Berikut adalah daftar minuman yang tersedia:")
    for minuman, harga in menu.items():
        print(f"{minuman}: Rp{harga} per cup")

    jumlah_transaksi = 0
    while True:
        minuman_dipilih = input(
            "Masukkan nama minuman yang ingin anda beli(atau 'selesai' untuk selesai)")
        if minuman_dipilih.lower() == 'selesai':
            break
        if minuman_dipilih not in menu:
            print("Maaf, minuman tersebut tidak tersedia")
            continue
        jumlah = float(
            input(f"Berapa cup {minuman_dipilih} yang anda inginkan?"))
        jumlah_transaksi += menu[minuman_dipilih] * jumlah

    if jumlah_transaksi > 350000:
        diskon = jumlah_transaksi * 0.15
        jumlah_transaksi -= diskon

    ppn = jumlah_transaksi * 0.10
    jumlah_transaksi += jumlah_transaksi * ppn
    print("Pajak:", ppn)

    print(f"total belanja anda adalah: Rp{jumlah_transaksi}")


belanja()
