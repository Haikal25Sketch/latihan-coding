class vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.__class__.__name__}{self.x,self.y}"

    def __repr__(self):
        return f"{self.__class__.__name__}(x ={self.x},y={self.y})"

    def _validate(self,other):
        if not isinstance(other,vector):
            raise ValueError(f"Hanya bisa dilakukan oleh objek {self.__class__.__name__}")
    def __add__(self,other):
        self._validate(other)
        return vector(self.x + other.x , self.y + other.y)

    def __eq__(self,other):
        self._validate(other)
        return self.x == other.x and self.y == other.y

a = vector(7,4)
b = vector(8,6)

print (a)
print (repr(a))
print (f"a + b adalah {a+b}")
print (f"apakah a dan b itu sama {a == b}")

print()

class toolbox:
    def __init__(self):
        self.alat = []
        print ("RAK ALAT SUDAH DIBUAT")
    def __len__(self):
        return len(self.alat)

    def add(self,*alat):
        for tool in alat:
            self.alat.append(tool)

    def __getitem__(self,index):
        return self.alat[index]

    def __setitem__(self,index,value):
        self.alat[index] = value

    def __str__(self):
        return f"Isi {self.__class__.__name__} : {','.join(self.alat)}"

tb = toolbox()
tb.add("gergaji","palu","tang")
print (f"Banyak alat yang ada di {tb.__class__.__name__} adalah {len(tb)}")
print (tb[0])
print (f"Nama alat di index ke 2 sebelum diubah {tb[2]}")
tb[2] = "Obeng"
print (f"Nama alat di index ke 2 setelah diubah {tb[2]}")
print (f"Panjang dari {tb.__class__.__name__ } adalah {len(tb)}")
print()

class setting:
    _singletone = None

    def __new__(cls,*args):
        print ("MEMBUAT OBJEK BARU DI __new__")
        if cls._singletone is None:
            print ("MEMBUAT OBJEK DENGAN ID BARU")
            cls._singletone = super().__new__(cls)
        else:
            print ("MEMBUAT OBJEK DENGAN ID LAMA")
        return cls._singletone

    def __init__(self,nama):
        print ("OBJEK SAMPAI KE __init__ ,SIAP DIINISIALISASI")
        self.nama = nama

    def __str__(self):
        return f"nama = {self.nama}"
a = setting("Setting1")
print (a)
print (f"ID DARI a ADALAH {id(a)}")
print()
b = setting("Setting2")
print (b)
print (f"ID DARI b ADALAH {id(b)}")

print()

class contextmanager:

    def __init__(self,nama):
        self.nama = nama

    def __enter__(self):
        print ("Koneksi ke database ",self.nama," dibuka")
        return "Connected"

    def __exit__(self,exc_type,exc_val,exc_tb):
        print ("Koneksi ke database ",self.nama," ditutup")
        print ("Error is ",exc_type)
        return False

with contextmanager("Haikal") as cm:
    print (cm)

class kelipatan:
    def __init__(self,angka,kelipatan):
        self.angka = angka
        self.kelipatan = kelipatan

    def __iter__(self):
        return kelipataniterator(self.angka,self.kelipatan)

class kelipataniterator:
    def __init__(self,angka,kelipatan):
        self.batas = 10
        self.angka = angka
        self.kelipatan = kelipatan
        self.posisi =0

    def __next__(self):
        if self.posisi >= self.batas:
            raise StopIteration
        value = self.angka
        self.angka += self.kelipatan
        self.posisi+=1
        return value

angka = kelipatan(5,3)
for b in angka:
    print (b)
