# ProjectAkhirDDP_A9
**Judul/Tema Projek**: Pengiriman Barang Antar Pulau dan Luar Pulau <br>
**Anggota & Peran**: <br>
- Muhammad Omar Zaahran (2609116023) / Project Leader <br>
- Tisha Ayu Nabilah Lubis (2609116006) / Anggota <br>
- Faizah Nabil (2609116007) / Anggota <br>
- Fatimatu Jahra (2609116033) / Anggota <br>

**Deskripsi Masalah**: Perkembangan teknologi mendorong kebutuhan akan sistem pengiriman barang yang lebih praktis dan efisien. Pengiriman konvensional masih memiliki keterbatasan dalam tarif, jangkauan, dan fleksibilitas. Oleh karena itu, dirancang sistem pengiriman barang antar pulau berbasis online yang menyediakan riwayat pemesanan serta pembayaran menggunakan e-money untuk mempermudah proses pengiriman. <br>
**Tujuan**: <br>
1.	Membangun sistem pengantaran barang secara online yang efisien dan mudah digunakan oleh para pengguna. <br>
2.	Memberikan akses agar pelanggan bisa mengirim barang ke dalam pulau dan luar pulau. <br>
3.	Mempermudah proses validasi arah tujuan pengantaran barang. <br>
<br>

# FLOWCHART
**1. Halaman Login dan Registrasi** <br>
<img width="6292" height="4652" alt="FW LOGIN" src="https://github.com/user-attachments/assets/7644528d-99ca-4990-aa82-d0b66a3506aa" /> <br>
: Flowchart pada halaman ini akan menampilkan menu utama yang berisi login, registrasi, dan keluar. Setelah dipilih salah satunya maka akan diarahkan ke halaman khusus sesuai pilihannya, namun jika pilihan tidak termasuk 1-3 maka akan dikembalikan ke tampilan menu utama. <br> 

**2. Halaman Admin** <br>
<img width="5152" height="6736" alt="fwadm drawio" src="https://github.com/user-attachments/assets/e610264e-f27c-468b-867b-431ee855e82b" /> <br>
: Flowchart pada halaman ini akan menampilkan menu CRUD penuh, menu tambahan validasi pengajuan dan pilihan logout. <br>
  `Pilihan 1` <br>
  akan menampilkan data dengan tampilan tabel dari prettytable, setelahnya akan menekan enter dan kembali ke halaman admin. <br>
  `Pilihan 2` <br>
  akan menampilkan halaman tambah pengiriman. <br>
  `Pilihan 3` <br>
  akan menampilkan halaman validasi penginputan. <br>
  `Pilihan 4` <br>
  akan menampilkan data dan input id resi, jika data akan ketemu maka akan dicek status, jika status diterima maka akan menampilkan 3 pilihan baru yaitu sedang dikirim, sampai tujuan, dan batalkan. Jika pilihan 1-3 maka akan otomatis disimpan ke json, jika pilihan di luar 1-3 maka update akan dibatalkan dan dikembalikan ke halaman admin. <br>
  `Pilihan 5` <br>
  akan menampilkan data dan id resi, apabila ketemu maka akan diberikan pilihan hapus (y/n), apabila ya maka data akan dihapus dan disimpan ke json, setelahnya dikembalikan ke halamn admin. <br>
  `Pilihan 6` <br>
  akan kembali ke halaman login. <br>
  

**3. Halaman Customer** <br>
 <img width="4412" height="5012" alt="FW CUST drawio" src="https://github.com/user-attachments/assets/341906e5-e3a1-43b7-bda3-ee90fe58f0b8" /> <br>
: Flowchart pada halaman ini hanya akan menampilkan menu yang lebih terbatas dibanding halaman dashboard admin. <br>
`Pilihan 1` <br>
akan menampilkan data pengiriman dari customer dengan menampilkan tabel dari prettytable, setelahnya akan menekan enter dan kembali ke halaman customer. <br>
`Pilihan 2` <br>
akan menampilkan halaman tambah pengiriman. <br>
 `Pilihan 3` <br>
akan menampilkan halaman untuk membayar pesanan. <br>
 `Pilihan 4` <br>
akan menampilkan halaman untuk mencetak struk bukti. <br>
  `Pilihan 5` <br>
akan menampilkan halaman untuk melakukan top up saldo dari akun customer. <br>
 `Pilihan 6` <br>
akan kembali ke halaman login. <br>
 
 **4. Halaman Validasi Pengiriman** <br>
 <img width="7724" height="10092" alt="FW VALIDASI PENGIRIMAN drawio" src="https://github.com/user-attachments/assets/605f43c1-2850-412f-8a5f-637bc57b79c0" /> <br>
 `page user dari page yang berbeda` <br> 
 pengguna mengajukan pengiriman dengan status "menunggu validasi". <br>
 `ketersediaan antrian` <br>
 jika antrian kosong maka tidak ada pengajuan menunggu validasi, tapi jika antrian tidak kosong tampilkan dengan pretty table. <br>
 `pilihan 1` <br>
 akan menampilkan input id resi <br>
 `pilihan 2`
 akan menampilkan eksekusi validasi pada setiap paket di antrian. <br>
 
 **5. Halaman Pesan Pengiriman** <br>
 <img width="4572" height="10172" alt="FW PESAN PENGIRIMAN drawio" src="https://github.com/user-attachments/assets/5786855d-5ff3-4bfb-a6c2-4e4712682916" /> <br>
 `Tampil daftar kiriman` <br>
sistem memuat dan menampilkan daftar seluruh pengiriman menggunakan prettytable. <br>
 `Tampil daftar kiriman` <br>
pengguna diminta memasukkan nomor ID resi (input 0 untuk batal), lalu sistem memeriksa apakah ID tersebut valid atau terdaftar. <br>
 `Input data pengiriman baru` <br>
pengguna diminta memasukkan detail data pengiriman baru (seperti kota tujuan, berat, dll.). <br>
 `Pengecekan tarif` <br>
sistem menghitung dan memeriksa biaya pengiriman berdasarkan data yang diinput. <br>
 `Pengecekan saldo MC` <br>
sistem memeriksa apakah saldo MC pengguna mencukupi untuk membayar biaya pengiriman. <br>
 `Potong saldo & simpan data` <br>
jika saldo cukup, saldo MC pengguna akan dikurangi, lalu data diperbarui dan disimpan ke file users.json dan pengiriman.json. <br>
 `Selesai & cetak struk` <br>
sistem menampilkan informasi bahwa transaksi berhasil, menampilkan sisa saldo, dan mencetak struk pengiriman.

 
 **6. Halaman Bayar Tagihan** <br>
 <img width="2332" height="6692" alt="FW BAYAR drawio" src="https://github.com/user-attachments/assets/992e6863-d18f-4037-a13a-b0ae124f014c" /> <br>
: Flowchart pada halaman ini akan menampilkan pemrosesan pembayaran 
`Filter tagihan customer` <br>
akan memfilter tagihan milik pengguna. <br>
`Ketersediaan tagihan` <br>
jika tidak ada tagihan aktif, sistem menampilkan pesan "Tidak ada tagihan pengiriman aktif" lalu kembali ke halaman utama. Jika ada, sistem lanjut menampilkan tagihan menggunakan PrettyTable dan meminta input ID resi. <br>
`Ketersediaan tagihan` <br>
jika pengguna memasukkan angka 0 (batal), proses dibatalkan dan kembali ke halaman utama. jika ID resi yang dimasukkan tidak ditemukan di dalam daftar tagihan, sistem menampilkan pemberitahuan error. <br>
`Memeriksa saldo (MC)` <br>
jika ID valid, sistem menampilkan detail resi target, total tagihan, dan saldo MC pengguna. Sistem kemudian memeriksa apakah saldo MC mencukupi (Saldo MC > biaya MC). Jika tidak cukup, sistem meminta pengguna melakukan top-up. <br>
`Konfirmasi pembayaran` <br>
jika saldo mencukupi, sistem meminta konfirmasi pembayaran (y/n). Jika pengguna memilih tidak, pembayaran dibatalkan. <br>
`Penyimpanan data` <br>
jika pembayaran dikonfirmasi, saldo MC pengguna akan dikurangi sebesar biaya tagihan, lalu diperbarui dan disimpan ke file
`Pembaruan status dan selesai` <br> 
Status pembayaran diubah menjadi "Lunas" (serta mengubah status pengiriman dari "Menunggu Pembayaran" menjadi "Diproses"), lalu data disimpan ke pengiriman.json. Terakhir, sistem menampilkan informasi pembayaran berhasil, sisa saldo, mencetak struk, dan mengembalikan pengguna ke halaman utama. <br>
 
 **7  . Halaman Top Up Saldo** <br>
 <img width="2496" height="5492" alt="FW TOP UP SALDO drawio" src="https://github.com/user-attachments/assets/af88e5fa-d7ac-40e8-941d-1d4ebd2f81e5" /> <br>
: Flowchart pada halaman ini akan menampilkan top up saldo <br>
  `Tampilkan kurs dan saldo` <br>
  akan menampilkan kurs 1 MC dan saldo saat ini <br>
  `Input nominal rupiah` <br>
  jika yang diinput adalah selain angka, 0 atau lebih dari 11.000.000 maka top up akan dibatalkan dan kembali ke halaman awal <br>
  `MC didapat` <br>
  akan menampilkan jumlah MC yang didapat cust dengan nominal / 1.000 <br>
  `Tampilkan konfirmasi` <br>
  akan menampilkan konfirmasi berupa nominal yang harus dibayar, MC yang akan didapat dan total saldo setelahnya <br>
  `Melanjutkan transaksi top up` <br>
  jika user memilih lanjut maka saldo MC akan otomatis tertambah dengan MC yang didapat, sedangkan jika tidak maka transaksi akan dibatalkan dan dikembalikan ke page awal <br>
  `Menyimpan data` <br>
  akan menyimpan data saldo terbaru ke users.json <br>
  `Cetak struk` <br>
  akan mencetak struk bukti top up dengan status berhasil <br>
  `Kembali ke halaman awal` <br>

# CODE PROGRAM
**Import Library & Inisialisasi** <br>
<img width="1060" height="608" alt="image" src="https://github.com/user-attachments/assets/de60b85f-fe66-4505-8dfe-61d614ce6263" /> <br>
: pada projek ini kami menggunakan 4 library dan 2 inisialisasi data. <br>
- `os` kami gunakan untuk mengecek keberadaan file, menghapus file, dan membersihkan terminal. <br>
- `json` kami gunakan untuk membaca, mengubah dan menyimpan data. <br>
- `pwinput` kami gunakan untuk menyembunyikan karakter yang diketik pengguna pada saat menginput password. <br>
- `prettytable` kami gunakan agar saat menampilkan data pengiriman agar lebih rapi dan enak dipandang. <br>
- `file_user = "user.json"` untuk menginisialisasi variabel file_user sebagai tempat menyimpan dan membaca data pengguna. <br>
- `file_pengiriman = "pengiriman.json"` untuk menginisialisasi variabel file_pengiriman sebagai tempat menyimpan dan membaca data pengiriman. <br>

**List Lokasi / Data Lokasi** <br>
<img width="1060" height="608" alt="image" src="https://github.com/user-attachments/assets/63249340-dde6-4dab-b86e-79d8163945d1" /> <img width="1060" height="646" alt="image" src="https://github.com/user-attachments/assets/db18df5c-44f7-4596-aa12-389d2eda8278" /> <br>
: menggunakan list agar data bersifat tetap dan tidak dapat diubah. <br>

**List Tarif** <br>
<img width="1060" height="532" alt="image" src="https://github.com/user-attachments/assets/2aa5e8c0-f836-4084-8c89-987543ea55af" /> <br>
: menggunakan list agar data bersifat tetap dan tidak dapat diubah. <br>

# FUNCTION
**Bersihkan Layar** <br>
<img width="1060" height="532" alt="image" src="https://github.com/user-attachments/assets/131035c9-2da1-46db-904e-d73ccf4fa1fe" /> <br>
: function ini digunakan untuk membersihkan layar terminal dengan menggunakan `os`. <br>

**Baca File** <br>
<img width="1060" height="798" alt="image" src="https://github.com/user-attachments/assets/ed54eec3-12de-47c1-8806-df415b1e4433" /> <br>
: function ini untuk membaca data pada file json, dengan menggunakan error handling jika data tidak ditemukan maka func ini akan memuat ulang data awal dan mengembalikannya. Jika data ada maka akan dibaca dan ditampilkan. <br>

**Simpan File** <br>
<img width="1060" height="798" alt="image" src="https://github.com/user-attachments/assets/e387b97d-f49e-4d36-afee-071687c069f1" /> <br>
: function ini mengguna json.dump untuk menyimpan data terbaru kepada file json. <br>

**Format Rupiah** <br>
<img width="1060" height="494" alt="image" src="https://github.com/user-attachments/assets/20485951-b2a6-46d1-b669-2a5448d0fdfe" /> <br>
: function ini digunakan untuk mengubah angka selain nol ke format rupiah dengan pemisah ribuan berupa titik dan juga mengubah koma menjadi titik. function ini juga mengecek apabila inputan berupa angka nol maka akan langsung dikembalikan menjadi rupiah 0. <br>

**Generate Resi / Cetak Struk** <br>
<img width="1060" height="646" alt="image" src="https://github.com/user-attachments/assets/9484b132-919e-4bb1-aac6-d1920feb09c1" /> <br>
: function ini digunakan untuk membuat nomor resi otomatis, dengan menggunakan perulangan while true, akan dibentuk nomor resi dengan awalan EXP dan 3 digit dibelakangnya dan diawali 0, dan apabila nomor resi sudah digunakan maka akan diganti dengan yang baru yang belum pernah tersimpan. <br>

**Cari di Tuple** <br>
<img width="1060" height="570" alt="code-snapshot9" src="https://github.com/user-attachments/assets/914578b7-d5dd-453d-ba4d-756a36f56be6" /> <br>
: function ini digunakan untuk mencari item pada daftar tuple, sistem akan terus mencari hingga menemukan kecocokan antara item dan tujuan input. `.stip()` digunakan untuk menghapus spasi di awal dan di akhir teks, `.lower()` digunakan untuk mengubah teks menjadi lowercase semua. <br>

**Cetak Struk** <br>
<img width="961" height="1600" alt="image" src="https://github.com/user-attachments/assets/ac35857a-08ff-4db6-a901-813ccf734ede" /> <br>
: function ini digunakan untuk mencetak bukti struk dengan `biaya_MC` didapat dari `total_biaya` dimulai dari angka 0. `Tarif_MC` didapat dari data `tarif_per_kg` dimulai dari angka 0. Setelahnya print struk bukti pengiriman yang berisi ID Resi, Username Akun, Nama Pemesan, Nomor HP, Kota Tujuan, Berat Barang, Jenis Rute, Tarif per kg, Total biaya MC, Status Pembayaran dan Status Pengiriman. <br>

**Registrasi** <br>
<img width="1028" height="2280" alt="code-snapshot11" src="https://github.com/user-attachments/assets/bcfddbcc-7c24-43d1-8ced-34dc65aeef83" /> <br> 

**Login** <br>
<img width="1028" height="1672" alt="code-snapshot12" src="https://github.com/user-attachments/assets/b79fd3b3-48b3-40e0-ad79-4dca7fde59d4" /> <br>

**Top up saldo** <br>
<img width="1028" height="4522" alt="code-snapshot13" src="https://github.com/user-attachments/assets/3cfa3e22-ef03-463a-9d34-e5ca04eed242" /> <br>









 











