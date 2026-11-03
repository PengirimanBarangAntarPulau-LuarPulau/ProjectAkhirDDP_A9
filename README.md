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
<img width="6292" height="4652" alt="login baru drawio" src="https://github.com/user-attachments/assets/5978b166-0b29-43fb-a4df-fcc4850eb3d2" /><br>
: Flowchart pada halaman ini akan menampilkan menu utama yang berisi login, registrasi, dan keluar. Setelah berhasil login atau registrasi maka akan delay 3detik terlebih dahulu baru diarahkan ke halaman menu sesuai role. <br> 

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
**1. Import Library** <br>
<img width="1060" height="532" alt="library" src="https://github.com/user-attachments/assets/063e5c36-5bbd-4dcc-b80e-718d2d58808d" /><br>
: pada projek ini kami menggunakan 4 library dan json. <br>
- `os` kami gunakan untuk mengecek keberadaan file, menghapus file, dan membersihkan terminal. <br>
- `json` kami gunakan untuk membaca, mengubah dan menyimpan data. <br>
- `pwinput` kami gunakan untuk menyembunyikan karakter yang diketik pengguna pada saat menginput password. <br>
- `prettytable` kami gunakan agar saat menampilkan data pengiriman agar lebih rapi dan enak dipandang. <br>
- `time` kami gunakan untuk loading ketika pengguna berhasil login. <br>

**3. Error Handling Awal** <br>
<img width="1060" height="494" alt="error handling awal" src="https://github.com/user-attachments/assets/d244078f-c60a-4064-92f1-ad8fb44396b9" /> <br>
: pada error handling awal ini kami gunakan sebagai antisipasi agar program tetap bisa berjalan meskipun modul/fungsi `hapus_data` belum tersedia atau gagal diimpor. <br>

**4. Inisialisasi Data** <br>
<img width="1060" height="494" alt="error handling awal" src="https://github.com/user-attachments/assets/86a6be0b-e985-4eee-9bfb-95a4696f66a0" /> <br>
- `file_user = "user.json"` untuk menginisialisasi variabel file_user sebagai tempat menyimpan dan membaca data pengguna. <br>
- `file_pengiriman = "pengiriman.json"` untuk menginisialisasi variabel file_pengiriman sebagai tempat menyimpan dan membaca data pengiriman. <br>

**5. List Lokasi / Data Lokasi** <br>
<img width="1060" height="608" alt="image" src="https://github.com/user-attachments/assets/63249340-dde6-4dab-b86e-79d8163945d1" /> <img width="1060" height="646" alt="image" src="https://github.com/user-attachments/assets/db18df5c-44f7-4596-aa12-389d2eda8278" /> <br>
: menggunakan list agar data bersifat tetap dan tidak dapat diubah. <br>

**6. List Tarif** <br>
<img width="1060" height="532" alt="image" src="https://github.com/user-attachments/assets/2aa5e8c0-f836-4084-8c89-987543ea55af" /> <br>
: menggunakan list agar data bersifat tetap dan tidak dapat diubah. <br>

# FUNCTION
**1. Bersihkan Layar** <br>
<img width="1060" height="532" alt="image" src="https://github.com/user-attachments/assets/131035c9-2da1-46db-904e-d73ccf4fa1fe" /> <br>
: function ini digunakan untuk membersihkan layar terminal dengan menggunakan `os`. <br>

**2. Loading Dashboard** <br>
<img width="1060" height="912" alt="loading dashboard" src="https://github.com/user-attachments/assets/085bf393-7f2a-4f07-8acf-16497b0fd555" /> <br>
: pada function ini ketika pengguna berhasil login/registrasi maka akan ditampilkan delay selama 3detik terlebih dahulu baru diarahkan lanjut ke menu sesuai role. <br>

**3. Baca File** <br>
<img width="1060" height="798" alt="image" src="https://github.com/user-attachments/assets/ed54eec3-12de-47c1-8806-df415b1e4433" /> <br>
: function ini untuk membaca data pada file json, dengan menggunakan error handling jika data tidak ditemukan maka func ini akan memuat ulang data awal dan mengembalikannya. Jika data ada maka akan dibaca dan ditampilkan. <br>

**4. Simpan File** <br>
<img width="1060" height="798" alt="image" src="https://github.com/user-attachments/assets/e387b97d-f49e-4d36-afee-071687c069f1" /> <br>
: function ini mengguna json.dump untuk menyimpan data terbaru kepada file json. <br>

**5. Format Rupiah** <br>
<img width="1060" height="494" alt="image" src="https://github.com/user-attachments/assets/20485951-b2a6-46d1-b669-2a5448d0fdfe" /> <br>
: function ini digunakan untuk mengubah angka selain nol ke format rupiah dengan pemisah ribuan berupa titik dan juga mengubah koma menjadi titik. function ini juga mengecek apabila inputan berupa angka nol maka akan langsung dikembalikan menjadi rupiah 0. <br>

**6. Generate Resi / Cetak Struk** <br>
<img width="1060" height="646" alt="image" src="https://github.com/user-attachments/assets/9484b132-919e-4bb1-aac6-d1920feb09c1" /> <br>
: function ini digunakan untuk membuat nomor resi otomatis, dengan menggunakan perulangan while true, akan dibentuk nomor resi dengan awalan EXP dan 3 digit dibelakangnya dan diawali 0, dan apabila nomor resi sudah digunakan maka akan diganti dengan yang baru yang belum pernah tersimpan. <br>

**7. Cari di Tuple** <br>
<img width="1060" height="570" alt="code-snapshot9" src="https://github.com/user-attachments/assets/914578b7-d5dd-453d-ba4d-756a36f56be6" /> <br>
: function ini digunakan untuk mencari item pada daftar tuple, sistem akan terus mencari hingga menemukan kecocokan antara item dan tujuan input. `.stip()` digunakan untuk menghapus spasi di awal dan di akhir teks, `.lower()` digunakan untuk mengubah teks menjadi lowercase semua. <br>

**8. Cetak Struk** <br>
<img width="961" height="1600" alt="image" src="https://github.com/user-attachments/assets/ac35857a-08ff-4db6-a901-813ccf734ede" /> <br>
: function ini digunakan untuk mencetak bukti struk dengan `biaya_MC` didapat dari `total_biaya` dimulai dari angka 0. `Tarif_MC` didapat dari data `tarif_per_kg` dimulai dari angka 0. Setelahnya print struk bukti pengiriman yang berisi ID Resi, Username Akun, Nama Pemesan, Nomor HP, Kota Tujuan, Berat Barang, Jenis Rute, Tarif per kg, Total biaya MC, Status Pembayaran dan Status Pengiriman. <br>

**9. Registrasi** <br>
<img width="1028" height="2280" alt="code-snapshot11" src="https://github.com/user-attachments/assets/bcfddbcc-7c24-43d1-8ced-34dc65aeef83" /> <br> 
: function ini digunakan untuk registrasi akun user yang baru, dimana meminta input username baru, jika user menginput selain alphabet maka dibatalkan dengan validasi `KeyboardInterrupt`, dan return jika username yang diinput kosong. Jika username ada di data username, maka di print `Username sudah dipakai` dan return. User diminta menginput password baru dengan syarat password harus lebih dari 4 karakter atau registrasi dibatalkan. Setelahnya `data_user` akan ditambahkan ke file dengan dictionary `username, password, role dan saldo`. <br>

**10. Login** <br>
<img width="1028" height="1672" alt="code-snapshot12" src="https://github.com/user-attachments/assets/b79fd3b3-48b3-40e0-ad79-4dca7fde59d4" /> <br>
: function ini digunakan untuk login pengguna. User menginput username, jika salah maka login dibatalkan, jika benar selanjutnya user menginput password menggunakan `pwinput` dan akan dibatalkan jika salah. Jika username dan password yang diinput benar, dan saldo tidak ditemukan di data maka `saldo = 0`. Setelahnya di print username dan role, namun jika tidak sesuai maka program akan `direturn` dan diprint status `username atau password salah`. <br>

**11. Top up saldo** <br>
<img width="1028" height="4522" alt="code-snapshot13" src="https://github.com/user-attachments/assets/3cfa3e22-ef03-463a-9d34-e5ca04eed242" /> <br>
: function ini digunakan untuk top up saldo user. `saldo_sekarang` didapat dari data saldo dimulai dari angka 0. Menggunakan `while True` user menginput nominal rupiah yang ingin di top up, jika user menginput angka 0 atau selain angka maka program akan berhenti dan top up dibatalkan. Jika nominal yang diinput tidak berupa kelipatan dan lebih dari 11.000.000, maka top up akan dibatalkan. Setelahnya user akan konfirmasi `Nominal Bayar, MC Didapat, Total Saldo`, jika ya maka saldo user akan otomatis tertambah dan disimpan di 	`data_user`, namun jika tidak maka top up akan dibatalkan. <br>

**12. Tampilkan Data** <br>
<img width="700" height="3534" alt="tampilkan data" src="https://github.com/user-attachments/assets/a7250740-007f-4907-81e2-5e89ed99ce0b" /> <br>
: pada function ini kami gunakan untuk menampilkan data pengiriman sesuai dengan rolenya, jika user maka akan divalidasi apakah usernamenya sesuai dengan data user, jika ya makaa akan ditampikan data pengirimannya, jika admin maka akan ditampilkan data pengiriman semua. tampilan data menggunakan prettytable agar lebih rapi. <br>

**13. Ajukan Pengiriman User** <br>
<img width="846" height="2050" alt="aju 1" src="https://github.com/user-attachments/assets/b4450fbb-2254-4863-b425-8489cd15eb87" /> <br>
: akan dilakukan input form terlebih dahulu dan akan ditampilkan saldo mc dari user tsb, dan ada error handling dimana jika inputan kosong maka akan otomatis diarahkan untuk mengisi kembali, contohnya seperti pada inputan nomor hp, jika inputan bukan berupa angka lebih daripada 0 maka akan ditampilkan bahw inputan harus berupa angka lebih daripada 0 dan diarahkan untuk mengisi kembali hingga inputan sesuai. <br>
<img width="846" height="1546" alt="aju 2" src="https://github.com/user-attachments/assets/aff85683-e26f-43de-8e86-61ad5539f50a" /> <br>
: lanjutannya akan menyimpan 3 variable yaitu `id_resi`, `kota_antar`, `kota_luar`. dan juga pda bagian ini dilakukan validasi berat barang, dimana jika berat barang tidak sesuai atau lebih dari 30, maka akan ditampilkan bahwa pengiriman ditolak dan data disimpan pada `simpan_file`. <br>
<img width="846" height="1434" alt="aju 3" src="https://github.com/user-attachments/assets/0396a9e5-06d3-49f8-824e-7f2ecd4071e0" /> <br>
: setelahnya adalah validasi kota tujuabn, jika tujuan tidak ada pada list kota tujuan maka akan ditampiulkan pengiriman ditolak dan disimpan. kemudian perhitungan total biaya sesuai dengan kota tujuan. <br>
<img width="846" height="2330" alt="aju 4" src="https://github.com/user-attachments/assets/f48d4d56-aa00-4986-9b85-d6e63ec43c19" /> <br>
: lanjutannya yaitu menampilkan rincian struk pesanan dan validasi pembayaran user, apabila saldo user tidak mencukupi maka akan user akan ditawarkan untuk melakukan top up terlebih dahulu. jika saldo user mencukupi maka user akan diberikan pilihan untuk memotong atau membayar ya atau tidak, jika ya maka saldo akan otomatis berkurang, setelah pembayaran berhasil akan ditampilkan status bahwa pembayaran berhasil. <br>
<img width="846" height="1070" alt="aju 5" src="https://github.com/user-attachments/assets/dc6f4f2e-b6f8-4f80-b4ba-b209cabc17c4" /> <br>
: lalu semua data disimpan pada variabel `pengiriman_baru`. 





# OUTPUT PROGRAM
**Menu Login** <br>
<img width="440" height="244" alt="image" src="https://github.com/user-attachments/assets/5f7fdeed-929c-4bf6-903b-6a49635e6f4d" /> <br>
: Ini merupakan menu awal dari program, dimana pengguna diminta untuk memilih menu yaitu login, registrasi (membuat akun user baru) dan keluar dari program. Jika pengguna tidak memilih menu dari 1-3 atau memasukkan huruf maka program akan terus mengulang sampai dengan pengguna memilih menu 1-3. <br>

**Login** <br>
<img width="520" height="221" alt="image" src="https://github.com/user-attachments/assets/81a4bc1d-88cd-437a-8152-7bab076e0806" /> <br>
: Ini merupakan output yang keluar ketika pengguna memilih pilihan 1 (Login) pada menu sebelumnya, dimana selanjutnya pengguna diminta untuk memasukkan username dan password sesuai dengan rolenya (Pada program ini terdapat dua role, yaitu admin dan user). Jika sudah memasukkan username dan juga password maka selanjutnya akan di arahkan ke dashboard masing-masing role. Namun jika pengguna memasukkan username atau password sesuai dengan isi dari file json yang tersimpan maka program akan mengembalikan pengguna ke menu sebelumnya. <br>

**Registrasi (User Baru)** <br>
<img width="494" height="340" alt="image" src="https://github.com/user-attachments/assets/ba6da592-eac0-4316-8f21-99d039333d95" /> <br>
: Ini merupakan output yang keluar ketika pengguna memilih pilihan menu ke 2, yaitu menu registrasi dimana pada menu ini pengguna diminta untuk membuat username dan juga password baru. Dan jika sudah melakukan registrasi program akan kembali ke menu sebelumnya dan pengguna bisa melakukan login menggunakan akun yang sudah di buat sebelumnya. <br>

# Role Admin <br>
**Dashboard Admin** <br>
: Merupakan output yang keluar ketika kita login sebagai role Admin, dimana pada role ini terdapat CRUD penuh serta menu tambahan validasi pengajuan pengiriman. Di sini pengguna diminta untuk memilih menu dari 1-6, jika tidak program akan terus mengulang dan meminta pengguna untuk tetap memilih menu dari 1-6. <br>

**Data Pengiriman di Admin** <br>
<img width="975" height="461" alt="image" src="https://github.com/user-attachments/assets/cc47ae03-eb5a-4e19-9511-288c792c87b6" /> <br>
: Merupakan output yang keluar ketika kita sebagai admin memilih menu 1 (Lihat semua data pengiriman) dimana pada menu ini admin dapat melihat semua data pengiriman yang ada dan ditampilkan dalam prettytable. Jika ingin keluar admin dapat menekan tombol enter dan akan kembali ke dashboard admin lagi. <br>

**Input pengiriman langsung (Secara offline)** <br>
<img width="513" height="959" alt="image" src="https://github.com/user-attachments/assets/645c4d31-813a-40b5-a046-685f7580166b" /> <br>
: Merupakan output ketika admin memilih menu ke 2 (Input pengiriman langsung pelanggan offline) pada dashboard admin. Menu ini meminta data dari sang pengirim seperti nama, nomor hp, berat dari barang yang akan dikirim, dan kota tujuan pengirimannya. Jika sudah melakukan pendataan maka akan keluar rincian biaya pengirimannya, disini admin meminta konfirmasi dan jika di konfirmasi maka akan keluar struk bukti pengirimannya dan akan langsung tervalidasi. Namun program akan menolak pengiriman jika dari berat atau lokasi pengiriman tidak sesuai dengan ketentuan dari program tersebut. <br>

**Validasi pengajuan pengiriman** <br>
<img width="975" height="690" alt="image" src="https://github.com/user-attachments/assets/c45e759f-4082-4178-a06c-5674e7a87c04" /> <br>
: Ini merupakan output jika admin memilih pilihan menu 3 (Validasi pengajuan pengiriman) dimana pada menu ini admin dapat memvalidasi setiap pengiriman dengan memilih 2 opsi validasi, yaitu; 
1. Validasi satu per satu berdasarkan ID resi.
2. Validasi secara otomatis sesuai dengan urutan antrian. <br>

**Update status perjalanan** <br>
<img width="975" height="727" alt="image" src="https://github.com/user-attachments/assets/087c1fd2-7032-41aa-b757-bc46c4ce0692" /> <br>
: Merupakan output ketika admin memilih menu 4 (Update status perjalanan pengiriman) dimana pada menu ini admin diminta untuk memasukkan ID resi yang ingin di update status pengirimannya, lalu akan diberikan beberapa pilihan status yaitu;
1. Sedang dikirim
2. Sampai tujuan
3. Batalkan pengiriman
Disini admin diminta untuk memilih pilihan status tersebut (1/2/3) <br>

**Hapus data pengiriman** <br>
<img width="975" height="490" alt="image" src="https://github.com/user-attachments/assets/85d15776-ff63-4441-a9a1-9e71bec3bd3b" /> <br>
: Merupakan output dari menu ke 5 (Hapus data pengiriman) dimana pada menu ini admin dapat menghapus data pengiriman, disini admin diminta untuk memasukkan ID resi yang ingin dihapus datanya, lalu program akan meminta validasi (y/n) untuk memastikan apakah data pengiriman tersebut benar-benar ingin dihapus atau tidak. Jika admin memilih “Y” maka data pengiriman tersebut akan terhapus. <br>

**Logout dari Admin** <br>
<img width="709" height="596" alt="image" src="https://github.com/user-attachments/assets/4a4a2a7e-66d2-4a95-8ca4-f7cc921caf22" /> <br>
: Merupakan output yang keluar ketika admin memilih pilihan 6 (logout) program akan langsung kembali ke menu login di awal. <br>

# Role User <br>
**Dashboard User**
<img width="538" height="794" alt="image" src="https://github.com/user-attachments/assets/8aa56efc-7168-4ec7-8f0a-a9f40a3d044f" /> <br>
: Ini merupakan output ketika kita login sebagai role user. Dimana selanjutnya kita di arahkan ke dashboard pengguna dengan menu yang lebih terbatas daripada role admin. Ketika login saldo dari user juga akan ditampilkan. <br>

**Data pengiriman user** <br>
<img width="975" height="323" alt="image" src="https://github.com/user-attachments/assets/853bf06c-a088-4cc1-803e-b39b37f8eabb" /> <br>
: Merupakan output ketika user memilih pilihan menu 1 (Cek status pengiriman saya) dimana sesuai dengan namanya user disini hanya bisa melihat data pengiriman yang user itu pesan sendiri. Jika ingin keluar user dapat menekan enter.

**Ajukan pengiriman baru** <br>
<img width="471" height="1101" alt="image" src="https://github.com/user-attachments/assets/17c0bcef-445d-48f2-b5b6-1b473d2acf28" /> <br>
: Merupakan output ketika user memilih pilihan menu 2 (Ajukan pengiriman barang baru). Untuk di awal nama pemesan dan juga saldo awal dari user akan langsung di tampilkan lalu untuk data yang akan diisi itu ada nomor hp, berat barang, dan tujuang pengiriman. Jika sudah diisi akan ditampilkan rincian struk pesanan berisi biaya dan user diminta untuk mengonfirmasi pesanan tersebut (y/n). Jika y, maka saldo dari user akan otomatis terpotong jika saldonya mencukupi dan pengajuan pengiriman berhasil dikirim, ID resi pun otomatis terbut. Namun program akan menolak pengiriman jika dari berat atau lokasi pengiriman tidak sesuai dengan ketentuan dari program tersebut. <br>

**Bayar tagihan pengiriman** <br>
<img width="975" height="357" alt="image" src="https://github.com/user-attachments/assets/6c42fed6-4619-4973-b160-a14004b9aef3" /> <br>
: Ini merupakan output ketika user memilih pilihan menu 3 (Bayar tagihan pengiriman sesuai struk). Di awal akan di tampilkan semua data pengiriman dari user tersebut dalam prettytable, lalu user diminta untuk memasukkan ID resi dari pengiriman yang ingin di bayar, jika sudah maka akan muncul resi dan total tagihan yang harus dibayar. Disini saldo dari user harus mencukupi untuk bisa membayar pesanannya tersebut, jika belum mencukupi maka user akan di perintahkan untuk top up saldo terlebih dahulu. <br>

**Cetak struk bukti pengiriman** <br>
<img width="975" height="747" alt="image" src="https://github.com/user-attachments/assets/37feb994-3c5a-4f7d-b05c-01e3f4899942" /> <br>
 : Ini merupakan output ketika user memilih pilihan 4 (Cetak struk bukti pengiriman). Dimana di awal akan di tampilkan semua data pengiriman yang user tersebut lakukan, lalu user diminta untuk memasukkan ID resi yang ingin di cetak struknya, dan struk dari resi tersebut akan tercetak. Jika sudah user diminta untuk menekan enter untuk kembali ke dashboard kembali. <br>

**Top up saldo** <br>
<img width="975" height="990" alt="image" src="https://github.com/user-attachments/assets/02cde5a0-3a23-4276-8bea-766cebb27f72" /> <br>
: Merupakan output ketika user memilih pilihan ke 5 (Top up saldo MC). Untuk 1 MC itu bernilai Rp. 1.000, dan untuk batas dari top up nya sendiri yaitu Rp.11.000.000. Pertama tama user akan diminta untuk mengisi nominal top  up yang mereka inginkan, jika sudah maka program akan meminta konfirmasi dari user (y/n) jika user memilih y maka top akan lanjut dan saldo user akan bertambah sesuai dengan nominal yang user isi tadi. <br>

**Logout dari User** <br>
<img width="634" height="646" alt="image" src="https://github.com/user-attachments/assets/7e1f7da0-34c4-4077-a005-f2d67564ccb8" /> <br>
: Ini merupakan output dari pilihan ke 6 (logout) ketika user memilih ini, maka dia langusng kembali ke menu sebelumnya yaitu login. <br>

**Keluar dari program** <br>
 <img width="659" height="290" alt="image" src="https://github.com/user-attachments/assets/e67eea38-4f7e-401c-9dd0-98027362f107" /> <br>
: Merupakan output ketika pengguna memilih pilihan 3 (keluar) pengguna akan keluar dan program akan berhenti. <br>








 











