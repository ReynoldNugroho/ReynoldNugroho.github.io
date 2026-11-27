"""
Snake 2D - Game Ular Sederhana
Pembuat : Reynold Nugroho
Library : tkinter (bawaan Python, tidak perlu install apa pun)

Kontrol:
    Panah / WASD  : gerakkan ular
    Spasi         : pause / lanjut
    R             : main lagi setelah game over
"""

import random
import tkinter as tk

__author__ = "Reynold Nugroho"

# ---------------- Pengaturan ----------------
LEBAR = 600
TINGGI = 600
UKURAN = 20                 # ukuran satu kotak
KECEPATAN = 100             # ms per langkah (makin kecil makin cepat)

WARNA_BG = "#1e1e2e"
WARNA_KEPALA = "#a6e3a1"
WARNA_BADAN = "#40a02b"
WARNA_MAKANAN = "#f38ba8"
WARNA_TEKS = "#cdd6f4"

ARAH = {
    "Up": (0, -1), "w": (0, -1),
    "Down": (0, 1), "s": (0, 1),
    "Left": (-1, 0), "a": (-1, 0),
    "Right": (1, 0), "d": (1, 0),
}


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake 2D - by Reynold Nugroho")
        self.root.resizable(False, False)

        self.label = tk.Label(root, font=("Consolas", 14, "bold"),
                              bg=WARNA_BG, fg=WARNA_TEKS)
        self.label.pack(fill="x")

        self.canvas = tk.Canvas(root, width=LEBAR, height=TINGGI,
                                bg=WARNA_BG, highlightthickness=0)
        self.canvas.pack()

        tk.Label(root, text="Dibuat oleh Reynold Nugroho",
                 font=("Consolas", 10), bg=WARNA_BG, fg="#6c7086").pack(fill="x")

        self.high_score = 0
        root.bind("<Key>", self.tombol)
        self.mulai()

    # ---------------- Logika game ----------------
    def mulai(self):
        tengah_x = (LEBAR // UKURAN) // 2
        tengah_y = (TINGGI // UKURAN) // 2
        self.ular = [(tengah_x - i, tengah_y) for i in range(3)]
        self.arah = (1, 0)
        self.arah_berikut = (1, 0)
        self.skor = 0
        self.game_over = False
        self.pause = False
        self.makanan = self.buat_makanan()
        self.update_label()
        self.langkah()

    def buat_makanan(self):
        kolom = LEBAR // UKURAN
        baris = TINGGI // UKURAN
        while True:
            posisi = (random.randint(0, kolom - 1), random.randint(0, baris - 1))
            if posisi not in self.ular:
                return posisi

    def tombol(self, event):
        key = event.keysym
        if key in ARAH or key.lower() in ARAH:
            baru = ARAH.get(key, ARAH.get(key.lower()))
            # tidak boleh berbalik arah langsung
            if (baru[0] + self.arah[0], baru[1] + self.arah[1]) != (0, 0):
                self.arah_berikut = baru
        elif key == "space" and not self.game_over:
            self.pause = not self.pause
            self.gambar()
        elif key.lower() == "r" and self.game_over:
            self.mulai()

    def langkah(self):
        if self.game_over:
            return
        if not self.pause:
            self.arah = self.arah_berikut
            kepala_x, kepala_y = self.ular[0]
            kepala_baru = (kepala_x + self.arah[0], kepala_y + self.arah[1])

            nabrak_dinding = not (0 <= kepala_baru[0] < LEBAR // UKURAN and
                                  0 <= kepala_baru[1] < TINGGI // UKURAN)
            if nabrak_dinding or kepala_baru in self.ular[:-1]:
                self.selesai()
                return

            self.ular.insert(0, kepala_baru)
            if kepala_baru == self.makanan:
                self.skor += 10
                self.high_score = max(self.high_score, self.skor)
                self.makanan = self.buat_makanan()
                self.update_label()
            else:
                self.ular.pop()

            self.gambar()
        self.root.after(KECEPATAN, self.langkah)

    def selesai(self):
        self.game_over = True
        self.gambar()
        self.canvas.create_text(LEBAR // 2, TINGGI // 2 - 20, text="GAME OVER",
                                fill=WARNA_MAKANAN, font=("Consolas", 36, "bold"))
        self.canvas.create_text(LEBAR // 2, TINGGI // 2 + 25,
                                text=f"Skor: {self.skor}   |   Tekan R untuk main lagi",
                                fill=WARNA_TEKS, font=("Consolas", 14))

    # ---------------- Tampilan ----------------
    def update_label(self):
        self.label.config(text=f"Skor: {self.skor}    High Score: {self.high_score}")

    def gambar(self):
        self.canvas.delete("all")

        mx, my = self.makanan
        self.canvas.create_oval(mx * UKURAN + 2, my * UKURAN + 2,
                                (mx + 1) * UKURAN - 2, (my + 1) * UKURAN - 2,
                                fill=WARNA_MAKANAN, outline="")

        for i, (x, y) in enumerate(self.ular):
            warna = WARNA_KEPALA if i == 0 else WARNA_BADAN
            self.canvas.create_rectangle(x * UKURAN + 1, y * UKURAN + 1,
                                         (x + 1) * UKURAN - 1, (y + 1) * UKURAN - 1,
                                         fill=warna, outline="")

        if self.pause:
            self.canvas.create_text(LEBAR // 2, TINGGI // 2, text="PAUSE",
                                    fill=WARNA_TEKS, font=("Consolas", 32, "bold"))


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg=WARNA_BG)
    SnakeGame(root)
    root.mainloop()
