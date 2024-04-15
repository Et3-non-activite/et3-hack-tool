import subprocess

giriş1 = int(input("1.Sistem Güncelleştirmek\n2.Sistem Paket Yükseltmek\n3.Tüm Paketleri Yükseltmek\nLütfen yapmak istediğiniz işlemi seçiniz: "))

if giriş1 == 1:
    subprocess.call(["sudo", "apt-get", "update", "-y"])
elif giriş1 == 2:
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
elif giriş1 == 3:
    subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"])
else:
    print("Geçersiz seçenek! Lütfen geçerli bir seçenek girin.")
