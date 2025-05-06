import os

class AplikasiKuis:
    def __init__(self):
        self.user = ''
        self.nim = ''
        self.soal = []
        self.skor = []
        self.daftar_user = 'user.txt'
        self.nama_file_soal = 'soal_sederhana.txt'
        self.load_soal()

    def load_soal(self):
        if os.path.exists(self.nama_file_soal):
            with open(self.nama_file_soal, 'r') as file:
                for line in file:
                    data = line.strip().split(';')
                    if len(data) == 3:
                        soal = data[0]
                        opsi = data[1].split(',')
                        jawaban = data[2]
                        self.soal.append({'soal': soal, 'opsi': opsi, 'jawaban': jawaban})
    def load_user(self):
        if os.path.exists(self.daftar_user):
            with open(self.daftar_user, 'r') as file:
                for line in file:
                    data = line.strip().split(';')
                    if len(data) == 3:
                        nama = data[0]
                        nim = data[1]
                        skor = data[2]
                        self.soal.append({'nama': nama, 'nim': nim, 'skor': skor})

    def welcome(self):
        self.clear()

    def halaman_nama(self):
        nama = input('Masukkan Nama anda: ')
        nim = input('Masukkan NIM anda: ')
        self.daftar_user.append({'nama': nama, 'nim': nim, 'skor': 0})
        for user_info in self.daftar_user:
            print(f"Halo Selamat Datang Nama: {user_info['nama']} dengan NIM: {user_info['nim']}")

    def tambah_soal(self):
        cek_admin = input('Masukkan PIN untuk verifikasi Anda adalah Admin: ')
        if cek_admin == '8909':
            print('Selamat Datang Admin!')
            while True:
                menu_admin = input('Pilih menu untuk admin: \n 1. Cek Soal \n 2. Tambah Soal \n 3. Lihat Leaderboard \n 4. Keluar \n Menu yang dipilih: ')
                if menu_admin == '1':
                    print(self.soal)
                elif menu_admin == '2':
                    while True:
                        tambah_soal = input('Masukkan Soal: ')
                        opsi_str = input('Masukkan Opsi Jawaban (pisahkan dengan koma): ')
                        jawaban = input('Masukkan Opsi Jawaban yang benar: ')
                        self.save_soal(tambah_soal, opsi_str, jawaban)
                        print('Soal berhasil ditambahkan!')
                        konfirmasi_tambah_soal = input('Ingin tambah soal lagi? (ya/tidak)').lower()
                        if konfirmasi_tambah_soal != 'ya':
                            break
                elif menu_admin == '3':
                    print('Fitur Dashboard belum Diimplementasikan')
                    break
                elif menu_admin == '4':
                    print('Terimakasih, Sampai jumpa di lain kesempatan!')
                    break
                else:
                    print('Menu tidak ada. Silahkan pilih sesuai yang tersedia.')
        else:
            print('PIN anda salah. Akses ditolak!')

    def save_soal(self, soal, opsi_str, jawaban):
        with open(self.nama_file_soal, 'a') as file:
            file.write(f"{soal};{opsi_str};{jawaban}\n")
            self.soal.append({'soal': soal, 'opsi': opsi_str.split(','), 'jawaban': jawaban})

    def mulai_kuis(self):
        if self.daftar_user:
            current_user = self.daftar_user[-1]
            print(f"Anda akan mengerjakan Kuis sebagai {current_user['nama']} dengan NIM {current_user['nim']}")
            for i, item in enumerate(self.soal):
                print(f"Pertanyaan {i + 1}: {item['soal']}")
                for j, opsi in enumerate(item['opsi']):
                    print(f"{j + 1}. {opsi}")
                jawaban = input("Masukkan jawaban (nomor): ")
                if jawaban == item['jawaban']:
                    print("Jawaban benar!")
                    current_user['skor'] += 1
                else:
                    print("Jawaban salah!")
            print(f"Skor akhir Anda: {current_user['skor']}")
        else:
            print("Belum ada pengguna yang terdaftar.")
    
    def cari_mahasiswa(self):
        cari = input('Masukkan NIM yang ingin dicari: ')
        for user in self.daftar_user:
            if user['nim'] == cari:
                print(f"Nama: {user['nama']}, NIM: {user['nim']}, Skor: {user['skor']}")
                return
        print("Mahasiswa tidak ditemukan.")

kuis_app = AplikasiKuis()
#kuis_app.halaman_nama()
#kuis_app.tambah_soal()
#kuis_app.mulai_kuis()
kuis_app.cari_mahasiswa()