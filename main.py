"""
Aplikasi gempa terkini yang diambil dari bmkg.go.id
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi Gempa Terkini')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
