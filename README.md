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
   $ python -m venv env
   ```
   then activate it
   ```bash
   $ env\Scripts\activate
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

### Tugas 2
1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima 
   proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, 
   model, dan template.

Ketika user ingin membuka website ini, mereka mengirimkan permintaan. Permintaan tersebut diterima oleh urls.py proyek, 
lalu mencocokkan path URL serta mengarahkannya ke urls.py aplikasi. Setelah itu, urls.py aplikasi kembali mencocokkan 
URL untuk memanggil view yang sesuai dengan permintaannya. Ketika view dipanggil, seringkali mereka akan membuat sebuah 
konteks terlebih dahulu untuk diberikan ke template nantinya. Pada pembuatan konteks inilah model akan mengambil data 
yang diperlukan oleh views (dan sebelumnya telah ditentukan struktur/fields datanya). Template kemudian akan di-_render_ 
yang menggabungkan HTML dengan data konteks dari view. Terakhir, view akan mengirimkan hasil render HTML tersebut ke 
_browser_ user.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template?
   Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

Banyak sekali alasan untuk memisahkan data dari template. Pertama, dengan memisahkannya, website kita menjadi jauh
lebih _maintainable_. Ketika kita ingin memasukkan atau mengubah data, kita hanya perlu melakukan modifikasi di 
database, bukan di templatenya secara langsung. Hal ini memudahkan kita karena tidak perlu mengubah kode HTML di 
template. Kedua, kode kita jadi bersifat dinamis. Misalnya tugas kita sekarang bukanlah membuat website portofolio, 
tapi membuat home page Youtube. Dengan memisahkan data dari template, kita bisa menggunakan template yang sama untuk 
menampilkan home page yang rekomendasi videonya berbeda-beda untuk setiap user. Terakhir, kita jadi bisa menggunakan 
data di sebuah template untuk ditampilkan juga di template lainnya. Dengan begitu, akan lebih mudah untuk mengembangkan 
website/aplikasi yang kita buat.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu 
   menjalankan kedua perintah tersebut.

_Command_ "makemigrations" hanya berfungsi untuk membuat skrip migrasi berdasarkan perubahan yang ada di model. Jadi, 
hanya membuat instruksinya saja. Sedangkan, _command_ "migrate" mengeksekusi skrip migrasi tersebut. _Command_ inilah 
yang secara langsung mengubah database yang kita punya. Salah satu perubahan pada model yang saya terapkan di website 
ini dan memerlukan kedua _command_ tersebut adalah perubahan field title menjadi position dan organization di model 
Experience saya. Dengan begitu, code saya berubah dari

```python
class Experience(models.Model):
    ...
    title = models.CharField(max_length=255)
    ...
```

menjadi

```python
class Experience(models.Model):
    ...
    position = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    ...
```

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

Note: Untuk tugas 2, saya tidak menggunakan AI sama sekali untuk menuliskan code.