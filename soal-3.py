import requests

# API Key = ef3b082b17fe409c94c8189b9758f916

print('Selamat datang, mau tahu berita apa hari ini?\n')
print('[1] Berita seputar teknologi\n[2] Berita seputar bisnis\n[3] Berita seputar olahraga\n[4] Berita seputar kesehatan\n[5] Berita seputar sains\n')

choice = input('Ketik pilihan Anda [1/2/3/4/5] : ')

urlTech = 'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=ef3b082b17fe409c94c8189b9758f916'
urlBusiness = 'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=ef3b082b17fe409c94c8189b9758f916'
urlSport = 'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=ef3b082b17fe409c94c8189b9758f916'
urlHealth = 'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=ef3b082b17fe409c94c8189b9758f916'
urlScience = 'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=ef3b082b17fe409c94c8189b9758f916'

if choice.isdigit():
    choice = int(choice)
    if choice == 1:
        print('Berikut adalah top 5 berita Indonesia bidang teknologi : ')
        newsTech = requests.get(urlTech)
        for i in range(0, 5):
            print(i + 1, '-', newsTech.json()['articles'][i]['title'])
    elif choice == 2:
        print('Berikut adalah top 5 berita Indonesia bidang bisnis : ')
        newsBusiness = requests.get(urlBusiness)
        for i in range(0, 5):
            print(i + 1, '-', newsBusiness.json()['articles'][i]['title'])
    elif choice == 3:
        print('Berikut adalah top 5 berita Indonesia bidang olahraga : ')
        newsSport = requests.get(urlSport)
        for i in range(0, 5):
            print(i + 1, '-', newsSport.json()['articles'][i]['title'])
    elif choice == 4:
        print('Berikut adalah top 5 berita Indonesia bidang kesehatan : ')
        newsHealth = requests.get(urlHealth)
        for i in range(0, 5):
            print(i + 1, '-', newsHealth.json()['articles'][i]['title'])
    elif choice == 5:
        print('Berikut adalah top 5 berita Indonesia bidang sains : ')
        newsScience = requests.get(urlScience)
        for i in range(0, 5):
            print(i + 1, '-', newsScience.json()['articles'][i]['title'])
    else:
        print('Pilihan yang Anda masukkan salah. Harap input kembali.')
else:
    print('Harap masukkan hanya angka.')