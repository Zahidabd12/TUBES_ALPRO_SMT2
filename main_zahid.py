class AplikasiKuis:
  def __init__(self):
    self.user = ''
    self.nim = ''
    self.soal = []
    self.skor = []
    self.daftar_user = []
  
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
          tambah_soal = input('Masukkan Soal: ')
          opsi = input('Masukkan Opsi Jawabannya (pisahkan melalui spasi)! :')
          opsi_split = opsi.split()
          jawaban = input('Masukkan Opsi Jawaban yang benar: ')
          self.soal.append({'soal': tambah_soal, 'opsi': opsi_split, 'jawaban': jawaban})
          print('Soal berhasil ditambahkan!')
          konfirmasi_tambah_soal = input('Ingin tambah soal lagi? (ya/tidak)').lower()
          if konfirmasi_tambah_soal != 'ya':
            continue
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
        
  def mulai_kuis(self):
    if self.daftar_user:
      current_user = self.daftar_user[-1]
      print(f"Anda akan mengerjakan Kuis sebagai {current_user['nama']} dengan NIM {current_user['nim']}")
    else:
      print("Belum ada pengguna yang terdaftar.")

kuis_app = AplikasiKuis()
kuis_app.halaman_nama()
#kuis_app.tambah_soal()
kuis_app.mulai_kuis()