# Portofolio — Reynold Andika Nugroho

Website portofolio statis (HTML + CSS + JS, tanpa build) yang siap di-hosting di GitHub Pages.

## Struktur

```
index.html        → halaman utama
style.css         → tampilan (tema terang/gelap)
script.js         → animasi, toggle tema, menu mobile
assets/
  profile.jpg                      → foto profil
  CV-Reynold-Andika-Nugroho.pdf    → CV untuk tombol "Unduh CV"
```

## Hosting di GitHub Pages

1. Buat repository baru di GitHub, misalnya `<username>.github.io` (agar alamatnya `https://<username>.github.io`).
2. Upload semua file di folder ini ke repository tersebut (atau lewat git):

   ```
   git init
   git add .
   git commit -m "Portofolio pertama"
   git branch -M main
   git remote add origin https://github.com/<username>/<username>.github.io.git
   git push -u origin main
   ```

3. Buka **Settings → Pages**, pilih **Deploy from a branch**, branch `main`, folder `/ (root)`, lalu **Save**.
4. Tunggu 1–2 menit, website aktif di `https://<username>.github.io`.

## Tema

Tampilan diadaptasi dari [react-resume-template](https://github.com/tbakerx/react-resume-template) oleh Tim Baker
(MIT License, © 2021 Tim Baker), ditulis ulang dalam HTML/CSS biasa agar bisa di-hosting di GitHub Pages tanpa build.

## Hal yang mudah diubah

- **Level skill**: di `index.html`, ubah `data-level="..."` (skala 1–10) pada tiap `<div class="skill">`.
- **Background hero**: di `style.css`, bagian `.hero__bg`, ganti gradient dengan foto,
  misalnya `background: url(assets/header-background.jpg) center/cover;`.
- **Form kontak**: tombol "Kirim Pesan" membuka aplikasi email pengunjung dengan pesan terisi otomatis
  (GitHub Pages tidak punya server untuk mengirim email).

## Mengganti foto

Foto saat ini diambil dari CV (resolusi kecil, 200×248). Untuk hasil lebih tajam, ganti `assets/profile.jpg`
dengan foto resolusi lebih tinggi (rasio sekitar 4:5) memakai nama file yang sama.
