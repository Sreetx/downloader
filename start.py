import os, time, sys, optparse, zipfile, socket, webbrowser 
try:
    from tqdm import tqdm
except: print('\n [!] Anda tidak memiliki module tqdm, module akan diinstall secara otomatis dalam 3 detik....');time.sleep(3);os.system('pip install tqdm');print('\n\a [+] Module tqdm berhasil di install. Harap jalankan kembali script ini\n');sys.exit()
try:
    import requests
except: print('\n [!] Anda tidak memiliki module requests, module akan diinstall secara otomatis dalam 3 detik....');time.sleep(3);os.system('pip install requests');print('\n\a [+] Module requests berhasil di install. Harap jalankan kembali script ini\n');sys.exit()

os.system('cls||clear')
banner = """
#----------------------------------------------------------------#
<|-----------------------| Night Eagle |------------------------|>
 | Author:             RX77E                                    |
 | Spesial Thank's:    RX77E                                    |
 | Github:             https://github.com/Sreetx                |
 | Instagram:          https://www.instagram.com/memelucubikin  |
<|--------------------------------------------------------------|>
#----------------------------------------------------------------#
"""

def bantuan():
    print(banner)
    print('''
python '''+sys.argv[0]+''' [OPTIONS/PERINTAH]
Perintah:
    --u --url         Gunakan ini untuk memasukkan url tujuan mengunduh suatu file
    --p --port        Gunakan ini untuk memasukkan port ketika menggunakan perintah --proxy (jika perlu)
    --px --proxy      Gunakan ini untuk memasukkan proxy login FTP(jika perlu)
    --d --directory   Gunakan ini untuk memasukkan directory tujuan menyimpan file
    --hh              Gunakan ini jika ingin meminta bantuan
    --user       Masukkan perintah ini ketika menggunakan perintah --proxy untuk memasukkan username FTP anda
    --passwd          Masukkan perintah ini ketika menggunakan perintah --proxy untuk memasukkan password login FTP anda
    --gc --gitclone   Gunakan ini untuk mengunduh file dari Github
    --tentang         Gunakan ini untuk meminta bantuan atau penjelasan tingkat lanjut

Contoh penggunaan:
    python '''+sys.argv[0]+''' --gitclone https://github.com/Sreetx/riddles
    python '''+sys.argv[0]+''' --url https://website.com/file.zip --directory /usr/root/document
    python '''+sys.argv[0]+''' --url https://website.com/file.zip --px 123.45.67 --port 443 --user contoh --passwd ngasalbro1234 --d /usr/root/document/hasil_download
    python '''+sys.argv[0]+''' --url https://website.com/file.zip --port 8080 --proxy 123.45.67 --user contoh --passwd ngasalbro1234 --directory /usr/root/document
    ''');sys.exit()

def proxy(passwd, prxy, port, ur):
    try:
        print(' [~] Menyiapkan proxy....')
        proksi = urllib.request.ProxyHandler({'http' : 'http://'+str(prxy)+':'+str(port)})
        logon = urllib.request.HTTPBasicAuthHandler()
        logon.add_password(user=str(ur), passwd=str(password))
        pembuka = urllib.request.build_opener(proxi, logon, urllib.request.CacheFTPHandler)
        urllib.request.install_opener(pembuka)
        print(' [+] Tersambung')
    except: print(' [!] Gagal menyiapkan proxy');sys.exit()
    
#Mengunduh
def download(link, penyimpanan):
    try:
        print(banner)
        print('\n [~] Menyiapkan file....')
        nama_file = link.split('/')[-1]
        print('\a [INFO] File yang akan diunduh: '+nama_file)
        r = requests.get(str(link), stream=True)
        total = int(r.headers.get('content-lenght', 0))
        with open(str(penyimpanan)+nama_file, 'wb') as file, tqdm(desc=' [~] '+nama_file, total=total, unit='b', unit_scale=True, unit_divisor=1024) as progres:
            for data in r.iter_content(chunk_size=1024):
                size = file.write(data)
                progres.update(size)
        print(' [+] Selesai. File disimpan dengan nama '+nama_file+'\n');sys.exit()
    except: print('\a\a\a [!] File yang akan diunduh tidak tersedia');sys.exit()
#GitClone
def kloning(clone):
    os.system('mkdir hasil')
    print(banner)
    print('\n [~] Menyiapkan file')
    gt = requests.get(str(clone)+'/archive/refs/heads/main.zip', stream=True)
    nama_file2 = clone.split('/')[-1]
    if gt.status_code == requests.codes.ok:
        print('\a [INFO] File yang akan diunduh: '+nama_file2)
        print(' [~] Mengunduh file....')
        fullsize = int(gt.headers.get('content-lenght', 0))
        with open('hasil/main.zip', 'wb') as file2, tqdm(desc=' [~] '+nama_file2+'.zip', total=fullsize, unit='b', unit_scale=True, unit_divisor=1024) as tunggu:
            for data2 in gt.iter_content(chunk_size=1024):
                ukuran = file2.write(data2)
                tunggu.update(ukuran)
        print('\a [+] File berhasil diunduh')
        print(' [~] Mengestrak file....')
        try:
            path = 'hasil/main.zip'
            f = zipfile.ZipFile(path)
            f.extractall('hasil',pwd=False)
            os.system('rm hasil/main.zip')
            print('\a [+] Berhasil, file disimpan pada directory "hasil"\n');sys.exit()
        except zipfile.BadZipFile: print('\a\a\a [!] File zip bermasalah!!! Pengekstrakan tidak dapat dilanjutkan. File akan segera dihapus\n');os.system('rm hasil/main.zip');sys.exit()
    else:
        print(' [~] Mengunduh file....')
        unduh = str(clone)+'/archive/refs/heads/master.zip'
        print('\a [INFO] File yang akan diunduh: '+nama_file2)
        gt2 = requests.get(unduh, stream=True)
        ukuranpenuh = int(gt2.headers.get('content-lenght', 0))
        with open('hasil/master.zip', 'wb') as file3, tqdm(desc=' [~] '+nama_file2+'.zip', total=ukuranpenuh, unit='b', unit_scale=True, unit_divisor=1024)as loading:
            for data3 in gt2.iter_content(chunk_size=1024):
                ukuran2 = file3.write(data3)
                loading.update(ukuran2)
        print('\a [+] File berhasil diunduh')
        print(' [~] Mengestrak file....')
        try:
            path2 = 'hasil/master.zip'
            s = zipfile.ZipFile(path2)
            s.extractall('hasil',pwd=False)
            os.system('rm hasil/master.zip')
            print('\a [+] Berhasil, file disimpan pada directory "hasil"\n');os.system('rm hasil/master.zip');sys.exit(1)
        except zipfile.BadZipFile: print('\a\a\a [!] File zip bermasalah!!! Pengekstrakan tidak dapat dilanjutkan. File akan segera dihapus\n');os.system('rm hasil/master.zip');sys.exit()

#Tentang
def ttg():
    print(banner)
    print('\n [~] Meminta bantuan tingkat lanjut....');time.sleep(2)
    print(' [~] Membuka browser....');time.sleep(1.5)
    webbrowser.open('https://postingan4ku.blogspot.com/2022/10/bantuanscriptnighteagle.html')
    print(' [+] Berhasil membuka browser\n');sys.exit()

menu = optparse.OptionParser('\n [?] Belum bisa menggunakan? Ketikan python '+sys.argv[0]+' --hh Untuk meminta bantuan\n')
menu.add_option('--url', dest='link')
menu.add_option('--tentang', dest='tentang', action='store_true', default=False)
menu.add_option('--p', '--port', dest='port')
menu.add_option('--px','--proxy', dest='prxy')
menu.add_option('--d','--directory', dest='penyimpanan')
menu.add_option('--gc','--gitclone', dest='clone')
menu.add_option('--user', dest='ur')
menu.add_option('--passwd', dest='password')
menu.add_option('--hh', dest='hlp', action='store_true', default=False)

(options, args) = menu.parse_args()
link = options.link
ur = options.ur
port = options.port
tentang = options.tentang
prxy = options.prxy
passwd = options.password
clone = options.clone
tentang = options.tentang
penyimpanan = options.penyimpanan
hlp = options.hlp
if link:
    try:
        socket.create_connection((socket.gethostbyname('google.com'), 80), 2)
    except: print(banner);print('\n [!] Periksa koneksi internet anda\n');sys.exit()
    if prxy:
        print(banner)
        proxy(passwd, prxy, port, ur)
    download(link, penyimpanan)
if clone:
    try:
        socket.create_connection((socket.gethostbyname('google.com'), 80), 2)
    except: print(banner);print(' [!] Periksa koneksi internet anda\n');sys.exit()
    kloning(clone)
if tentang:
    ttg()
if hlp:
    bantuan()
if penyimpanan:
    print(banner)
    print(' [!] Anda belum memasukkan input pada perintah --url\n');sys.exit()
if passwd:
    print(banner)
    print(' [!] Anda belum memasukkan input pada perintah --proxy\n');sys.exit()
if ur:
    print(banner)
    print(' [!] Anda belum memasukkan input pada perintah --proxy\n');sys.exit()
if prxy:
    print(banner)
    print(' [!] Anda belum memasukkan input pada perintah --url\n');sys.exit()
if port:
    print(parser)
    print(' [!] Anda belum memasukkan input pada perintah --proxy\n');sys.exit()
else:
    print(menu.usage)