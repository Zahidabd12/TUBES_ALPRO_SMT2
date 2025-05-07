import os

class AplikasiKuis:
    def __init__(self):
        self.user = ''
        self.nim = ''
        self.soal = []
        self.skor = []
        self.daftar_user_file = 'user.txt'
        self.daftar_user = []
        self.nama_file_soal = 'soal_sederhana.txt'
        self.load_soal()
        self.load_user()

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
        if os.path.exists(self.daftar_user_file):
            with open(self.daftar_user_file, 'r') as file:
                self.daftar_user = []
                for line in file:
                    data = line.strip().split(';')
                    if len(data) == 3:
                        nama = data[0]
                        nim = data[1]
                        skor = int(data[2])
                        self.daftar_user.append({'nama': nama, 'nim': nim, 'skor': skor})
        else:
            self.daftar_user = []

    def save_user(self):
        with open(self.daftar_user_file, 'w') as file:
            for user in self.daftar_user:
                file.write(f"{user['nama']};{user['nim']};{user['skor']}\n")

    def welcome(self):
        self.clear()

    def halaman_nama(self):
        nama = input('Masukkan Nama anda: ')
        nim = input('Masukkan NIM anda: ')
        user_baru = {'nama': nama, 'nim': nim, 'skor': 0}
        self.daftar_user.append(user_baru)
        self.save_user()
        print(f"Halo Selamat Datang Nama: {user_baru['nama']} dengan NIM: {user_baru['nim']}")

    def tambah_soal(self):
        cek_admin = input('Masukkan PIN untuk verifikasi Anda adalah Admin: ')
        if cek_admin == '8909':
            print('Selamat Datang Admin!')
            while True:
                menu_admin = input('Pilih menu untuk admin: \n 1. Cek Soal \n 2. Tambah Soal \n 3. Lihat Leaderboard \n 4. Cari User \n 5. Keluar \n Menu yang dipilih: ')
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
                    self.tampilkan_leaderboard()
                elif menu_admin == '4':
                    self.menu_cari_user()
                elif menu_admin == '5':
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
            self.save_user()
            print(f"Skor akhir Anda: {current_user['skor']}")
        else:
            print("Belum ada pengguna yang terdaftar.")

    def tampilkan_leaderboard(self):
        if not self.daftar_user:
            print("Leaderboard masih kosong.")
            return
        leaderboard = sorted(self.daftar_user, key=lambda user: user['skor'], reverse=True)
        print("\n===== Leaderboard =====")
        for i, user in enumerate(leaderboard):
            print(f"{i + 1}. Nama: {user['nama']}, Skor: {user['skor']}, NIM: {user['nim']}")
        print("======================\n")

    def cari_user_sequential(self, nama_cari):
        hasil_pencarian = []
        for user in self.daftar_user:
            if user['nama'].lower() == nama_cari.lower():
                hasil_pencarian.append(user)
        return hasil_pencarian

    def cari_user_binary(self, nama_cari):
        self.daftar_user.sort(key=lambda user: user['nama'].lower())
        low = 0
        high = len(self.daftar_user) - 1
        hasil_pencarian = []

        while low <= high:
            mid = (low + high) // 2
            nama_tengah = self.daftar_user[mid]['nama'].lower()
            if nama_tengah < nama_cari.lower():
                low = mid + 1
            elif nama_tengah > nama_cari.lower():
                high = mid - 1
            else:
                index = mid
                while index >= 0 and self.daftar_user[index]['nama'].lower() == nama_cari.lower():
                    hasil_pencarian.append(self.daftar_user[index])
                    index -= 1
                index = mid + 1
                while index < len(self.daftar_user) and self.daftar_user[index]['nama'].lower() == nama_cari.lower():
                    hasil_pencarian.append(self.daftar_user[index])
                    index += 1
                return hasil_pencarian 

        return hasil_pencarian

    def menu_cari_user(self):
        print("\n===== Cari User =====")
        nama_cari = input("Masukkan nama user yang ingin dicari: ")

        hasil_sequential = self.cari_user_sequential(nama_cari)
        print("\n--- Hasil Pencarian Sequential ---")
        if hasil_sequential:
            for user in hasil_sequential:
                print(f"Nama: {user['nama']}, NIM: {user['nim']}, Skor: {user['skor']}")
        else:
            print(f"Tidak ada user dengan nama '{nama_cari}' ditemukan.")

        self.daftar_user.sort(key=lambda user: user['nama'].lower())
        hasil_binary = self.cari_user_binary(nama_cari)
        print("\n--- Hasil Pencarian Binary ---")
        if hasil_binary:
            for user in hasil_binary:
                print(f"Nama: {user['nama']}, NIM: {user['nim']}, Skor: {user['skor']}")
        else:
            print(f"Tidak ada user dengan nama '{nama_cari}' ditemukan (Binary Search).")
        print("=====================\n")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

kuis_app = AplikasiKuis()
# kuis_app.halaman_nama()
# kuis_app.mulai_kuis()
kuis_app.tambah_soal() 
# kuis_app.cari_mahasiswa() 