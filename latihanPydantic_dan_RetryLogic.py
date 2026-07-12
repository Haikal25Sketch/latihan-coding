from pydantic import BaseModel, Field,ValidationError
from typing import Optional
import requests
import time
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

def buat_session():
    session = requests.Session()
    retry = Retry(
        total = 5,
        backoff_factor = 2,
        status_forcelist = [429,500,503])

    adapter = HTTPAdapter(max_retries = retry)
    session.mount("https://",adapter)

    return session


class GithubUser(BaseModel):
    login: str
    id: int
    bio: Optional[str] = "Tidak ada bio"
    public_repos: int = Field(alias="public_repos")
    kelamin: str = "Tidak diketahui"


def ambil_user(username):
    session = buat_session()
    url =f"https://api.github.com/users/{username}"
    response = session.get(url)
    if response.status_code == 200:
        try:
            user = GithubUser(**response.json())
            print (f"LOGIN :{user.login} \nREPOS : {user.public_repos}\nBIO : {user.bio} ")
            return user

        except ValidationError as e:
            print ("DATA TIDAK SESUAI : ",e)
    return None

ambil_user("Haikal25Sketch")
print()

def cari_user(username):
    url = f"https://api.github.com/users/{username}"
    session2= buat_session()
    response2=session2.get(url)
    if response2.status_code == 200:
        try:
            user2 = GithubUser(**response2.json())
            print ("VALIDASI BERHASIL")
            return user2
        except ValidationError as e:
            print (f"DATA TIDAK VALID {e}")
            return None
    else:
        print ("USER TIDAK DITEMUKAN")

cari_user("Haikal25Sketch")

session3= buat_session()
response3= session3.get("https://mail.google.com")
print (response3.headers)
