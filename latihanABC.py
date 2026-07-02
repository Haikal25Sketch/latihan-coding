from abc import ABC,abstractmethod

class storage(ABC):

    @abstractmethod
    def simpan(self,key,data):
        pass
    @abstractmethod
    def ambil(self,key):
        pass

class file(storage):
    def __init__(self):
        self.rak =[]

    def simpan(self,key,data):
        self.rak.append({"key":key,"data":data})
        return f"Data dengan key {key} berhasil ditambahkan"
    def ambil(self,key):
        for data in self.rak:
            if data["key"] == key:
                return data["data"]
            return None

f1 = file()
f1.simpan(12,"Hutao")
f1.ambil(12)

class pembayaran(ABC):

    @abstractmethod
    def bayar(self,jumlah):
        pass

class Bank(pembayaran):
    def __init__(self,rekening):
        self.rekening = rekening
    def bayar(self,jumlah):
        self.rekening.saldo -= jumlah

        print (f"[INFO][BANK]{self.rekening.nama} BERHASIL MELAKUKAN PEMBAYARAN {jumlah}")

class Ewallet(pembayaran):
    def __init__(self,rekening):
        self.rekening = rekening
    def bayar(self,jumlah):
        self.rekening.saldo-= jumlah
        print (f"[INFO][EWALLET]{self.rekening.nama} BERHASIL MELAKUKAN PEMBAYARAN {jumlah} ")


class rekening:
    def __init__(self,nama,saldo):
        self.nama = nama
        self.saldo = saldo
        if self.saldo == 0:
            print ("Saldo Habis")


class pesanan:
    def __init__(self,total_harga):
        self.total_harga = total_harga

    def pembayaran(self,transaksi):
        bayar = transaksi.bayar(self.total_harga)


class pembayaranfactory:
    mapping={
    "BANK" : Bank,
    "EWALLET":Ewallet
    }
    @staticmethod
    def create(jenis,rekening):
        jenis = jenis.upper()
        kelas_bayar = pembayaranfactory.mapping.get(jenis)
        if not kelas_bayar:
            raise ValueError("Jenis pembayaran tidak tersedia")
        return kelas_bayar(rekening)

rekening1 = rekening("Haikal",19000)
while True:
    try:
        jenis = input("Masukkan jenis pembayaran : ")
        total = int(input("Total bayar : "))
        if total >rekening1.saldo:
            raise ValueError("Saldo Kurang")

        pembayaran = pembayaranfactory.create(jenis,rekening1)
        bayar = pesanan(total)
        bayar.pembayaran(pembayaran)

        lanjut = input ("Lanjut atau berhenti (y/n) : ").upper()
        if lanjut == "N":
            print (f"[INFO] Saldo {rekening1.nama} tersisa {rekening1.saldo}")
            break
        else:
            continue
    except Exception as e:
        print ("Terjadi Error : ",e)
