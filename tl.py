import requests

print(" [+]  Author    : Rianda Fuad Shafly")
print(" [+]  Info      : Data Covid Indonesia")
print(" [+]  Website   : www.riandafuadshafly.my.id")
print(" [+]  Contact   : bangrianda456@gmail.com")
print(" ---------------------------------------------")
teks = input(" [?] Masukkan Teks : ")
def main(hoho):
     url = "https://raden-gozal.herokuapp.com/api/translate?kata={}&apikey=zahirgans".format(teks)
     data = requests.get(url).json()
     arti = data['result']['text']
     print(" [-] Artinya       : " + arti)
     
main(teks)
