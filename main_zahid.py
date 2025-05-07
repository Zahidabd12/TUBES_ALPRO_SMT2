import os
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

class AplikasiKuis: # Kelas logika aplikasi (seperti yang sudah kita buat sebelumnya)
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

class AplikasiKuisGUI: # Kelas untuk GUI
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Kuis")
        self.style = ttk.Style(theme="flatly") # Pilih tema yang menarik
        self.kuis_app = AplikasiKuis() # Membuat instance dari kelas logika
        self.current_question_index = 0
        self.user_answer = tk.StringVar()
        self.current_user = None # Untuk menyimpan informasi user yang sedang aktif

        self.show_login_page()

    def show_login_page(self):
        self.clear_frame()
        login_frame = ttk.Frame(self.master, padding=20)
        login_frame.pack(fill="both", expand=True)

        ttk.Label(login_frame, text="Selamat Datang di Aplikasi Kuis!", font=("Arial", 16)).pack(pady=10)

        ttk.Label(login_frame, text="Nama:").pack(pady=5)
        self.nama_entry = ttk.Entry(login_frame)
        self.nama_entry.pack(pady=5)

        ttk.Label(login_frame, text="NIM:").pack(pady=5)
        self.nim_entry = ttk.Entry(login_frame)
        self.nim_entry.pack(pady=5)

        ttk.Button(login_frame, text="Mulai Kuis", command=self.start_quiz).pack(pady=15)

    def start_quiz(self):
        nama = self.nama_entry.get()
        nim = self.nim_entry.get()
        if nama and nim:
            self.current_user = {'nama': nama, 'nim': nim, 'skor': 0}
            self.kuis_app.daftar_user.append(self.current_user)
            self.kuis_app.save_user() # Simpan user baru
            self.show_quiz_page()
        else:
            messagebox.showerror("Error", "Nama dan NIM harus diisi.")

    def show_quiz_page(self):
        if not self.kuis_app.soal:
            messagebox.showinfo("Info", "Soal kuis belum tersedia.")
            return

        self.clear_frame()
        quiz_frame = ttk.Frame(self.master, padding=20)
        quiz_frame.pack(fill="both", expand=True)

        self.question_label = ttk.Label(quiz_frame, text="", font=("Arial", 12), wraplength=400)
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for i in range(4): # Asumsi maksimal 4 opsi
            radio_button = ttk.Radiobutton(quiz_frame, text="", variable=self.user_answer, value=str(i + 1))
            self.radio_buttons.append(radio_button)
            radio_button.pack(anchor="w", pady=5)

        ttk.Button(quiz_frame, text="Jawab", command=self.check_answer).pack(pady=15)
        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.kuis_app.soal):
            current_soal = self.kuis_app.soal[self.current_question_index]
            self.question_label.config(text=f"Pertanyaan {self.current_question_index + 1}: {current_soal['soal']}")
            options = current_soal['opsi']
            for i, button in enumerate(self.radio_buttons):
                if i < len(options):
                    button.config(text=options[i], state="normal")
                else:
                    button.config(text="", state="disabled") # Menonaktifkan opsi yang tidak ada
            self.user_answer.set(None) # Reset pilihan jawaban
        else:
            self.show_result_page()

    def check_answer(self):
        if self.user_answer.get():
            current_soal = self.kuis_app.soal[self.current_question_index]
            jawaban_user = self.user_answer.get()
            jawaban_benar_index = -1
            for i, opsi in enumerate(current_soal['opsi']):
                if opsi == current_soal['jawaban']:
                    jawaban_benar_index = i + 1
                    break

            if jawaban_user == str(jawaban_benar_index):
                messagebox.showinfo("Benar", "Jawaban Anda benar!")
                if self.current_user:
                    self.current_user['skor'] += 1
            else:
                messagebox.showerror("Salah", f"Jawaban Anda salah. Jawaban yang benar adalah: {current_soal['jawaban']}")

            self.current_question_index += 1
            self.load_question()
        else:
            messagebox.showwarning("Peringatan", "Silakan pilih jawaban terlebih dahulu.")

    def show_result_page(self):
        self.clear_frame()
        result_frame = ttk.Frame(self.master, padding=20)
        result_frame.pack(fill="both", expand=True)

        ttk.Label(result_frame, text="Hasil Kuis", font=("Arial", 16)).pack(pady=10)
        if self.current_user:
            ttk.Label(result_frame, text=f"Nama: {self.current_user['nama']}", font=("Arial", 12)).pack(pady=5)
            ttk.Label(result_frame, text=f"NIM: {self.current_user['nim']}", font=("Arial", 12)).pack(pady=5)
            ttk.Label(result_frame, text=f"Skor Anda: {self.current_user['skor']} / {len(self.kuis_app.soal)}", font=("Arial", 12, "bold")).pack(pady=10)

        ttk.Button(result_frame, text="Kembali ke Menu Login", command=self.show_login_page).pack(pady=15)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    app = AplikasiKuisGUI(root)
    root.mainloop()