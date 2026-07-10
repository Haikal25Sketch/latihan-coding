import os
import requests
from dotenv import load_dotenv
# Skenario A
response_A = requests.get("https://httpbingo.org/post") #Method not allowed karena dia mau mengambil data(GET) dari laci post(Tempat dimana kitamenyimpan data)
#print("Status A:", response_A.status_code)

# Skenario B
data_user = {"nama": "Haikal", "peran": "AI Engineer"}
response_B = requests.post("https://httpbingo.org/post", json=data_user)
data_dict = response_B.json()
#print("Status B:", response_B.status_code)
#print("Nama yang dikirim:", data_dict["json"]["nama"])

print()

url = "https://httpbingo.org/post"
data ={"Nama proyek": "Asisten pintar", "versi":1.0 ,"status":"Development"}
response_C = requests.post(url,json=data)
#print ("Status respone_C adalah ",response_C.status_code)
json = response_C.json()
#print ("Proyek sudah didaftarkan : ",json["json"]["Nama proyek"]) # json disini adalah yang ada di dalam response_C.json


print()

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
headers = {
    "Authorization": f"token {token}"
}

url ="https://api.github.com/user/repos"
response_d = requests.get (url,headers=headers,params={"page":1,"per_page":5})
data = response_d.json()
for repo in data:
    print ("Nama repo : ",repo["name"])


print()

headers = {
    "Authorization": f"token {token}"
}
def ambil_data_ai(url):
    try:
        response = requests.get(url,headers=headers,timeout=5)
        response.raise_for_status()
        print ("Status code response : ",response.status_code)
        for key,value in response.json().items():
            print (f"{key} : {value}")

    except requests.exceptions.ConnectionError:
        print ("Koneksi internet atau Url bermasalah")
    except requests.exceptions.HTTPError as e:
        print ("Server menolak,ada masalah HTTP")
    except requests.exceptions.RequestException as e:
        print ("Terjadi error misterius dalam requests")

ambil= ambil_data_ai
ambil("https://api.github.com/user")
