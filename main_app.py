
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class KuisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis")
        self.root.geometry("800x800")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.configure('TLabel', font=('Montserrat', 12))
        style.configure('Heading.TLabel', font=('Montserrat', 22, 'bold'))
        style.configure('TButton', font=('Montserrat', 12))
        style.configure('Large.TButton', font=('Montserrat', 14))

        self.background_color = "#f5f5f5"
        self.accent_color = "#3498db"

        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.content_frame = ttk.Frame(self.main_frame, padding=20)
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        self.frame = ttk.Frame(self.content_frame)
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
        title_frame = ttk.Frame(self.frame)
        title_frame.pack(pady=20, fill="x")
        ttk.Label(title_frame, text="APLIKASI KUIS", font=("Montserrat", 28, "bold")).pack()
        ttk.Label(title_frame, text="Uji Pengetahuan Anda", font=("Montserrat", 14, "italic")).pack(pady=5)
        ttk.Separator(self.frame).pack(fill="x", pady=10)

        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=20)
        ttk.Button(button_frame, text="Mulai Kuis", command=self.tampilan_login, bootstyle="success-outline",
                   width=25, style='Large.TButton').pack(pady=15, ipady=8)
        ttk.Button(button_frame, text="Lihat Leaderboard", command=self.menu_leaderboard, bootstyle="info-outline",
                   width=25, style='Large.TButton').pack(pady=15, ipady=8)
        ttk.Button(button_frame, text="Keluar", command=self.root.destroy, bootstyle="danger-outline",
                   width=25, style='Large.TButton').pack(pady=15, ipady=8)

        footer = ttk.Label(self.frame, text="© 2025 Aplikasi Kuis", font=("Montserrat", 10))
        footer.pack(side="bottom", pady=10)

    def tampilan_login(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Silakan Masukkan Data Diri", font=("Montserrat", 22, "bold")).pack(pady=20)

        form_frame = ttk.Frame(self.frame, padding=20)
        form_frame.pack(pady=20, fill="x")

        ttk.Label(form_frame, text="Nama Lengkap", font=("Montserrat", 14)).pack(anchor="w", pady=(10, 5))
        self.entry_nama = ttk.Entry(form_frame, font=("Montserrat", 14), width=40)
        self.entry_nama.pack(fill="x", ipady=5, pady=(0, 15))

        ttk.Label(form_frame, text="Nomor Induk Mahasiswa (NIM)", font=("Montserrat", 14)).pack(anchor="w", pady=(10, 5))
        self.entry_nim = ttk.Entry(form_frame, font=("Montserrat", 14), width=40)
        self.entry_nim.pack(fill="x", ipady=5, pady=(0, 15))

        button_frame = ttk.Frame(form_frame)
        button_frame.pack(pady=20, fill="x")
        ttk.Button(button_frame, text="Mulai Kuis", command=self.mulai_kuis, bootstyle="primary", width=15).pack(
            side="left", padx=5, ipady=8)
        ttk.Button(button_frame, text="Kembali", command=self.menu_awal, bootstyle="secondary", width=15).pack(
            side="left", padx=5, ipady=8)

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
        progress_frame = ttk.Frame(self.frame)
        progress_frame.pack(fill="x", pady=10)
        ttk.Label(progress_frame, text=f"Soal {self.index_soal + 1} dari {len(self.soal)}",
                 font=("Montserrat", 14, "bold")).pack(side="left")
        ttk.Progressbar(progress_frame, value=(self.index_soal + 1) * 100 / len(self.soal),
                        length=400, bootstyle="success").pack(side="right", padx=10)

        question_frame = ttk.Frame(self.frame, padding=20)
        question_frame.pack(fill="x", pady=20)
        ttk.Label(question_frame, text=soal["pertanyaan"], font=("Montserrat", 18),
                 wraplength=600, justify="center").pack()

        options_frame = ttk.Frame(self.frame, padding=10)
        options_frame.pack(fill="x", pady=10)
        self.jawaban_terpilih = tk.StringVar()
        for pilihan in soal["pilihan"]:
            ttk.Radiobutton(options_frame, text=pilihan, variable=self.jawaban_terpilih,
                            value=pilihan, padding=10).pack(fill="x", pady=5, ipady=5)

        ttk.Button(self.frame, text="Lanjut", command=self.periksa_jawaban, bootstyle="primary", width=20).pack(pady=20, ipady=8)

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
        result_frame = ttk.Frame(self.frame, padding=20)
        result_frame.pack(fill=BOTH, expand=True)
        ttk.Label(result_frame, text="Kuis Selesai!", font=("Montserrat", 28, "bold")).pack(pady=20)
        ttk.Label(result_frame, text=f"Terima kasih, {self.nama}", font=("Montserrat", 18)).pack(pady=10)

        score_frame = ttk.Frame(result_frame, padding=20, bootstyle="light")
        score_frame.pack(pady=20, ipadx=20, ipady=20)
        percentage = (self.skor / len(self.soal)) * 100
        ttk.Label(score_frame, text=f"Skor Anda:", font=("Montserrat", 16)).pack(pady=(0, 10))
        ttk.Label(score_frame, text=f"{self.skor} dari {len(self.soal)}", font=("Montserrat", 24, "bold"),
                 bootstyle="success" if percentage >= 70 else "warning" if percentage >= 40 else "danger").pack(pady=5)
        ttk.Label(score_frame, text=f"{percentage:.1f}%", font=("Montserrat", 18, "bold")).pack(pady=5)

        self.simpan_data_txt()

        button_frame = ttk.Frame(result_frame)
        button_frame.pack(pady=20)
        ttk.Button(button_frame, text="Kembali ke Menu", command=self.menu_awal, bootstyle="primary", width=20).pack(
            side="left", padx=5, ipady=8)
        ttk.Button(button_frame, text="Keluar", command=self.root.destroy, bootstyle="danger", width=15).pack(
            side="left", padx=5, ipady=8)

    def simpan_data_txt(self):
        baris = f"{self.nama}:{self.nim}:{self.skor}/{len(self.soal)}\n"
        try:
            with open("data.txt", "a") as f:
                f.write(baris)
        except Exception as e:
            messagebox.showerror("Gagal Menyimpan", f"Terjadi kesalahan saat menyimpan: {e}")

    def get_jumlah_peserta(self):
        try:
            with open("data.txt", "r") as f:
                lines = f.readlines()
                return len([line for line in lines if ":" in line])
        except FileNotFoundError:
            return 0

    def menu_leaderboard(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Leaderboard", font=("Montserrat", 24, "bold")).pack(pady=10)

        # Tambahkan info jumlah pengguna
        jumlah_peserta = self.get_jumlah_peserta()
        ttk.Label(self.frame, text=f"Total Peserta: {jumlah_peserta}", font=("Montserrat", 14, "italic")).pack(pady=5)

        button_frame = ttk.Frame(self.frame, padding=10)
        button_frame.pack(fill="x", pady=20)

        options = [
            ("Lihat Semua Data", self.tampilkan_semua_data, "primary"),
            ("Urut Data berdasarkan NIM", self.Insert_Nim, "primary"),
            ("Urut Data berdasarkan Skor", self.Insert_Skor, "info"),
            ("Cari (Sequential Search)", self.cari_seq, "success"),
            ("Cari (Binary Search)", self.cari_bin, "warning")
        ]

        for text, command, style in options:
            ttk.Button(button_frame, text=text, command=command, bootstyle=f"{style}-outline", width=30).pack(
                pady=8, ipady=8, fill="x")
        ttk.Button(self.frame, text="Kembali", command=self.menu_awal, bootstyle="secondary", width=15).pack(pady=10)

    def tampilkan_semua_data(self):
        self.bersihkan_frame()
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill="x", pady=10)
        ttk.Label(header_frame, text="Data Peserta", font=("Montserrat", 20, "bold")).pack(side="left")
        ttk.Button(header_frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary", width=10).pack(side="right")
        ttk.Separator(self.frame).pack(fill="x", pady=10)

        data_list = ttk.Frame(self.frame, padding=10)
        data_list.pack(fill=BOTH, expand=True)

        try:
            with open("data.txt", "r") as f:
                lines = f.readlines()
            if not lines:
                ttk.Label(data_list, text="Belum ada data.", font=("Montserrat", 12)).pack(pady=20)
            for line in lines:
                ttk.Label(data_list, text=line.strip(), font=("Montserrat", 11)).pack(anchor="w")
        except FileNotFoundError:
            ttk.Label(data_list, text="File tidak ditemukan.", font=("Montserrat", 12)).pack(pady=20)

        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary", width=15).pack(pady=10)

    def cari_seq(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Sequential Search", font=("Montserrat", 20, "bold")).pack(pady=10)
        entry = ttk.Entry(self.frame, font=("Montserrat", 14), width=40)
        entry.pack(pady=10)

        result_label = ttk.Label(self.frame, text="", font=("Montserrat", 12))
        result_label.pack(pady=10)

        def search():
            keyword = entry.get().strip().lower()
            if not keyword:
                messagebox.showwarning("Input Kosong", "Masukkan kata kunci pencarian.")
                return
            try:
                found = False
                with open("data.txt", "r") as f:
                    for line in f:
                        if keyword in line.lower():
                            result_label.config(text=f"Ditemukan:\n{line.strip()}")
                            found = True
                            break
                if not found:
                    result_label.config(text="Tidak ditemukan.")
            except FileNotFoundError:
                result_label.config(text="File tidak ditemukan.")

        ttk.Button(self.frame, text="Cari", command=search, bootstyle="info").pack(pady=5)
        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary").pack(pady=5)

    def cari_bin(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Binary Search (berdasarkan Nama)", font=("Montserrat", 20, "bold")).pack(pady=10)
        entry = ttk.Entry(self.frame, font=("Montserrat", 14), width=40)
        entry.pack(pady=10)

        result_label = ttk.Label(self.frame, text="", font=("Montserrat", 12))
        result_label.pack(pady=10)

        def search():
            nama_dicari = entry.get().strip().lower()
            if not nama_dicari:
                messagebox.showwarning("Input Kosong", "Masukkan nama untuk pencarian.")
                return
            try:
                with open("data.txt", "r") as f:
                    data = [line.strip() for line in f if ":" in line]
                data.sort(key=lambda x: x.split(":")[0].lower())
                left, right = 0, len(data) - 1
                while left <= right:
                    mid = (left + right) // 2
                    name_mid = data[mid].split(":")[0].lower()
                    if name_mid == nama_dicari:
                        result_label.config(text=f"Ditemukan:\n{data[mid]}")
                        return
                    elif name_mid < nama_dicari:
                        left = mid + 1
                    else:
                        right = mid - 1
                result_label.config(text="Tidak ditemukan.")
            except FileNotFoundError:
                result_label.config(text="File tidak ditemukan.")

        ttk.Button(self.frame, text="Cari", command=search, bootstyle="warning").pack(pady=5)
        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary").pack(pady=5)

    def Insert_Nim(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Data Diurutkan berdasarkan NIM", font=("Montserrat", 18, "bold")).pack(pady=10)
        ttk.Label(self.frame, text="(Insertion Sort)", font=("Montserrat", 14)).pack(pady=5)

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
                ttk.Label(self.frame, text=line, font=("Montserrat", 11)).pack(anchor="w")
        except FileNotFoundError:
            ttk.Label(self.frame, text="File tidak ditemukan.", font=("Montserrat", 12)).pack(pady=20)

        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary", width=15).pack(pady=10)

    def Insert_Skor(self):
        self.bersihkan_frame()
        ttk.Label(self.frame, text="Data Diurutkan berdasarkan Skor", font=("Montserrat", 18, "bold")).pack(pady=10)
        ttk.Label(self.frame, text="(Insertion Sort)", font=("Montserrat", 14)).pack(pady=5)

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
                ttk.Label(self.frame, text=line, font=("Montserrat", 11)).pack(anchor="w")
        except FileNotFoundError:
            ttk.Label(self.frame, text="File tidak ditemukan.", font=("Montserrat", 12)).pack(pady=20)

        ttk.Button(self.frame, text="Kembali", command=self.menu_leaderboard, bootstyle="secondary", width=15).pack(pady=10)


if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = KuisApp(root)
    root.mainloop()
