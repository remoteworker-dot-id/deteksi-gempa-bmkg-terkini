import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 10 Januari 2022
    Waktu: 04:59:07 WIB
    Magnitudo: 5.5
    Kedalaman: 10 km
    Lokasi: LU=1.49, BT=127.85
    Pusat Gempa: Pusat gempa berada di darat 5 km barat daya Halmahera Utara
    Dirasakan: Dirasakan (Skala MMI): IV Tobelo, III-IV Sofifi, III-IV Galela, II-III Morotai
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitude = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None
        for res in result:
            if i == 1:
                magnitude = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i += 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitude'] = magnitude
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return

    print('\nGempabumi terkini menurut BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitude']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Pusat: {result['lokasi']}")
    print(f"Dirasakan: {result['dirasakan']}")

if __name__ == '__main__':
    print('Masih ada bug yang disengaja untuk pembelajaran')
