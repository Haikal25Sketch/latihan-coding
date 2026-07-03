"""PEMBALIK KATA"""
class Kata:
    def __init__(self,kata):
        self.kata = kata

    def __iter__(self):
        return pembalikkata(self.kata)

    def __str__(self):
        return self.kata

class pembalikkata:
    def __init__(self,kata):
        self.kata = kata
        self.batas = len(self.kata)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.batas < 0:
            raise StopIteration
        value = self.kata[self.batas]
        self.batas-=1
        return value
word = Kata("Haikal")
for kata in word:
    print (kata)

"""YIELD"""
def antrian_pagi(n):
    awal =1
    while awal <= n:
        yield f"Atrian ke {awal} dipagi hari"
        awal+=1

def antrian_vip(n):
    yield "Antrian VIP1"
    yield from antrian_pagi(n)
    yield "Antrian Tambahan!!!"

for antri in antrian_vip(9):
    print (antri)

print()
"""DESCRIPTOR"""
class Validasi_nilai:
    def __set_name__(self,owner,nilai):
        self.nilai = nilai
        print (owner)
        print (nilai)
        print (self)

    def __set__(self,instance,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Data Harus bertipe angka")
        if value >100 or value <0:
            raise ValueError("Nilai Harus 0-100")
        instance.__dict__[self.nilai] = value

    def __get__(self,instance,owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.nilai,"Data belum ada")

    def __delete__(self,instance):
        if self.nilai in instance.__dict__:
            del instance.__dict__[self.nilai]

class Siswa:
    nilai =Validasi_nilai()

    def __init__(self,nama,nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"{self.nama} : {self.nilai}"

siswa1 = Siswa("Budi",100)
print (siswa1.__dict__)
"""INHERITANCE DAN POLYMORPHISM"""

class Notifikasi:

    def kirim(self,pesan):
        raise NotImplementedError("PAKAI kirimnya()")

class EmailSender(Notifikasi):

    def __init__(self,tujuan):
        print ("PENGIRIM EMAIL DIBUAT")
        self.tujuan = tujuan
    def kirim(self,pesan):
        print (f"Mengirim Email ke {self.tujuan}. Isi pesan : {pesan}")

class TelegramSender(Notifikasi):

    def __init__(self,tujuan):
        print ("PENGIRIM TELEGRAM DIBUAT")
        self.tujuan = tujuan
    def kirim(self,pesan):
        print (f"Mengirim Telegram ke {self.tujuan}. Isi pesan : {pesan}")

tele = TelegramSender("HuTao")
email= EmailSender("Citlali")
email.kirim("Hai")
tele.kirim("Oha")
print()
def mesin_pesan(pengirim,pesan):
    for send in pengirim:
        send.kirim(pesan)
kirim = mesin_pesan([tele,email],"Hai,apakah kamu sehat?")
kirim

print()


class Sesi_kerja:

    def __init__(self,nama,jabatan):
        self.nama = nama
        self.jabatan = jabatan

    def __enter__(self):
        print (f"{self.nama} yang bekerja sebagai {self.jabatan} sedang bekerja")
        return "GANBATTEEEEEE"

    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type:
            print (f"Terjadi error {exc_type.__name__}: {exc_val}")
        else:
            print ("Sesi kerja selesai tanpa kendala!!!WAKTUNYA PULANG")
        return True
with Sesi_kerja("HuTao","Streamer") as sk:
    print (1/0)
