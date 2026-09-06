<div align="center">
<h1 align="center">📜 My Portofolio</h1>
<p align="center">Portofolio Website for PBP</p>

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white&logoSize=auto)

Nama: Risyad Athaya Muhammad

NPM: 2506595890

Kelas: PBP F
</div>

## ⚙️ How to Run
1. **Clone this repository** from terminal using the following command
   ```bash
   $ git clone https://github.com/RisyadAthaya/myportofolio.git
   ```
2. **Create and activate the virtual environment** using the following command in the project root directory
   ```bash
   $ python -m venv venv
   ```
   then activate it
   ```bash
   $ venv\Scripts\activate
   ```
3. **Install the dependencies** on requirements.txt using the following command
   ```bash
   $ pip install -r requirements.txt
   ```
4. **Run the server** using the following command
   ```bash
   $ python manage.py runserver
   ```
   then open your browser and go to http://127.0.0.1:8000/ to view the website.

## ❓ Reflective Questions
### Tugas 1
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda
   merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`,
   atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa
   elemen tersebut sudah memenuhi kebutuhan desain Anda?

Saya menggunakan beberapa tag semantic pada HTML, terutama `<section>`. Meskipun secara design tag ini tidak
berpengaruh secara signifikan, penggunaannya sangat membantu saya sebagai developer website untuk memahami
fungsi dari elemen yang sedang saya kerjakan. Dengan begitu, saya bisa memilih style atau design yang lebih
sesuai dengan elemen yang ingin saya ubah.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda
   mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan
   desktop ke mobile?

Tantangan terbesarnya menurut saya adalah memastikan spacing atau gap dari setiap elemen tetap nyaman untuk
dilihat dari berbagai device. Untuk tata letak, selama menggunakan flex dan grid, menurut saya tidak terlalu
sulit untuk menatanya ulang untuk tampilannya di device lain. Akan tetapi, saya sempat (dan masih) mengalami
beberapa masalah karena padding atau margin yang saya gunakan terlalu besar sehingga proporsi text dan gambar
di website tidak sesuai harapan saya. Untuk menentukan elemen mana yang harus diubah, saya melihat dari dua
hal: ukuran elemen dan directionnya (row atau column). Saya akan memperhatikan elemen yang besar dan/atau
diletakkan secara row. Biasanya, elemen yang kecil atau diletakkan secara column tidak menimbulkan banyak
masalah (meskipun tetap harus diperiksa secara manual).

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan
   informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling
   ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

Yang paling terasa tentunya saya harus mengetik item-item untuk sebuah list secara manual. Untuk sekarang,
belum terlalu banyak hal yang ingin saya masukkan, tetapi hal ini bisa cukup menyulitkan ketika saya ingin memasukkan
item lebih banyak atau elemen dari masing-masing item semakin kompleks (seperti menambahkan gambar, link, dan lainnya).
Sederhana saja, pada iterasi selanjutnya, saya ingin membuat sebuah file JavaScript untuk memasukkan elemen dari
item-item tersebut dengan lebih mudah.

## 🤖 AI Disclosure
Tools AI yang digunakan: Gemini.

Apa saja yang saya lakukan dengan AI pada codebase ini?
- Mencari arti dari beberapa semantic tags di HTML
- "Translate" penulisan classes di Tailwind CSS (karena terbiasa memakai Tailwind) ke Vanilla CSS
- Mencari penataan README.md yang baik
- Menanyakan cara menulis commit messages yang sesuai dengan conventional commits

Saya menyadari bahwa AI masih memiliki banyak kekurangan sehingga saya selalu melakukan crosscheck
setiap kali mendapatkan jawaban dari chatbot. Selain itu, saya tidak menggunakan AI Coding Assistant
untuk memudahkan saya mengingat style-style dan juga elemen-elemen yang saya buat secara manual di HTML
dan juga CSS.