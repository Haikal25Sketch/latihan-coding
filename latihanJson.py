import json

class Buku_Fav:

    def __init__(self,nama,buku,tahun):
        self.nama = nama
        self.buku = buku
        self.tahun = tahun

    def save (self,location):
        data = {
        "Penulis":self.nama,
        "Judul Buku":self.buku,
        "Tahun Terbit":self.tahun
        }
        with open (location,"w") as f:
            json.dump(data,f,indent=4)
    def load(self,location):
        with open (location,"r") as f:
            data = json.load(f)
            self.nama = data["Penulis"]
            self.buku = data["Judul Buku"]
            self.tahun = data["Tahun Terbit"]

a = Buku_Fav("Henry Manampiring","Filosofi Teras",2019)
a.save("Buku.json")
a.nama = "Haikal"
print ("NAMA SEBELUM LOAD")
print (a.nama)
a.load("Buku.json")
print ("NAMA SESUDAH LOAD")
print (a.nama)

print()

class Mahasiswa:

    def __init__(self,nama,umur,jurusan):
        self.nama = nama
        self.umur= umur
        self.jurusan= jurusan

    def save (self,location):
        data = {
        "Nama":self.nama,
        "Umur":self.umur,
        "Jurusan":self.jurusan
        }
        with open (location,"w") as f:
            json.dump(data,f,indent=4)
    def load(self,location):
        with open (location,"r") as f:
            data = json.load(f)
            self.nama = data["Nama"]
            self.umur = data["Umur"]
            self.jurusan = data["Jurusan"]

b = Mahasiswa("HuTao",19,"Ekonomi")
b.save("Mahasiswa.json")
print ("NAMA SEBELUM LOAD")
b.nama = "YaeMiko"
print (b.nama)
b.load("Mahasiswa.json")
print ("NAMA SESUDAH LOAD")
print (b.nama)

print()

class DataSiswa:
    def __init__(self):
        self.database= []

    def tambah_siswa(self,nama,umur):
        self.database.append({"Nama":nama,"Umur":umur})

    def lihat_data(self):
        return self.database

    def save(self,location):
        data = self.database
        with open(location,"w") as file:
            json.dump(data,file,indent=4)

    def load_data(location):
        with open(location,"r") as file:
            data = json.load(file)
            self.database.append(data)

Db1 = DataSiswa()
Db1.tambah_siswa("HuTao",19)
print (Db1.lihat_data())
Db1.save("Database_Siswa.json")
Db1.tambah_siswa("Citlali",200)
Db1.tambah_siswa("YaeMiko",30)
Db1.tambah_siswa("Yelan",25)
Db1.tambah_siswa("Lumine",1000)
print (Db1.lihat_data())
Db1.save("Database_Siswa.json")

