import requests

# kelimeler listesi
keywords = []

# dizinler.txt dosyasını oku
with open("common.txt", "r") as f:
  # her satırı oku
  for line in f:
    # satır sonundaki "\n" ifadesini sil
    keyword = line.strip()
    # kelimeyi listeye ekle
    keywords.append(keyword)

# her kelime için dizin yolunu oluşturun ve HTTP isteği gönderin
for keyword in keywords:
  directory_path = f"http://google.com/{keyword}"
  response = requests.get(directory_path)

  # durum kodunu kontrol edin
  if response.status_code == 200:
    # dizin yolunun var olduğunu doğruladık
    # dizin yolunun içeriğini inceleyin
    print(f"{directory_path}:")
    print(response.text)
  else:
    # dizin yolunun var olmadığını doğruladık
    print(f"{directory_path}: Dizin yolu bulunamadı")
