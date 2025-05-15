
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class KuisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill=BOTH, expand=True)

        self.soal = [
            {"pertanyaan": "Apa ibu kota Indonesia?", "pilihan": ["Jakarta", "Bandung", "Surabaya", "Medan"], "jawaban": "Jakarta"},
            {"pertanyaan": "Berapa hasil dari 5 + 7?", "pilihan": ["10", "11", "12", "13"], "jawaban": "12"},
            {"pertanyaan": "Siapa penemu lampu pijar?", "pilihan": ["Newton", "Einstein", "Edison", "Tesla"], "jawaban": "Edison"},
        ]

        self.index_soal = 0
        self.skor = 0
        self.nama = ""
        self.nim = ""

        self.menu_awal()

    def bersihkan_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def menu_awal(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Selamat Datang di Aplikasi Kuis", font=("Helvetica", 16, "bold")).pack(pady=30)
        ttk.Button(self.frame, text="Mulai Kuis", command=self.tampilan_login, bootstyle="success").pack(pady=10)
        ttk.Button(self.frame, text="Lihat Leaderboard", command=self.menu_leaderboard, bootstyle="info").pack(pady=10)
        ttk.Button(self.frame, text="Keluar", command=self.root.destroy, bootstyle="danger").pack(pady=10)

    def tampilan_login(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Masukkan Nama", font=("Helvetica", 12)).pack(pady=10)
        self.entry_nama = ttk.Entry(self.frame, font=("Helvetica", 12))
        self.entry_nama.pack()

        ttk.Label(self.frame, text="Masukkan NIM", font=("Helvetica", 12)).pack(pady=10)
        self.entry_nim = ttk.Entry(self.frame, font=("Helvetica", 12))
        self.entry_nim.pack()

        ttk.Button(self.frame, text="Mulai", command=self.mulai_kuis, bootstyle="primary").pack(pady=20)
        ttk.Button(self.frame, text="Kembali", command=self.menu_awal, bootstyle="secondary").pack(pady=5)

    def mulai_kuis(self):
        self.nama = self.entry_nama.get().strip()
        self.nim = self.entry_nim.get().strip()

        if not self.nama or not self.nim:
            messagebox.showwarning("Input Tidak Lengkap", "Nama dan NIM harus diisi.")
            return

        if not self.nim.isdigit():
            messagebox.showwarning("NIM Tidak Valid", "NIM harus berupa angka.")
            return

        self.index_soal = 0
        self.skor = 0
        self.tampilkan_soal()

    def tampilkan_soal(self):
        self.bersihkan_frame()

        soal = self.soal[self.index_soal]
        ttk.Label(self.frame, text=f"Soal {self.index_soal + 1} dari {len(self.soal)}", font=("Helvetica", 12, "bold")).pack(pady=10)
        ttk.Label(self.frame, text=soal["pertanyaan"], font=("Helvetica", 14)).pack(pady=10)

        self.jawaban_terpilih = tk.StringVar()

        for pilihan in soal["pilihan"]:
            ttk.Radiobutton(self.frame, text=pilihan, variable=self.jawaban_terpilih, value=pilihan).pack(anchor="w", padx=20, pady=5)

        ttk.Button(self.frame, text="Lanjut", command=self.periksa_jawaban, bootstyle="primary").pack(pady=20)

    def periksa_jawaban(self):
        jawaban = self.jawaban_terpilih.get()
        if not jawaban:
            messagebox.showwarning("Belum Pilih Jawaban", "Silakan pilih jawaban terlebih dahulu.")
            return

        if jawaban == self.soal[self.index_soal]["jawaban"]:
            self.skor += 1

        self.index_soal += 1
        if self.index_soal < len(self.soal):
            self.tampilkan_soal()
        else:
            self.tampilkan_hasil()

    def tampilkan_hasil(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Kuis Selesai!", font=("Helvetica", 16, "bold")).pack(pady=20)
        ttk.Label(self.frame, text=f"Skor Anda: {self.skor} dari {len(self.soal)}", font=("Helvetica", 14)).pack(pady=10)
        self.simpan_data_txt()
        ttk.Button(self.frame, text="Kembali ke Menu", command=self.menu_awal, bootstyle="secondary").pack(pady=10)
        ttk.Button(self.frame, text="Keluar", command=self.root.destroy, bootstyle="danger").pack(pady=5)

    def simpan_data_txt(self):
        baris = f"{self.nama}:{self.nim}:{self.skor}/{len(self.soal)}\n"
        try:
            with open("data.txt", "a") as f:
                f.write(baris)
        except Exception as e:
            messagebox.showerror("Gagal Menyimpan", f"Terjadi kesalahan saat menyimpan: {e}")

    def menu_leaderboard(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Leaderboard", font=("Helvetica", 16, "bold")).pack(pady=10)
        ttk.Button(self.frame, text="Lihat Semua Data", command=self.tampilkan_semua_data, bootstyle="primary").pack(pady=5)
        ttk.Button(self.frame, text="Urut data berdasarkan NIM", command=self.Insert_Nim, bootstyle="primary").pack(pady=5)
        ttk.Button(self.frame, text="Urut databerdasarkan Skor", command=self.Insert_Skor, bootstyle="info").pack(pady=5)
        ttk.Button(self.frame, text="Cari (Sequential Search)", command=self.cari_seq, bootstyle="info").pack(pady=5)
        ttk.Button(self.frame, text="Cari (Binary Search)", command=self.cari_bin, bootstyle="warning").pack(pady=5)
        ttk.Button(self.frame, text="Kembali", command=self.menu_awal, bootstyle="secondary").pack(pady=10)

    def tampilkan_semua_data(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Data Peserta", font=("Helvetica", 14, "bold")).pack(pady=10)
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    ttk.Label(self.frame, text=line.strip(), font=("Helvetica", 11)).pack(anchor="w")
        except FileNotFoundError:
            ttk.Label(self.frame, text="Belum ada data.", font=("Helvetica", 12)).pack()
        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary").pack(pady=10)

    def cari_seq(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Sequential Search", font=("Helvetica", 14, "bold")).pack(pady=10)
        entry = ttk.Entry(self.frame)
        entry.pack(pady=5)
        result = ttk.Label(self.frame, text="", font=("Helvetica", 11))
        result.pack(pady=5)

        def search():
            nama_dicari = entry.get().strip().lower()
            try:
                with open("data.txt", "r") as f:
                    for line in f:
                        if nama_dicari in line.lower():
                            result.config(text=f"Ditemukan: {line.strip()}")
                            return
                    result.config(text="Tidak ditemukan.")
            except FileNotFoundError:
                result.config(text="File data.txt tidak ditemukan.")

        ttk.Button(self.frame, text="Cari", command=search, bootstyle="info").pack(pady=5)
        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary").pack(pady=5)

    def cari_bin(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Binary Search (berdasarkan Nama)", font=("Helvetica", 14, "bold")).pack(pady=10)
        entry = ttk.Entry(self.frame)
        entry.pack(pady=5)
        result = ttk.Label(self.frame, text="", font=("Helvetica", 11))
        result.pack(pady=5)

        def search():
            nama_dicari = entry.get().strip().lower()
            try:
                with open("data.txt", "r") as f:
                    data = [line.strip() for line in f if ":" in line]
                    data.sort(key=lambda x: x.split(":")[0].lower())  # sort by nama
                    kiri, kanan = 0, len(data) - 1
                    while kiri <= kanan:
                        tengah = (kiri + kanan) // 2
                        nama_tengah = data[tengah].split(":")[0].lower()
                        if nama_dicari == nama_tengah:
                            result.config(text=f"Ditemukan: {data[tengah]}")
                            return
                        elif nama_dicari < nama_tengah:
                            kanan = tengah - 1
                        else:
                            kiri = tengah + 1
                    result.config(text="Tidak ditemukan.")
            except FileNotFoundError:
                result.config(text="File data.txt tidak ditemukan.")

        ttk.Button(self.frame, text="Cari", command=search, bootstyle="warning").pack(pady=5)
        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary").pack(pady=5)

    def Insert_Nim(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Data Diurutkan berdasarkan NIM (Insertion Sort)", font=("Helvetica", 14, "bold")).pack(pady=10)
        try:
            with open("data.txt", "r") as f:
                data = [line.strip() for line in f if ":" in line]
            for i in range(1, len(data)):
                key = data[i]
                key_nim = int(key.split(":")[1])
                j = i - 1
                while j >= 0 and int(data[j].split(":")[1]) > key_nim:
                    data[j + 1] = data[j]
                    j -= 1
                data[j + 1] = key
            for line in data:
                ttk.Label(self.frame, text=line, font=("Helvetica", 11)).pack(anchor="w")
        except FileNotFoundError:
            ttk.Label(self.frame, text="File ditemukan.", font=("Helvetica", 12)).pack()
        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary").pack(pady=10)

    def Insert_Skor(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Data Diurutkan berdasarkan Skor (Insertion Sort)", font=("Helvetica", 14, "bold")).pack(pady=10)

        try:
            with open("data.txt", "r") as f:
                data = [line.strip() for line in f if ":" in line]
            for i in range(1, len(data)):
                key = data[i]
                key_skor = int(key.split(":")[2].split("/")[0])
                j = i - 1
                while j >= 0 and int(data[j].split(":")[2].split("/")[0]) < key_skor:
                    data[j + 1] = data[j]
                    j -= 1
                data[j + 1] = key
            for line in data:
                ttk.Label(self.frame, text=line, font=("Helvetica", 11)).pack(anchor="w")
        except FileNotFoundError:
            ttk.Label(self.frame, text="File tidak ditemukan.", font=("Helvetica", 12)).pack()

        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary").pack(pady=10)

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    app = KuisApp(root)
    root.mainloop()
