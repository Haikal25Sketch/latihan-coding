class item:
    def __init__(self,nama,harga):
        self.nama = nama
        self.harga = harga

class keranjang:
    def __init__(self):
        self.items =[]
        self.awal = 0
    def tambah_barang(self,*item):
        for barang in item:
            self.items.append(barang)
            print (f"{barang.nama} berhasil dimasukkan ke keranjang")
    def __str__(self):
        info = ""
        for barang in self.items:
            info += f"{barang.nama}:{barang.harga}\n"
        return info
    def hitung_total(self):
        total = 0
        for item in self.items:
            total+= item.harga
        print ("Total belanjaannya adalah : ",total)
keranjang1 = keranjang()
keranjang1.tambah_barang(item("Beras",10000),item("Minyak",7000))
keranjang1.hitung_total()
print (keranjang1)

"""ERROR DESIGN"""
class BioskopError(Exception):
    pass

class Umur_tidak_cukup(BioskopError):
    def __init__(self,umur,umur_min):
        self.umur = umur
        self.umur_min = umur_min
        super().__init__(f"Umur anda {self.umur} tahun, tidak boleh masuk ")

class Kursi_penuh(BioskopError):
    def __init__(self,no_kursi):
        self.no_kursi = no_kursi
        super().__init__(f"Kursi dengan nomer {self.no_kursi} sudah penuh")



class Bioskop:
    kursi= set()
    def __init__(self,nama):
        self.nama = nama
        self.umur_min =17
        print (f"HAI {self.nama.upper()},SELAMAT DATANG DI BIOSKOP KAMI.")

    def pesan_tiket(self,umur,no_kursi):
        if umur < self.umur_min:
            raise Umur_tidak_cukup(umur,self.umur_min)
        if no_kursi in Bioskop.kursi:
            raise Kursi_penuh(no_kursi)
        Bioskop.kursi.add(no_kursi)
        print ("SELAMAT MENIKMATI FILM KAMI.")

try:
    bioskop1 = Bioskop("HuTao")
    bioskop1.pesan_tiket(12,5)
except Exception as e:
    print (e)
print()
try:
    bioskop2 = Bioskop("Citlali")
    bioskop2.pesan_tiket(19,5)
except Exception as e:
    print (e)
print()
try:
    bioskop3 = Bioskop("Nahida")
    bioskop3.pesan_tiket(18,5)
except Exception as e:
    print (e)
class KoneksiBankError(Exception):
    pass

class TransaksiGagal(Exception):
    pass

def proses_bank():
    raise KoneksiBankError("Server sedang terputus sementara")

def bayar_belanjaan():
    try:
        proses_bank()

    except KoneksiBankError as e:
        print (e.__cause__)
        raise TransaksiGagal("Transaksi untuk sementara waktu tidak bisa dilakukan") from e

try:
    bayar_belanjaan()

except TransaksiGagal as e:
    print ("Error : ",e)
    print ("Penyebab :",e.__cause__)
