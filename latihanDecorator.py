def butuh_admin(func):
    def bungkus(*args,**kwargs):
        pemilik = "ADMIN"
        print (f"{'='*5} SELAMAT DATANG {'='*5}")
        if args[0].upper() != pemilik:
            print (f"ANDA BUKAN {pemilik},AKSES DITOLAK")
        else:
            func(*args,**kwargs)
    return bungkus
@butuh_admin
def buka_data_rahasia(role):
    print ("ADMIN DATANG,SEMUA HARUS TUNDUK!!!")
    return role


buka_data_rahasia("admin")

print()



def simpan_cache(func):
    cache ={}
    def wrapper(n):
        if n not in cache:
            hasil = func(n)
            cache[n] = hasil
        else:
            hasil =cache[n]
            print ("[CACHE]MENGAMBIL DARI CACHE!!")
        return hasil
    return wrapper

@simpan_cache
def hitung_kuadrat(n):
    return n*n
print (hitung_kuadrat(2))
print (hitung_kuadrat(2))
print (hitung_kuadrat(298))
print (hitung_kuadrat(298))
print()

def jadikan_bold(func):
    def wrapper(text):
        if not isinstance(text,str):
            raise ValueError("Tipe Data harus Str")
        hasil =f"<b> {text} </b> "
        return hasil
    return wrapper

@jadikan_bold
def get_username(nama):
    return nama

print (get_username("TUNDUKLAH KEPADA SANG PENGUASA KEGELAPAN"))

def batasi_maksimal(angka_maksimal): # Lapis 1: Ambil angka 100
    def decorator(func):             # Lapis 2: Ambil fungsi set_volume
        def wrapper(level):          # Lapis 3: Ambil parameter fungsi asli (level)
            if level > angka_maksimal:
                level = angka_maksimal
            return func(level)       # Jalankan fungsi asli dengan level yang sudah dibatasi
        return wrapper
    return decorator

@batasi_maksimal(100)
def set_volume(level):
    print(f"Volume diatur ke: {level}")

set_volume(150) # Output: Volume diatur ke: 100
