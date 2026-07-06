#GENERATOR ADALAH FUNGSI YANG TERCIPTA KARENA ADANYA YIELD DIDALAMNYA
import time
import random
def sensor_stream_generator(limit=100):
    """
    Simulasi sensor yang mengirimkan data terus menerus.
    Alih-alih menyimpan 100 data di list, kita 'yield' satu per satu.
    """
    for i in range(limit):
        # Simulasi data suhu (antara 20.0 sampai 35.0 derajat)
        suhu = round(random.uniform(20.0, 35.0), 2)

        # 'yield' menghentikan fungsi sementara dan mengirimkan data ke luar
        yield {"id": i, "suhu": suhu, "timestamp": time.time()}


def anomali_detector_generator(raw_data):
    for suhu in raw_data:
        if suhu["suhu"] > 32.0:
            yield {"id":suhu["id"], "suhu":suhu["suhu"], "status":"ANOMALI"}


def run():
    print ("MEMULAI GENERATOR")
    data_mentah = sensor_stream_generator(limit =25)
    cleaner = anomali_detector_generator(data_mentah)

    jumlah = 0
    nomer=0
    for data in cleaner:
        jumlah+=1
        nomer+=1
        print (f"Memproses data ke {nomer}, suhu {data['suhu']}° diterima")
    if nomer >0:
        print (f"{'='*5} HASIL ANALISIS {'='*5}")
        print ("JUMLAH ANOMALI TERDETEKSI : ",jumlah)
run()
print()

def new_generator():
    while True:
        suhu = round(random.uniform(20.0,40.0),2)
        yield {"suhu":suhu}

def anomali_detector(raw_data):
    count = 0
    for data in raw_data :
        batas = 32
        if data["suhu"] > batas:
            count+=1
            yield {"id":count,"suhu":data["suhu"],"status":"ANOMALI"}



def run():
    print ("MEMULAI GENERATOR")
    jumlah = 3
    nomer = 0
    raw_data = new_generator()
    filter = anomali_detector(raw_data)

    for data in filter:
        nomer+=1
        print (f"MEMPROSES DATA KE {nomer},SUHU {data['suhu']}° DITERIMA")
        if nomer == jumlah:
            break
    print (f"{jumlah} DATA ANOMALI BERHASIL DIKUMPULKAN")
run()


