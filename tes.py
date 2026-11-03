# import os
# import json
# import pwinput
# from prettytable import PrettyTable

# from Projek import hapus_data

# file_user = "users.json"
# file_pengiriman = "pengiriman.json"

# TUJUAN_ANTAR_PULAU = (
#     "Samarinda",
#     "Pontianak",
#     "Palangkaraya",
#     "Banjarmasin",
#     "Tanjung Selor"
# )

# TUJUAN_LUAR_PULAU = (
#     "Jakarta",
#     "Banda Aceh",
#     "Palembang",
#     "Bali",
#     "Papua",
#     "Makassar"
# )

# # Tarif langsung dalam satuan MC
# TARIF_ANTAR_PULAU = 15 
# TARIF_LUAR_PULAU = 35  
# KURS_MC_RUPIAH = 1000  # Kurs khusus untuk menu Top Up saldo


# def bersihkan_layar():
#     if os.name == "nt":
#         os.system("cls")
#     else:
#         os.system("clear")


# def baca_file(nama_file, data_awal):
#     if not os.path.exists(nama_file):
#         simpan_file(nama_file, data_awal)
#         return data_awal
    
#     try:
#         with open(nama_file, "r") as f:
#             data = json.load(f)
#             return data
#     except Exception:
#         simpan_file(nama_file, data_awal)
#         return data_awal


# def simpan_file(nama_file, data):
#     with open(nama_file, "w") as f:
#         json.dump(data, f, indent=4)


# def format_rupiah(angka):
#     if angka == 0:
#         return "Rp 0"
#     return f"Rp {angka:,.0f}".replace(",", ".")


# def generate_resi(data_paket):
#     nomor = len(data_paket) + 1
#     while True:
#         resi = f"EXP{nomor:03d}"
#         if not any(p["id"] == resi for p in data_paket):
#             return resi
#         nomor += 1


# def cari_di_tuple(tujuan_input, daftar_tuple):
#     for item in daftar_tuple:
#         if item.strip().lower() == tujuan_input.strip().lower():
#             return item
#     return None


# def cetak_struk(data):
#     biaya_mc = data.get("total_biaya", data.get("biaya_mc", 0))
#     tarif_mc = data.get("tarif_per_kg", 0)
#     print("\n" + "=" * 50)
#     print("           STRUK BUKTI PENGIRIMAN")
#     print("=" * 50)
#     print(f"ID Resi           : {data['id']}")
#     print(f"Username Akun     : {data.get('username', '-')}")
#     print(f"Nama Pemesan      : {data['nama']}")
#     print(f"Nomor HP          : {data['no_hp']}")
#     print(f"Kota Tujuan       : {data['tujuan']}")
#     print(f"Berat Barang      : {data['berat']} kg")
#     print(f"Jenis Rute        : {data.get('kategori', '-')}")
#     print(f"Tarif per kg      : {tarif_mc} MC")
#     print(f"Total Biaya       : {biaya_mc} MC")
#     print(f"Status Bayar      : {data.get('status_pembayaran', 'Belum Dibayar')}")
#     print(f"Status Pengiriman : {data['status']}")
#     print("=" * 50)
#     print("       * Simpan struk ini sebagai bukti resmi *")
#     print("=" * 50)


# def registrasi(data_user):
#     print("\n--- REGISTRASI AKUN BARU ---")
#     try:
#         username = input("Buat username : ").strip()
#     except KeyboardInterrupt:
#         print("\n[!] Registrasi dibatalkan.")
#         return
    
#     if username == "":
#         print("Username tidak boleh kosong!")
#         return
        
#     for user in data_user:
#         if user["username"].lower() == username.lower():
#             print("Username sudah dipakai, coba username lain!")
#             return
            
#     try:
#         try:
#             password = pwinput.pwinput("Buat password : ").strip()
#         except KeyboardInterrupt:
#             raise
#         except Exception:
#             password = input("Buat password : ").strip()
#     except KeyboardInterrupt:
#         print("\n[!] Registrasi dibatalkan.")
#         return

#     if len(password) < 4:
#         print("Password minimal 4 karakter!")
#         return
        
#     user_baru = {
#         "username": username,
#         "password": password,
#         "role": "user",
#         "saldo": 0  
#     }
    
#     data_user.append(user_baru)
#     simpan_file(file_user, data_user)
#     print("Akun berhasil didaftarkan sebagai User! Saldo awal: 0 MC. Silakan login.")


# def login(data_user):
#     print("\n--- LOGIN PENGGUNA ---")
#     try:    
#         username = input("Username : ").strip()
#     except KeyboardInterrupt:
#         print("\n[!] Login dibatalkan.")
#         return None

#     try:
#         try:
#             password = pwinput.pwinput("Password : ").strip()
#         except KeyboardInterrupt:
#             raise
#         except Exception:
#             password = input("Password : ").strip()
#     except KeyboardInterrupt:
#         print("\n[!] Login dibatalkan.")
#         return None
    
#     for user in data_user:
#         if user["username"].lower() == username.lower() and user["password"] == password: 
#             if "saldo" not in user:
#                 user["saldo"] = 0
#             print(f"\nLogin berhasil! Selamat datang, {user['username']} ({user['role'].upper()}).")
#             return user
            
#     print("Username atau password salah!")
#     return None


# def top_up_saldo(user_login, data_user):
#     print("\n========================================")
#     print("            TOP UP SALDO MC")
#     print("========================================")
#     print(f"Kurs Konversi  : 1 MC = {format_rupiah(KURS_MC_RUPIAH)}")
#     saldo_sekarang = user_login.get("saldo", 0)
#     print(f"Saldo Saat Ini : {saldo_sekarang} MC ({format_rupiah(saldo_sekarang * KURS_MC_RUPIAH)})")
#     print("========================================")
    
#     while True:
#         try:
#             input_rp = input("Masukkan nominal Rupiah yang ingin di-top up (contoh: 50000) atau '0' untuk batal: ").strip()
#         except KeyboardInterrupt:
#             print("\n[!] Top up dibatalkan.")
#             return

#         if input_rp == "0":
#             print("Top up dibatalkan.")
#             return
            
#         if not input_rp.isdigit():
#             print("Nominal harus berupa angka bulat positif!")
#             continue
            
#         nominal_rp = int(input_rp)
#         if nominal_rp < KURS_MC_RUPIAH:
#             print(f"Nominal minimal top up adalah {format_rupiah(KURS_MC_RUPIAH)} (1 MC)!")
#             continue
            
#         if nominal_rp % KURS_MC_RUPIAH != 0:
#             print(f"Nominal harus berupa kelipatan {format_rupiah(KURS_MC_RUPIAH)}! (Contoh: 10000, 25000, 50000)")
#             continue

#         if nominal_rp > 11000000:
#             print("Nominal top up maksimal adalah Rp 11.000.000!")
#             continue

#         mc_didapat = nominal_rp // KURS_MC_RUPIAH
#         break

#     print("\n--- Konfirmasi Top Up ---")
#     print(f"Nominal Bayar : {format_rupiah(nominal_rp)}")
#     print(f"MC Didapat    : +{mc_didapat} MC")
#     print(f"Total Saldo   : {saldo_sekarang + mc_didapat} MC")

#     try:
#         konfirmasi = input("Lanjutkan transaksi top up? (y/n): ").strip().lower()
#     except KeyboardInterrupt:
#         print("\n[!] Transaksi top up dibatalkan.")
#         return

#     if konfirmasi == "y":
#         user_login["saldo"] = saldo_sekarang + mc_didapat

#         for u in data_user:
#             if u["username"].lower() == user_login["username"].lower():
#                 u["saldo"] = user_login["saldo"]
#                 break
#         simpan_file(file_user, data_user)
        
#         print("\n" + "=" * 42)
#         print("           STRUK BUKTI TOP UP")
#         print("=" * 42)
#         print(f"Username Akun : {user_login['username']}")
#         print(f"Nominal Bayar : {format_rupiah(nominal_rp)}")
#         print(f"MC Masuk      : +{mc_didapat} MC")
#         print(f"Saldo Akhir   : {user_login['saldo']} MC ({format_rupiah(user_login['saldo'] * KURS_MC_RUPIAH)})")
#         print("Status        : BERHASIL")
#         print("=" * 42)
#         print("[+] Saldo MC berhasil ditambahkan dan tersimpan!")
#     else:
#         print("Transaksi top up dibatalkan.")


# def tampilkan_data(data_paket, filter_username=None):
#     bersihkan_layar()
    
#     if filter_username:
#         paket_tampil = [p for p in data_paket if p.get("username") == filter_username]
#         print(f"=== DAFTAR PENGIRIMAN SAYA ({filter_username}) ===")
#     else:
#         paket_tampil = data_paket
#         print("=== DAFTAR SEMUA DATA PENGIRIMAN (ADMIN) ===")
    
#     if len(paket_tampil) == 0:
#         print("Belum ada data pengiriman.")
#         return
        
#     tabel = PrettyTable()
#     tabel.field_names = ["No", "ID Resi", "Nama", "Tujuan", "Berat", "Total Biaya", "Status Bayar", "Status Pengiriman"]
    
#     tabel.align["No"] = "c"
#     tabel.align["ID Resi"] = "c"
#     tabel.align["Nama"] = "l"
#     tabel.align["Tujuan"] = "l"
#     tabel.align["Berat"] = "r"
#     tabel.align["Total Biaya"] = "r"
#     tabel.align["Status Bayar"] = "c"
#     tabel.align["Status Pengiriman"] = "l"

#     nomor = 1
#     for paket in paket_tampil:
#         biaya_mc = paket.get("total_biaya", paket.get("biaya_mc", 0))
#         tabel.add_row([
#             nomor,
#             paket["id"],
#             paket["nama"],
#             paket["tujuan"],
#             f"{paket['berat']} kg",
#             f"{biaya_mc} MC",
#             paket.get("status_pembayaran", "Belum Dibayar"),
#             paket["status"]
#         ])
#         nomor += 1
        
#     print(tabel)


# def ajukan_pengiriman_user(data_paket, user_login, data_user):
#     print("\n=== FORM PENGAJUAN PENGIRIMAN BARANG ===")
#     nama = user_login["username"]
#     print(f"Nama Pengirim/Pemesan : {nama}")
#     print(f"Saldo MC Anda Saat Ini: {user_login.get('saldo', 0)} MC")
        
#     try:
#         no_hp = input("Masukkan Nomor HP     : ")
#     except KeyboardInterrupt:
#         print("\n[!] Pengajuan dibatalkan.")
#         return

#     while not no_hp.isdigit() or int(no_hp) <= 0:
#         print("Nomor HP harus berupa angka lebih dari 0!")
#         try:
#             no_hp = input("Masukkan Nomor HP     : ")
#         except KeyboardInterrupt:
#             print("\n[!] Pengajuan dibatalkan.")
#             return

#     while True:
#         try:
#             input_berat = input("Masukkan berat barang (kg)     : ")
#             berat = float(input_berat.replace(",", "."))
#             if berat <= 0:
#                 print("Berat barang tidak valid! Harus lebih dari 0 kg.")
#                 continue
#             break
#         except ValueError:
#             print("Berat harus berupa angka!")
#         except KeyboardInterrupt:
#             print("\n[!] Pengajuan dibatalkan.")
#             return

#     while True:
#         try:
#             tujuan = input("Masukkan Kota Tujuan Pengiriman: ").strip()
#         except KeyboardInterrupt:
#             print("\n[!] Pengajuan dibatalkan.")
#             return
#         if tujuan == "":
#             print("Kota tujuan tidak boleh kosong!")
#             continue
#         break

#     id_resi = generate_resi(data_paket)
#     kota_antar = cari_di_tuple(tujuan, TUJUAN_ANTAR_PULAU)
#     kota_luar = cari_di_tuple(tujuan, TUJUAN_LUAR_PULAU)

#     if berat > 30:
#         kategori = "Antar Pulau" if kota_antar else ("Luar Pulau" if kota_luar else "-")
#         tujuan_resmi = kota_antar or kota_luar or tujuan
#         tarif_per_kg = TARIF_ANTAR_PULAU if kota_antar else (TARIF_LUAR_PULAU if kota_luar else 0)
#         total_biaya = int(berat * tarif_per_kg)

#         print(f"\n[-] Berat barang ({berat} kg) melebihi batas maksimal 30 kg!")
#         print("[-] PENGIRIMAN LANGSUNG DITOLAK.")
        
#         pengiriman_baru = {
#             "id": id_resi,
#             "username": user_login["username"],
#             "nama": nama,
#             "no_hp": no_hp,
#             "berat": berat,
#             "tujuan": tujuan_resmi,
#             "kategori": kategori,
#             "tarif_per_kg": tarif_per_kg,
#             "total_biaya": total_biaya,
#             "biaya_mc": total_biaya,
#             "status_pembayaran": "Batal (Ditolak)",
#             "status": "Ditolak (Kelebihan Berat > 30 kg)"
#         }
#         data_paket.append(pengiriman_baru)
#         simpan_file(file_pengiriman, data_paket)
#         cetak_struk(pengiriman_baru)
#         return

#     if not kota_antar and not kota_luar:
#         print(f"\n[-] Kota tujuan '{tujuan}' di luar rute jangkauan pengiriman!")
#         print("[-] PENGIRIMAN LANGSUNG DITOLAK.")
        
#         pengiriman_baru = {
#             "id": id_resi,
#             "username": user_login["username"],
#             "nama": nama,
#             "no_hp": no_hp,
#             "berat": berat,
#             "tujuan": tujuan,
#             "kategori": "-",
#             "tarif_per_kg": 0,
#             "total_biaya": 0,
#             "biaya_mc": 0,
#             "status_pembayaran": "Batal (Ditolak)",
#             "status": "Ditolak (Tujuan Tidak Terjangkau)"
#         }
#         data_paket.append(pengiriman_baru)
#         simpan_file(file_pengiriman, data_paket)
#         cetak_struk(pengiriman_baru)
#         return

#     if kota_antar:
#         kategori = "Antar Pulau"
#         tujuan_resmi = kota_antar
#         tarif_per_kg = TARIF_ANTAR_PULAU
#     else:
#         kategori = "Luar Pulau"
#         tujuan_resmi = kota_luar
#         tarif_per_kg = TARIF_LUAR_PULAU

#     total_biaya = int(berat * tarif_per_kg)
#     biaya_mc = total_biaya

#     print("\n" + "-" * 48)
#     print("            RINCIAN STRUK PESANAN")
#     print("-" * 48)
#     print(f"Kota Tujuan   : {tujuan_resmi} ({kategori})")
#     print(f"Berat Barang  : {berat} kg")
#     print(f"Tarif per kg  : {tarif_per_kg} MC")
#     print(f"Total Biaya   : {total_biaya} MC")
#     print("-" * 48)
#     print(f"Saldo MC Anda : {user_login.get('saldo', 0)} MC")
#     print("-" * 48)

#     status_bayar = "Belum Dibayar"

#     if user_login.get("saldo", 0) < biaya_mc:
#         print(f"[!] Saldo MC Anda TIDAK MENCUKUPI untuk membayar pesanan ini!")
#         print(f"[!] Saldo saat ini : {user_login.get('saldo', 0)} MC")
#         print(f"[!] Diperlukan     : {biaya_mc} MC (Kurang {biaya_mc - user_login.get('saldo', 0)} MC)")
#         print("[*] Silakan lakukan Top Up terlebih dahulu sebelum memesan.")
#         try:
#             pilihan = input("Apakah ingin menyimpan pengajuan ini dengan status 'Belum Dibayar'? (y/n): ").strip().lower()
#         except KeyboardInterrupt:
#             print("\n[!] Pengajuan pengiriman dibatalkan.")
#             return
#         if pilihan != "y":
#             print("Pengajuan pengiriman dibatalkan.")
#             return
#     else:
#         try:
#             konfirmasi = input(f"Lakukan pemesanan dan potong saldo sebesar {biaya_mc} MC? (y/n): ").strip().lower()
#         except KeyboardInterrupt:
#             print("\n[!] Pengajuan pengiriman dibatalkan.")
#             return
#         if konfirmasi == "y":
#             user_login["saldo"] -= biaya_mc
#             for u in data_user:
#                 if u["username"].lower() == user_login["username"].lower():
#                     u["saldo"] = user_login["saldo"]
#                     break
#             simpan_file(file_user, data_user)
#             status_bayar = "Lunas"
#             print(f"\n[+] PEMBAYARAN BERHASIL!")
#             print(f"[+] Saldo MC dipotong  : -{biaya_mc} MC")
#             print(f"[+] Sisa Saldo MC Anda : {user_login['saldo']} MC")
#         else:
#             print("Pengajuan dibatalkan.")
#             return

#     pengiriman_baru = {
#         "id": id_resi,
#         "username": user_login["username"],
#         "nama": nama,
#         "no_hp": no_hp,
#         "berat": berat,
#         "tujuan": tujuan_resmi,
#         "kategori": kategori,
#         "tarif_per_kg": tarif_per_kg,
#         "total_biaya": total_biaya,
#         "biaya_mc": biaya_mc,
#         "status_pembayaran": status_bayar,
#         "status": "Menunggu Validasi"
#     }

#     data_paket.append(pengiriman_baru)
#     simpan_file(file_pengiriman, data_paket)

#     print("\n[+] Pengajuan pengiriman berhasil dikirim!")
#     print(f"[+] ID Resi Anda : {id_resi}")
#     print("[*] Status saat ini: 'Menunggu Validasi' oleh Admin.")
#     cetak_struk(pengiriman_baru)


# def ajukan_pengiriman_admin(data_paket, admin_login):
#     print("\n=== INPUT PENGIRIMAN LANGSUNG (PELANGGAN OFFLINE / WALK-IN) ===")
    
#     while True:
#         try:
#             nama = input("Masukkan Nama Pengirim/Pemesan : ").strip()
#         except KeyboardInterrupt:
#             print("\n[!] Penginputan pengiriman dibatalkan.")
#             return
#         if nama == "":
#             print("Nama pengirim tidak boleh kosong!")
#             continue
#         break

#     try:
#         no_hp = input("Masukkan Nomor HP              : ").strip()
#     except KeyboardInterrupt:
#         print("\n[!] Penginputan pengiriman dibatalkan.")
#         return

#     while not no_hp.isdigit() or int(no_hp) <= 0:
#         print("Nomor HP harus berupa angka lebih dari 0!")
#         try:
#             no_hp = input("Masukkan Nomor HP              : ").strip()
#         except KeyboardInterrupt:
#             print("\n[!] Penginputan pengiriman dibatalkan.")
#             return

#     while True:
#         try:
#             input_berat = input("Masukkan berat barang (kg)      : ")
#             berat = float(input_berat.replace(",", "."))
#             if berat <= 0:
#                 print("Berat barang tidak valid! Harus lebih dari 0 kg.")
#                 continue
#             break
#         except ValueError:
#             print("Berat harus berupa angka!")
#         except KeyboardInterrupt:
#             print("\n[!] Penginputan pengiriman dibatalkan.")
#             return

#     while True:
#         try:
#             tujuan = input("Masukkan Kota Tujuan Pengiriman : ").strip()
#         except KeyboardInterrupt:
#             print("\n[!] Penginputan pengiriman dibatalkan.")
#             return
#         if tujuan == "":
#             print("Kota tujuan tidak boleh kosong!")
#             continue
#         break

#     id_resi = generate_resi(data_paket)
#     kota_antar = cari_di_tuple(tujuan, TUJUAN_ANTAR_PULAU)
#     kota_luar = cari_di_tuple(tujuan, TUJUAN_LUAR_PULAU)

#     if berat > 30:
#         kategori = "Antar Pulau" if kota_antar else ("Luar Pulau" if kota_luar else "-")
#         tujuan_resmi = kota_antar or kota_luar or tujuan
#         tarif_per_kg = TARIF_ANTAR_PULAU if kota_antar else (TARIF_LUAR_PULAU if kota_luar else 0)
#         total_biaya = int(berat * tarif_per_kg)

#         print(f"\n[-] Berat {berat} kg melebihi batas 30 kg! PENGIRIMAN LANGSUNG DITOLAK.")
#         pengiriman_baru = {
#             "id": id_resi,
#             "username": f"Walk-in ({nama})",
#             "nama": nama,
#             "no_hp": no_hp,
#             "berat": berat,
#             "tujuan": tujuan_resmi,
#             "kategori": kategori,
#             "tarif_per_kg": tarif_per_kg,
#             "total_biaya": total_biaya,
#             "biaya_mc": total_biaya,
#             "status_pembayaran": "Batal (Ditolak)",
#             "status": "Ditolak (Kelebihan Berat > 30 kg)"
#         }
#         data_paket.append(pengiriman_baru)
#         simpan_file(file_pengiriman, data_paket)
#         cetak_struk(pengiriman_baru)
#         return

#     if not kota_antar and not kota_luar:
#         print(f"\n[-] Kota '{tujuan}' di luar rute jangkauan! PENGIRIMAN LANGSUNG DITOLAK.")
#         pengiriman_baru = {
#             "id": id_resi,
#             "username": f"Walk-in ({nama})",
#             "nama": nama,
#             "no_hp": no_hp,
#             "berat": berat,
#             "tujuan": tujuan,
#             "kategori": "-",
#             "tarif_per_kg": 0,
#             "total_biaya": 0,
#             "biaya_mc": 0,
#             "status_pembayaran": "Batal (Ditolak)",
#             "status": "Ditolak (Tujuan Tidak Terjangkau)"
#         }
#         data_paket.append(pengiriman_baru)
#         simpan_file(file_pengiriman, data_paket)
#         cetak_struk(pengiriman_baru)
#         return

#     if kota_antar:
#         kategori = "Antar Pulau"
#         tujuan_resmi = kota_antar
#         tarif_per_kg = TARIF_ANTAR_PULAU
#     else:
#         kategori = "Luar Pulau"
#         tujuan_resmi = kota_luar
#         tarif_per_kg = TARIF_LUAR_PULAU

#     total_biaya = int(berat * tarif_per_kg)

#     print("\n" + "-" * 48)
#     print("            RINCIAN BIAYA PENGIRIMAN")
#     print("-" * 48)
#     print(f"Nama Pengirim : {nama}")
#     print(f"Kota Tujuan   : {tujuan_resmi} ({kategori})")
#     print(f"Berat Barang  : {berat} kg")
#     print(f"Tarif per kg  : {tarif_per_kg} MC")
#     print(f"Total Biaya   : {total_biaya} MC")
#     print(f"Status Bayar  : Lunas (Pembayaran Langsung)")
#     print("-" * 48)

#     try:
#         konfirmasi = input("Konfirmasi simpan dan proses pengiriman langsung ini? (y/n): ").strip().lower()
#     except KeyboardInterrupt:
#         print("\n[!] Penginputan pengiriman dibatalkan.")
#         return

#     if konfirmasi != "y":
#         print("Penginputan pengiriman dibatalkan.")
#         return

#     status_bayar = "Lunas"
#     status_paket = "Diterima (Diproses)"

#     pengiriman_baru = {
#         "id": id_resi,
#         "username": f"Walk-in ({nama})",
#         "nama": nama,
#         "no_hp": no_hp,
#         "berat": berat,
#         "tujuan": tujuan_resmi,
#         "kategori": kategori,
#         "tarif_per_kg": tarif_per_kg,
#         "total_biaya": total_biaya,
#         "biaya_mc": total_biaya,
#         "status_pembayaran": status_bayar,
#         "status": status_paket
#     }

#     data_paket.append(pengiriman_baru)
#     simpan_file(file_pengiriman, data_paket)

#     print("\n[+] Pengiriman langsung berhasil ditambahkan dan berstatus LUNAS!")
#     print(f"[+] ID Resi : {id_resi}")
#     cetak_struk(pengiriman_baru)


# def bayar_tagihan_user(data_paket, user_login, data_user):
#     print("\n=== PEMBAYARAN TAGIHAN PENGIRIMAN DENGAN SALDO MC ===")
#     tagihan = [
#         p for p in data_paket 
#         if p.get("username") == user_login["username"] 
#         and p.get("status_pembayaran") != "Lunas" 
#         and "Ditolak" not in p.get("status", "")
#         and p.get("total_biaya", 0) > 0
#     ]

#     if len(tagihan) == 0:
#         print("Tidak ada tagihan pengiriman aktif yang perlu dibayar.")
#         return

#     tabel = PrettyTable()
#     tabel.field_names = ["No", "ID Resi", "Tujuan", "Berat", "Total Biaya", "Status"]
#     nomor = 1
#     for p in tagihan:
#         tabel.add_row([
#             nomor, p["id"], p["tujuan"], f"{p['berat']} kg", 
#             f"{p.get('total_biaya', 0)} MC", 
#             p["status"]
#         ])
#         nomor += 1
#     print(tabel)

#     try:
#         cari_resi = input("\nMasukkan ID Resi yang ingin dibayar (atau '0' untuk batal): ").strip().upper()
#     except KeyboardInterrupt:
#         print("\n[!] Pembayaran dibatalkan.")
#         return

#     if cari_resi == "0":
#         return

#     target = next((p for p in tagihan if p["id"] == cari_resi), None)
#     if not target:
#         print("ID Resi tidak ditemukan dalam daftar tagihan Anda!")
#         return

#     biaya_mc = target.get("total_biaya", target.get("biaya_mc", 0))
#     saldo_sekarang = user_login.get("saldo", 0)

#     print(f"\nResi Target   : {target['id']} ({target['tujuan']})")
#     print(f"Total Tagihan : {biaya_mc} MC")
#     print(f"Saldo MC Anda : {saldo_sekarang} MC")

#     if saldo_sekarang < biaya_mc:
#         print(f"\n[!] Saldo MC Anda tidak cukup! Kurang {biaya_mc - saldo_sekarang} MC.")
#         print("[*] Silakan lakukan Top Up terlebih dahulu melalui menu Top Up.")
#         return

#     try:
#         konfirmasi = input(f"Konfirmasi pembayaran {biaya_mc} MC untuk resi {target['id']}? (y/n): ").strip().lower()
#     except KeyboardInterrupt:
#         print("\n[!] Pembayaran dibatalkan.")
#         return

#     if konfirmasi == "y":
#         user_login["saldo"] -= biaya_mc
#         for u in data_user:
#             if u["username"].lower() == user_login["username"].lower():
#                 u["saldo"] = user_login["saldo"]
#                 break
#         simpan_file(file_user, data_user)

#         target["status_pembayaran"] = "Lunas"
#         if target["status"] == "Diterima (Menunggu Pembayaran)":
#             target["status"] = "Diterima (Diproses)"
#         simpan_file(file_pengiriman, data_paket)

#         print("\n[+] PEMBAYARAN RESI BERHASIL!")
#         print(f"[+] Sisa Saldo MC Anda: {user_login['saldo']} MC")
#         cetak_struk(target)
#     else:
#         print("Pembayaran dibatalkan.")


# def validasi_pengiriman_admin(data_paket, data_user):
#     print("\n=== VALIDASI PENGAJUAN PENGIRIMAN DARI USER ===")
    
#     antrian = [p for p in data_paket if p["status"] == "Menunggu Validasi"]
    
#     if len(antrian) == 0:
#         print("Tidak ada pengajuan pengiriman yang menunggu validasi.")
#         return

#     tabel = PrettyTable()
#     tabel.field_names = ["No", "ID Resi", "Pemesan", "Tujuan", "Berat", "Status Bayar", "Status"]
#     nomor = 1
#     for p in antrian:
#         tabel.add_row([nomor, p["id"], p["nama"], p["tujuan"], f"{p['berat']} kg", p.get("status_pembayaran", "-"), p["status"]])
#         nomor += 1
#     print(tabel)

#     print("\nOpsi Validasi:")
#     print("1. Validasi Satu per Satu berdasarkan ID Resi")
#     print("2. Validasi Otomatis Semua Pengajuan Antrian")
#     print("0. Kembali")
    
#     try:
#         pilihan = input("Pilih menu validasi (0-2): ").strip()
#     except KeyboardInterrupt:
#         print("\n[!] Validasi dibatalkan.")
#         return

#     if pilihan == "1":
#         try:
#             cari_resi = input("Masukkan ID Resi yang ingin divalidasi: ").strip().upper()
#         except KeyboardInterrupt:
#             print("\n[!] Validasi dibatalkan.")
#             return

#         target = next((p for p in antrian if p["id"] == cari_resi), None)
#         if not target:
#             print("ID Resi tidak ditemukan dalam antrian validasi!")
#             return
#         eksekusi_validasi(target, data_user)
#         simpan_file(file_pengiriman, data_paket)
#         print(f"\n[+] Validasi resi {target['id']} selesai!")

#     elif pilihan == "2":
#         for p in antrian:
#             eksekusi_validasi(p, data_user)
#         simpan_file(file_pengiriman, data_paket)
#         print("\n[+] Seluruh pengajuan berhasil divalidasi otomatis!")


# def eksekusi_validasi(paket, data_user=None):
#     print(f"\n--- Memproses Validasi Resi: {paket['id']} ({paket['nama']}) ---")

#     if paket["berat"] > 30:
#         paket["status"] = "Ditolak (Kelebihan Berat > 30 kg)"
#         print(f"[-] Berat {paket['berat']} kg > 30 kg -> PENGIRIMAN DIBATALKAN / DITOLAK.")
#         return

#     print(f"[+] Berat {paket['berat']} kg memenuhi syarat (<= 30 kg). Melanjutkan validasi tujuan...")

#     kota_antar = cari_di_tuple(paket["tujuan"], TUJUAN_ANTAR_PULAU)
#     kota_luar = cari_di_tuple(paket["tujuan"], TUJUAN_LUAR_PULAU)

#     if kota_antar:
#         paket["kategori"] = "Antar Pulau"
#         paket["tujuan"] = kota_antar  
#         paket["tarif_per_kg"] = TARIF_ANTAR_PULAU
#         paket["total_biaya"] = int(paket["berat"] * TARIF_ANTAR_PULAU)
#         paket["biaya_mc"] = paket["total_biaya"]
#         if paket.get("status_pembayaran") == "Lunas":
#             paket["status"] = "Diterima (Diproses)"
#         else:
#             paket["status"] = "Diterima (Menunggu Pembayaran)"
#         print(f"[+] Tujuan '{kota_antar}' terdaftar (Kategori: Antar Pulau). Status: {paket['status']}.")
#     elif kota_luar:
#         paket["kategori"] = "Luar Pulau"
#         paket["tujuan"] = kota_luar  
#         paket["tarif_per_kg"] = TARIF_LUAR_PULAU
#         paket["total_biaya"] = int(paket["berat"] * TARIF_LUAR_PULAU)
#         paket["biaya_mc"] = paket["total_biaya"]
#         if paket.get("status_pembayaran") == "Lunas":
#             paket["status"] = "Diterima (Diproses)"
#         else:
#             paket["status"] = "Diterima (Menunggu Pembayaran)"
#         print(f"[+] Tujuan '{kota_luar}' terdaftar (Kategori: Luar Pulau). Status: {paket['status']}.")
#     else:
#         paket["status"] = "Ditolak (Tujuan Tidak Terjangkau)"
#         print(f"[-] Tujuan '{paket['tujuan']}' tidak ada dalam jangkauan rute. Status: DITOLAK.")


# def ubah_status_admin(data_paket):
#     print("\n--- UPDATE STATUS PENGIRIMAN ---")
#     tampilkan_data(data_paket)
    
#     try:
#         cari_id = input("\nMasukkan ID Resi yang ingin diupdate statusnya: ").strip().upper()
#     except KeyboardInterrupt:
#         print("\n[!] Update status dibatalkan.")
#         return

#     paket = next((p for p in data_paket if p["id"] == cari_id), None)
    
#     if not paket:
#         print("ID Resi tidak ditemukan!")
#         return

#     if "Ditolak" in paket["status"]:
#         print(f"[!] Paket ini telah berstatus '{paket['status']}' dan tidak dapat diproses lebih lanjut.")
#         return

#     print(f"\nID Resi       : {paket['id']}")
#     print(f"Nama Pemesan  : {paket['nama']}")
#     print(f"Status Saat Ini: {paket['status']}")
#     print(f"Status Bayar  : {paket.get('status_pembayaran', '-')}")
#     print("\nPilih status baru:")
#     print("1. Sedang Dikirim")
#     print("2. Sampai Tujuan")
#     print("3. Batalkan Pengiriman")

#     try:
#         pilih = input("Pilih (1/2/3): ").strip()
#     except KeyboardInterrupt:
#         print("\n[!] Update status dibatalkan.")
#         return
    
#     if pilih == "1":
#         paket["status"] = "Sedang Dikirim"
#     elif pilih == "2":
#             paket["status"] = "Sampai Tujuan"
#     elif pilih == "3":
#             paket["status"] = "Dibatalkan Admin"
#     else:
#             print("Pilihan tidak valid, pembaharuan dibatalkan!")
#             return
            
#     simpan_file(file_pengiriman, data_paket)
#     print(f"[+] Status resi {paket['id']} berhasil diupdate menjadi: {paket['status']}")


#     def hapus_data(data_paket):
#         print("\n--- HAPUS DATA PENGIRIMAN ---")
#         tampilkan_data(data_paket)
        
#         if len(data_paket) == 0:
#             return
            
#         try:
#             cari_id = input("\nMasukkan ID Resi yang mau dihapus: ").strip().upper()
#         except KeyboardInterrupt:
#             print("\n[!] Penghapusan data dibatalkan.")
#             return
        
#         for i in range(len(data_paket)):
#             if data_paket[i]["id"] == cari_id:
#                 try:
#                     konfirmasi = input(f"Apakah yakin menghapus resi {cari_id}? (y/n): ")
#                 except KeyboardInterrupt:
#                     print("\n[!] Penghapusan data dibatalkan.")
#                     return

#             if konfirmasi.lower() == "y":
#                 data_paket.pop(i)
#                 simpan_file(file_pengiriman, data_paket)
#                 print("Data berhasil dihapus!")
#             else:
#                 print("Penghapusan dibatalkan.")
#             return
            
#     print("ID Resi tidak ditemukan!")


# def menu_admin(user_login, data_user):
#     while True:
#         data_paket = baca_file(file_pengiriman, [])
#         print("\n========================================")
#         print("           DASHBOARD ADMIN")
#         print(f"Login sebagai: {user_login['username']} (ADMIN)")
#         print("========================================")
#         print("1. Lihat Semua Data Pengiriman")
#         print("2. Input Pengiriman Langsung (Pelanggan Offline / Walk-in)")
#         print("3. Validasi Pengajuan Pengiriman Baru (Validasi Berat & Tujuan)")
#         print("4. Update Status Perjalanan (Sedang Dikirim / Selesai)")
#         print("5. Hapus Data Pengiriman")
#         print("6. Logout")
#         print("========================================")
        
#         try:
#             pilihan = input("Pilih menu (1-6): ").strip()
#         except KeyboardInterrupt:
#             print("\n[!] Logout otomatis dari Admin.")
#             break
        
#         if pilihan == "1":
#             tampilkan_data(data_paket)
#             try:
#                 input("\nTekan Enter untuk kembali...")
#             except KeyboardInterrupt:
#                 print()
#         elif pilihan == "2":
#             ajukan_pengiriman_admin(data_paket, user_login)
#         elif pilihan == "3":
#             validasi_pengiriman_admin(data_paket, data_user)
#         elif pilihan == "4":
#             ubah_status_admin(data_paket)
#         elif pilihan == "5":
#             hapus_data (data_paket)
#         elif pilihan == "6":
#             print("Berhasil logout dari Admin.")
#             break
#         else:
#             print("Pilihan menu tidak valid!")


# def menu_user(user_login, data_user):
#     while True:
#         data_paket = baca_file(file_pengiriman, [])
#         saldo_sekarang = user_login.get("saldo", 0)
        
#         print("\n========================================")
#         print("           DASHBOARD PELANGGAN")
#         print(f"Login sebagai : {user_login['username']} (USER)")
#         print(f"Saldo MC Anda : {saldo_sekarang} MC ({format_rupiah(saldo_sekarang * KURS_MC_RUPIAH)})")
#         print("========================================")
#         print("1. Cek Status Pengiriman Saya")
#         print("2. Ajukan Pengiriman Barang Baru")
#         print("3. Bayar Tagihan Pengiriman (Sesuai Struk)")
#         print("4. Cetak Struk Bukti Pengiriman")
#         print("5. Top Up Saldo MC (1 MC = Rp 1.000)")
#         print("6. Logout")
#         print("========================================")
        
#         try:
#             pilihan = input("Pilih menu (1-6): ").strip()
#         except KeyboardInterrupt:
#             print("\n[!] Logout otomatis dari User.")
#             break
        
#         if pilihan == "1":
#             tampilkan_data(data_paket, filter_username=user_login["username"])
#             try:
#                 input("\nTekan Enter untuk kembali...")
#             except KeyboardInterrupt:
#                 print()
#         elif pilihan == "2":
#             ajukan_pengiriman_user(data_paket, user_login, data_user)
#         elif pilihan == "3":
#             bayar_tagihan_user(data_paket, user_login, data_user)
#         elif pilihan == "4":
#             tampilkan_data(data_paket, filter_username=user_login["username"])
#             try:
#                 cari_id = input("\nMasukkan ID Resi yang ingin dicetak struknya: ").strip().upper()
#             except KeyboardInterrupt:
#                 print("\n[!] Batal mencetak struk.")
#                 continue

#             paket = next((p for p in data_paket if p["id"] == cari_id and p.get("username") == user_login["username"]), None)
#             if paket:
#                 cetak_struk(paket)
#             else:
#                 print("ID Resi tidak ditemukan atau bukan milik akun Anda!")
#             try:
#                 input("\nTekan Enter untuk kembali...")
#             except KeyboardInterrupt:
#                 print()
#         elif pilihan == "5":
#             top_up_saldo(user_login, data_user)
#         elif pilihan == "6":
#             print("Berhasil logout dari User.")
#             break
#         else:
#             print("Pilihan menu tidak valid!")


# def main():
#     data_awal_user = [
#         {"username": "admin", "password": "123", "role": "admin", "saldo": 0}
#     ]
#     data_user = baca_file(file_user, data_awal_user)
    
#     for u in data_user:
#         if "saldo" not in u:
#             u["saldo"] = 0
#     simpan_file(file_user, data_user)

#     while True:
#         print("\n==================================")
#         print("  SISTEM PENGIRIMAN KARGO LOGISTIK")
#         print("==================================")
#         print("1. Login")
#         print("2. Registrasi (User Baru)")
#         print("3. Keluar")
#         print("==================================")
        
#         try:
#             pilihan = input("Pilih menu (1-3): ").strip()
#         except KeyboardInterrupt:
#             print("\n\nTerima kasih sudah menggunakan program ini.")
#             break
        
#         if pilihan == "1":
#             user_login = login(data_user)
#             if user_login:
#                 if user_login["role"] == "admin":
#                     menu_admin(user_login, data_user)
#                 else:
#                     menu_user(user_login, data_user)
#         elif pilihan == "2":
#             registrasi(data_user)
#         elif pilihan == "3":
#             print("Terima kasih sudah menggunakan program ini.")
#             break
#         else:
#             print("Pilihan salah, masukkan angka 1 sampai 3!")


# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\n\nProgram dihentikan oleh pengguna.")



import os
import json
import time
import pwinput
from prettytable import PrettyTable

try:
    from Projek import hapus_data
except ImportError:
    pass

file_user = "users.json"
file_pengiriman = "pengiriman.json"

TUJUAN_ANTAR_PULAU = (
    "Samarinda",
    "Pontianak",
    "Palangkaraya",
    "Banjarmasin",
    "Tanjung Selor"
)

TUJUAN_LUAR_PULAU = (
    "Jakarta",
    "Banda Aceh",
    "Palembang",
    "Bali",
    "Papua",
    "Makassar"
)

# Tarif langsung dalam satuan MC
TARIF_ANTAR_PULAU = 15 
TARIF_LUAR_PULAU = 35  
KURS_MC_RUPIAH = 1000  # Kurs khusus untuk menu Top Up saldo


def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def loading_dashboard(role=""):
    """Memberikan delay loading 3 detik dengan animasi titik sebelum masuk dashboard"""
    pesan = f"Sedang mengalihkan ke Dashboard {role.upper()}" if role else "Sedang memuat dashboard"
    print(f"\n{pesan}", end="", flush=True)
    try:
        for _ in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
        print("\n")
    except KeyboardInterrupt:
        print("\n")


def baca_file(nama_file, data_awal):
    if not os.path.exists(nama_file):
        simpan_file(nama_file, data_awal)
        return data_awal
    
    try:
        with open(nama_file, "r") as f:
            data = json.load(f)
            return data
    except Exception:
        simpan_file(nama_file, data_awal)
        return data_awal


def simpan_file(nama_file, data):
    with open(nama_file, "w") as f:
        json.dump(data, f, indent=4)


def format_rupiah(angka):
    if angka == 0:
        return "Rp 0"
    return f"Rp {angka:,.0f}".replace(",", ".")


def generate_resi(data_paket):
    nomor = len(data_paket) + 1
    while True:
        resi = f"EXP{nomor:03d}"
        if not any(p["id"] == resi for p in data_paket):
            return resi
        nomor += 1


def cari_di_tuple(tujuan_input, daftar_tuple):
    for item in daftar_tuple:
        if item.strip().lower() == tujuan_input.strip().lower():
            return item
    return None


def cetak_struk(data):
    biaya_mc = data.get("total_biaya", data.get("biaya_mc", 0))
    tarif_mc = data.get("tarif_per_kg", 0)
    print("\n" + "=" * 50)
    print("           STRUK BUKTI PENGIRIMAN")
    print("=" * 50)
    print(f"ID Resi           : {data['id']}")
    print(f"Username Akun     : {data.get('username', '-')}")
    print(f"Nama Pemesan      : {data['nama']}")
    print(f"Nomor HP          : {data['no_hp']}")
    print(f"Kota Tujuan       : {data['tujuan']}")
    print(f"Berat Barang      : {data['berat']} kg")
    print(f"Jenis Rute        : {data.get('kategori', '-')}")
    print(f"Tarif per kg      : {tarif_mc} MC")
    print(f"Total Biaya       : {biaya_mc} MC")
    print(f"Status Bayar      : {data.get('status_pembayaran', 'Belum Dibayar')}")
    print(f"Status Pengiriman : {data['status']}")
    print("=" * 50)
    print("       * Simpan struk ini sebagai bukti resmi *")
    print("=" * 50)


def registrasi(data_user):
    print("\n--- REGISTRASI AKUN BARU ---")
    try:
        username = input("Buat username : ").strip()
    except KeyboardInterrupt:
        print("\n[!] Registrasi dibatalkan.")
        return
    
    if username == "":
        print("Username tidak boleh kosong!")
        return
        
    for user in data_user:
        if user["username"].lower() == username.lower():
            print("Username sudah dipakai, coba username lain!")
            return
            
    try:
        try:
            password = pwinput.pwinput("Buat password : ").strip()
        except KeyboardInterrupt:
            raise
        except Exception:
            password = input("Buat password : ").strip()
    except KeyboardInterrupt:
        print("\n[!] Registrasi dibatalkan.")
        return

    if len(password) < 4:
        print("Password minimal 4 karakter!")
        return
        
    user_baru = {
        "username": username,
        "password": password,
        "role": "user",
        "saldo": 0  
    }
    
    data_user.append(user_baru)
    simpan_file(file_user, data_user)
    print("Akun berhasil didaftarkan sebagai User! Saldo awal: 0 MC. Silakan login.")


def login(data_user):
    print("\n--- LOGIN PENGGUNA ---")
    try:    
        username = input("Username : ").strip()
    except KeyboardInterrupt:
        print("\n[!] Login dibatalkan.")
        return None

    try:
        try:
            password = pwinput.pwinput("Password : ").strip()
        except KeyboardInterrupt:
            raise
        except Exception:
            password = input("Password : ").strip()
    except KeyboardInterrupt:
        print("\n[!] Login dibatalkan.")
        return None
    
    for user in data_user:
        if user["username"].lower() == username.lower() and user["password"] == password: 
            if "saldo" not in user:
                user["saldo"] = 0
            print(f"\nLogin berhasil! Selamat datang, {user['username']} ({user['role'].upper()}).")
            
            # Loading screen 3 detik sebelum masuk dashboard
            loading_dashboard(user["role"])
            return user
            
    print("Username atau password salah!")
    return None


def top_up_saldo(user_login, data_user):
    print("\n========================================")
    print("            TOP UP SALDO MC")
    print("========================================")
    print(f"Kurs Konversi  : 1 MC = {format_rupiah(KURS_MC_RUPIAH)}")
    saldo_sekarang = user_login.get("saldo", 0)
    print(f"Saldo Saat Ini : {saldo_sekarang} MC ({format_rupiah(saldo_sekarang * KURS_MC_RUPIAH)})")
    print("========================================")
    
    while True:
        try:
            input_rp = input("Masukkan nominal Rupiah yang ingin di-top up (contoh: 50000) atau '0' untuk batal: ").strip()
        except KeyboardInterrupt:
            print("\n[!] Top up dibatalkan.")
            return

        if input_rp == "0":
            print("Top up dibatalkan.")
            return
            
        if not input_rp.isdigit():
            print("Nominal harus berupa angka bulat positif!")
            continue
            
        nominal_rp = int(input_rp)
        if nominal_rp < KURS_MC_RUPIAH:
            print(f"Nominal minimal top up adalah {format_rupiah(KURS_MC_RUPIAH)} (1 MC)!")
            continue
            
        if nominal_rp % KURS_MC_RUPIAH != 0:
            print(f"Nominal harus berupa kelipatan {format_rupiah(KURS_MC_RUPIAH)}! (Contoh: 10000, 25000, 50000)")
            continue

        if nominal_rp > 11000000:
            print("Nominal top up maksimal adalah Rp 11.000.000!")
            continue

        mc_didapat = nominal_rp // KURS_MC_RUPIAH
        break

    print("\n--- Konfirmasi Top Up ---")
    print(f"Nominal Bayar : {format_rupiah(nominal_rp)}")
    print(f"MC Didapat    : +{mc_didapat} MC")
    print(f"Total Saldo   : {saldo_sekarang + mc_didapat} MC")

    try:
        konfirmasi = input("Lanjutkan transaksi top up? (y/n): ").strip().lower()
    except KeyboardInterrupt:
        print("\n[!] Transaksi top up dibatalkan.")
        return

    if konfirmasi == "y":
        user_login["saldo"] = saldo_sekarang + mc_didapat

        for u in data_user:
            if u["username"].lower() == user_login["username"].lower():
                u["saldo"] = user_login["saldo"]
                break
        simpan_file(file_user, data_user)
        
        print("\n" + "=" * 42)
        print("           STRUK BUKTI TOP UP")
        print("=" * 42)
        print(f"Username Akun : {user_login['username']}")
        print(f"Nominal Bayar : {format_rupiah(nominal_rp)}")
        print(f"MC Masuk      : +{mc_didapat} MC")
        print(f"Saldo Akhir   : {user_login['saldo']} MC ({format_rupiah(user_login['saldo'] * KURS_MC_RUPIAH)})")
        print("Status        : BERHASIL")
        print("=" * 42)
        print("[+] Saldo MC berhasil ditambahkan dan tersimpan!")
    else:
        print("Transaksi top up dibatalkan.")


def tampilkan_data(data_paket, filter_username=None):
    bersihkan_layar()
    
    if filter_username:
        paket_tampil = [p for p in data_paket if p.get("username") == filter_username]
        print(f"=== DAFTAR PENGIRIMAN SAYA ({filter_username}) ===")
    else:
        paket_tampil = data_paket
        print("=== DAFTAR SEMUA DATA PENGIRIMAN (ADMIN) ===")
    
    if len(paket_tampil) == 0:
        print("Belum ada data pengiriman.")
        return
        
    tabel = PrettyTable()
    tabel.field_names = ["No", "ID Resi", "Nama", "Tujuan", "Berat", "Total Biaya", "Status Bayar", "Status Pengiriman"]
    
    tabel.align["No"] = "c"
    tabel.align["ID Resi"] = "c"
    tabel.align["Nama"] = "l"
    tabel.align["Tujuan"] = "l"
    tabel.align["Berat"] = "r"
    tabel.align["Total Biaya"] = "r"
    tabel.align["Status Bayar"] = "c"
    tabel.align["Status Pengiriman"] = "l"

    nomor = 1
    for paket in paket_tampil:
        biaya_mc = paket.get("total_biaya", paket.get("biaya_mc", 0))
        tabel.add_row([
            nomor,
            paket["id"],
            paket["nama"],
            paket["tujuan"],
            f"{paket['berat']} kg",
            f"{biaya_mc} MC",
            paket.get("status_pembayaran", "Belum Dibayar"),
            paket["status"]
        ])
        nomor += 1
        
    print(tabel)


def ajukan_pengiriman_user(data_paket, user_login, data_user):
    print("\n=== FORM PENGAJUAN PENGIRIMAN BARANG ===")
    nama = user_login["username"]
    print(f"Nama Pengirim/Pemesan : {nama}")
    print(f"Saldo MC Anda Saat Ini: {user_login.get('saldo', 0)} MC")
        
    try:
        no_hp = input("Masukkan Nomor HP     : ")
    except KeyboardInterrupt:
        print("\n[!] Pengajuan dibatalkan.")
        return

    while not no_hp.isdigit() or int(no_hp) <= 0:
        print("Nomor HP harus berupa angka lebih dari 0!")
        try:
            no_hp = input("Masukkan Nomor HP     : ")
        except KeyboardInterrupt:
            print("\n[!] Pengajuan dibatalkan.")
            return

    while True:
        try:
            input_berat = input("Masukkan berat barang (kg)     : ")
            berat = float(input_berat.replace(",", "."))
            if berat <= 0:
                print("Berat barang tidak valid! Harus lebih dari 0 kg.")
                continue
            break
        except ValueError:
            print("Berat harus berupa angka!")
        except KeyboardInterrupt:
            print("\n[!] Pengajuan dibatalkan.")
            return

    while True:
        try:
            tujuan = input("Masukkan Kota Tujuan Pengiriman: ").strip()
        except KeyboardInterrupt:
            print("\n[!] Pengajuan dibatalkan.")
            return
        if tujuan == "":
            print("Kota tujuan tidak boleh kosong!")
            continue
        break

    id_resi = generate_resi(data_paket)
    kota_antar = cari_di_tuple(tujuan, TUJUAN_ANTAR_PULAU)
    kota_luar = cari_di_tuple(tujuan, TUJUAN_LUAR_PULAU)

    if berat > 30:
        kategori = "Antar Pulau" if kota_antar else ("Luar Pulau" if kota_luar else "-")
        tujuan_resmi = kota_antar or kota_luar or tujuan
        tarif_per_kg = TARIF_ANTAR_PULAU if kota_antar else (TARIF_LUAR_PULAU if kota_luar else 0)
        total_biaya = int(berat * tarif_per_kg)

        print(f"\n[-] Berat barang ({berat} kg) melebihi batas maksimal 30 kg!")
        print("[-] PENGIRIMAN LANGSUNG DITOLAK.")
        
        pengiriman_baru = {
            "id": id_resi,
            "username": user_login["username"],
            "nama": nama,
            "no_hp": no_hp,
            "berat": berat,
            "tujuan": tujuan_resmi,
            "kategori": kategori,
            "tarif_per_kg": tarif_per_kg,
            "total_biaya": total_biaya,
            "biaya_mc": total_biaya,
            "status_pembayaran": "Batal (Ditolak)",
            "status": "Ditolak (Kelebihan Berat > 30 kg)"
        }
        data_paket.append(pengiriman_baru)
        simpan_file(file_pengiriman, data_paket)
        cetak_struk(pengiriman_baru)
        return

    if not kota_antar and not kota_luar:
        print(f"\n[-] Kota tujuan '{tujuan}' di luar rute jangkauan pengiriman!")
        print("[-] PENGIRIMAN LANGSUNG DITOLAK.")
        
        pengiriman_baru = {
            "id": id_resi,
            "username": user_login["username"],
            "nama": nama,
            "no_hp": no_hp,
            "berat": berat,
            "tujuan": tujuan,
            "kategori": "-",
            "tarif_per_kg": 0,
            "total_biaya": 0,
            "biaya_mc": 0,
            "status_pembayaran": "Batal (Ditolak)",
            "status": "Ditolak (Tujuan Tidak Terjangkau)"
        }
        data_paket.append(pengiriman_baru)
        simpan_file(file_pengiriman, data_paket)
        cetak_struk(pengiriman_baru)
        return

    if kota_antar:
        kategori = "Antar Pulau"
        tujuan_resmi = kota_antar
        tarif_per_kg = TARIF_ANTAR_PULAU
    else:
        kategori = "Luar Pulau"
        tujuan_resmi = kota_luar
        tarif_per_kg = TARIF_LUAR_PULAU

    total_biaya = int(berat * tarif_per_kg)
    biaya_mc = total_biaya

    print("\n" + "-" * 48)
    print("            RINCIAN STRUK PESANAN")
    print("-" * 48)
    print(f"Kota Tujuan   : {tujuan_resmi} ({kategori})")
    print(f"Berat Barang  : {berat} kg")
    print(f"Tarif per kg  : {tarif_per_kg} MC")
    print(f"Total Biaya   : {total_biaya} MC")
    print("-" * 48)
    print(f"Saldo MC Anda : {user_login.get('saldo', 0)} MC")
    print("-" * 48)

    status_bayar = "Belum Dibayar"

    if user_login.get("saldo", 0) < biaya_mc:
        print(f"[!] Saldo MC Anda TIDAK MENCUKUPI untuk membayar pesanan ini!")
        print(f"[!] Saldo saat ini : {user_login.get('saldo', 0)} MC")
        print(f"[!] Diperlukan     : {biaya_mc} MC (Kurang {biaya_mc - user_login.get('saldo', 0)} MC)")
        print("[*] Silakan lakukan Top Up terlebih dahulu sebelum memesan.")
        try:
            pilihan = input("Apakah ingin menyimpan pengajuan ini dengan status 'Belum Dibayar'? (y/n): ").strip().lower()
        except KeyboardInterrupt:
            print("\n[!] Pengajuan pengiriman dibatalkan.")
            return
        if pilihan != "y":
            print("Pengajuan pengiriman dibatalkan.")
            return
    else:
        try:
            konfirmasi = input(f"Lakukan pemesanan dan potong saldo sebesar {biaya_mc} MC? (y/n): ").strip().lower()
        except KeyboardInterrupt:
            print("\n[!] Pengajuan pengiriman dibatalkan.")
            return
        if konfirmasi == "y":
            user_login["saldo"] -= biaya_mc
            for u in data_user:
                if u["username"].lower() == user_login["username"].lower():
                    u["saldo"] = user_login["saldo"]
                    break
            simpan_file(file_user, data_user)
            status_bayar = "Lunas"
            print(f"\n[+] PEMBAYARAN BERHASIL!")
            print(f"[+] Saldo MC dipotong  : -{biaya_mc} MC")
            print(f"[+] Sisa Saldo MC Anda : {user_login['saldo']} MC")
        else:
            print("Pengajuan dibatalkan.")
            return

    pengiriman_baru = {
        "id": id_resi,
        "username": user_login["username"],
        "nama": nama,
        "no_hp": no_hp,
        "berat": berat,
        "tujuan": tujuan_resmi,
        "kategori": kategori,
        "tarif_per_kg": tarif_per_kg,
        "total_biaya": total_biaya,
        "biaya_mc": biaya_mc,
        "status_pembayaran": status_bayar,
        "status": "Menunggu Validasi"
    }

    data_paket.append(pengiriman_baru)
    simpan_file(file_pengiriman, data_paket)

    print("\n[+] Pengajuan pengiriman berhasil dikirim!")
    print(f"[+] ID Resi Anda : {id_resi}")
    print("[*] Status saat ini: 'Menunggu Validasi' oleh Admin.")
    cetak_struk(pengiriman_baru)


def ajukan_pengiriman_admin(data_paket, admin_login):
    print("\n=== INPUT PENGIRIMAN LANGSUNG (PELANGGAN OFFLINE / WALK-IN) ===")
    
    while True:
        try:
            nama = input("Masukkan Nama Pengirim/Pemesan : ").strip()
        except KeyboardInterrupt:
            print("\n[!] Penginputan pengiriman dibatalkan.")
            return
        if nama == "":
            print("Nama pengirim tidak boleh kosong!")
            continue
        break

    try:
        no_hp = input("Masukkan Nomor HP              : ").strip()
    except KeyboardInterrupt:
        print("\n[!] Penginputan pengiriman dibatalkan.")
        return

    while not no_hp.isdigit() or int(no_hp) <= 0:
        print("Nomor HP harus berupa angka lebih dari 0!")
        try:
            no_hp = input("Masukkan Nomor HP              : ").strip()
        except KeyboardInterrupt:
            print("\n[!] Penginputan pengiriman dibatalkan.")
            return

    while True:
        try:
            input_berat = input("Masukkan berat barang (kg)      : ")
            berat = float(input_berat.replace(",", "."))
            if berat <= 0:
                print("Berat barang tidak valid! Harus lebih dari 0 kg.")
                continue
            break
        except ValueError:
            print("Berat harus berupa angka!")
        except KeyboardInterrupt:
            print("\n[!] Penginputan pengiriman dibatalkan.")
            return

    while True:
        try:
            tujuan = input("Masukkan Kota Tujuan Pengiriman : ").strip()
        except KeyboardInterrupt:
            print("\n[!] Penginputan pengiriman dibatalkan.")
            return
        if tujuan == "":
            print("Kota tujuan tidak boleh kosong!")
            continue
        break

    id_resi = generate_resi(data_paket)
    kota_antar = cari_di_tuple(tujuan, TUJUAN_ANTAR_PULAU)
    kota_luar = cari_di_tuple(tujuan, TUJUAN_LUAR_PULAU)

    if berat > 30:
        kategori = "Antar Pulau" if kota_antar else ("Luar Pulau" if kota_luar else "-")
        tujuan_resmi = kota_antar or kota_luar or tujuan
        tarif_per_kg = TARIF_ANTAR_PULAU if kota_antar else (TARIF_LUAR_PULAU if kota_luar else 0)
        total_biaya = int(berat * tarif_per_kg)

        print(f"\n[-] Berat {berat} kg melebihi batas 30 kg! PENGIRIMAN LANGSUNG DITOLAK.")
        pengiriman_baru = {
            "id": id_resi,
            "username": f"Walk-in ({nama})",
            "nama": nama,
            "no_hp": no_hp,
            "berat": berat,
            "tujuan": tujuan_resmi,
            "kategori": kategori,
            "tarif_per_kg": tarif_per_kg,
            "total_biaya": total_biaya,
            "biaya_mc": total_biaya,
            "status_pembayaran": "Batal (Ditolak)",
            "status": "Ditolak (Kelebihan Berat > 30 kg)"
        }
        data_paket.append(pengiriman_baru)
        simpan_file(file_pengiriman, data_paket)
        cetak_struk(pengiriman_baru)
        return

    if not kota_antar and not kota_luar:
        print(f"\n[-] Kota '{tujuan}' di luar rute jangkauan! PENGIRIMAN LANGSUNG DITOLAK.")
        pengiriman_baru = {
            "id": id_resi,
            "username": f"Walk-in ({nama})",
            "nama": nama,
            "no_hp": no_hp,
            "berat": berat,
            "tujuan": tujuan,
            "kategori": "-",
            "tarif_per_kg": 0,
            "total_biaya": 0,
            "biaya_mc": 0,
            "status_pembayaran": "Batal (Ditolak)",
            "status": "Ditolak (Tujuan Tidak Terjangkau)"
        }
        data_paket.append(pengiriman_baru)
        simpan_file(file_pengiriman, data_paket)
        cetak_struk(pengiriman_baru)
        return

    if kota_antar:
        kategori = "Antar Pulau"
        tujuan_resmi = kota_antar
        tarif_per_kg = TARIF_ANTAR_PULAU
    else:
        kategori = "Luar Pulau"
        tujuan_resmi = kota_luar
        tarif_per_kg = TARIF_LUAR_PULAU

    total_biaya = int(berat * tarif_per_kg)

    print("\n" + "-" * 48)
    print("            RINCIAN BIAYA PENGIRIMAN")
    print("-" * 48)
    print(f"Nama Pengirim : {nama}")
    print(f"Kota Tujuan   : {tujuan_resmi} ({kategori})")
    print(f"Berat Barang  : {berat} kg")
    print(f"Tarif per kg  : {tarif_per_kg} MC")
    print(f"Total Biaya   : {total_biaya} MC")
    print(f"Status Bayar  : Lunas (Pembayaran Langsung)")
    print("-" * 48)

    try:
        konfirmasi = input("Konfirmasi simpan dan proses pengiriman langsung ini? (y/n): ").strip().lower()
    except KeyboardInterrupt:
        print("\n[!] Penginputan pengiriman dibatalkan.")
        return

    if konfirmasi != "y":
        print("Penginputan pengiriman dibatalkan.")
        return

    status_bayar = "Lunas"
    status_paket = "Diterima (Diproses)"

    pengiriman_baru = {
        "id": id_resi,
        "username": f"Walk-in ({nama})",
        "nama": nama,
        "no_hp": no_hp,
        "berat": berat,
        "tujuan": tujuan_resmi,
        "kategori": kategori,
        "tarif_per_kg": tarif_per_kg,
        "total_biaya": total_biaya,
        "biaya_mc": total_biaya,
        "status_pembayaran": status_bayar,
        "status": status_paket
    }

    data_paket.append(pengiriman_baru)
    simpan_file(file_pengiriman, data_paket)

    print("\n[+] Pengiriman langsung berhasil ditambahkan dan berstatus LUNAS!")
    print(f"[+] ID Resi : {id_resi}")
    cetak_struk(pengiriman_baru)


def bayar_tagihan_user(data_paket, user_login, data_user):
    print("\n=== PEMBAYARAN TAGIHAN PENGIRIMAN DENGAN SALDO MC ===")
    tagihan = [
        p for p in data_paket 
        if p.get("username") == user_login["username"] 
        and p.get("status_pembayaran") != "Lunas" 
        and "Ditolak" not in p.get("status", "")
        and p.get("total_biaya", 0) > 0
    ]

    if len(tagihan) == 0:
        print("Tidak ada tagihan pengiriman aktif yang perlu dibayar.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "ID Resi", "Tujuan", "Berat", "Total Biaya", "Status"]
    nomor = 1
    for p in tagihan:
        tabel.add_row([
            nomor, p["id"], p["tujuan"], f"{p['berat']} kg", 
            f"{p.get('total_biaya', 0)} MC", 
            p["status"]
        ])
        nomor += 1
    print(tabel)

    try:
        cari_resi = input("\nMasukkan ID Resi yang ingin dibayar (atau '0' untuk batal): ").strip().upper()
    except KeyboardInterrupt:
        print("\n[!] Pembayaran dibatalkan.")
        return

    if cari_resi == "0":
        return

    target = next((p for p in tagihan if p["id"] == cari_resi), None)
    if not target:
        print("ID Resi tidak ditemukan dalam daftar tagihan Anda!")
        return

    biaya_mc = target.get("total_biaya", target.get("biaya_mc", 0))
    saldo_sekarang = user_login.get("saldo", 0)

    print(f"\nResi Target   : {target['id']} ({target['tujuan']})")
    print(f"Total Tagihan : {biaya_mc} MC")
    print(f"Saldo MC Anda : {saldo_sekarang} MC")

    if saldo_sekarang < biaya_mc:
        print(f"\n[!] Saldo MC Anda tidak cukup! Kurang {biaya_mc - saldo_sekarang} MC.")
        print("[*] Silakan lakukan Top Up terlebih dahulu melalui menu Top Up.")
        return

    try:
        konfirmasi = input(f"Konfirmasi pembayaran {biaya_mc} MC untuk resi {target['id']}? (y/n): ").strip().lower()
    except KeyboardInterrupt:
        print("\n[!] Pembayaran dibatalkan.")
        return

    if konfirmasi == "y":
        user_login["saldo"] -= biaya_mc
        for u in data_user:
            if u["username"].lower() == user_login["username"].lower():
                u["saldo"] = user_login["saldo"]
                break
        simpan_file(file_user, data_user)

        target["status_pembayaran"] = "Lunas"
        if target["status"] == "Diterima (Menunggu Pembayaran)":
            target["status"] = "Diterima (Diproses)"
        simpan_file(file_pengiriman, data_paket)

        print("\n[+] PEMBAYARAN RESI BERHASIL!")
        print(f"[+] Sisa Saldo MC Anda: {user_login['saldo']} MC")
        cetak_struk(target)
    else:
        print("Pembayaran dibatalkan.")


def validasi_pengiriman_admin(data_paket, data_user):
    print("\n=== VALIDASI PENGAJUAN PENGIRIMAN DARI USER ===")
    
    antrian = [p for p in data_paket if p["status"] == "Menunggu Validasi"]
    
    if len(antrian) == 0:
        print("Tidak ada pengajuan pengiriman yang menunggu validasi.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "ID Resi", "Pemesan", "Tujuan", "Berat", "Status Bayar", "Status"]
    nomor = 1
    for p in antrian:
        tabel.add_row([nomor, p["id"], p["nama"], p["tujuan"], f"{p['berat']} kg", p.get("status_pembayaran", "-"), p["status"]])
        nomor += 1
    print(tabel)

    print("\nOpsi Validasi:")
    print("1. Validasi Satu per Satu berdasarkan ID Resi")
    print("2. Validasi Otomatis Semua Pengajuan Antrian")
    print("0. Kembali")
    
    try:
        pilihan = input("Pilih menu validasi (0-2): ").strip()
    except KeyboardInterrupt:
        print("\n[!] Validasi dibatalkan.")
        return

    if pilihan == "1":
        try:
            cari_resi = input("Masukkan ID Resi yang ingin divalidasi: ").strip().upper()
        except KeyboardInterrupt:
            print("\n[!] Validasi dibatalkan.")
            return

        target = next((p for p in antrian if p["id"] == cari_resi), None)
        if not target:
            print("ID Resi tidak ditemukan dalam antrian validasi!")
            return
        eksekusi_validasi(target, data_user)
        simpan_file(file_pengiriman, data_paket)
        print(f"\n[+] Validasi resi {target['id']} selesai!")

    elif pilihan == "2":
        for p in antrian:
            eksekusi_validasi(p, data_user)
        simpan_file(file_pengiriman, data_paket)
        print("\n[+] Seluruh pengajuan berhasil divalidasi otomatis!")


def eksekusi_validasi(paket, data_user=None):
    print(f"\n--- Memproses Validasi Resi: {paket['id']} ({paket['nama']}) ---")

    if paket["berat"] > 30:
        paket["status"] = "Ditolak (Kelebihan Berat > 30 kg)"
        print(f"[-] Berat {paket['berat']} kg > 30 kg -> PENGIRIMAN DIBATALKAN / DITOLAK.")
        return

    print(f"[+] Berat {paket['berat']} kg memenuhi syarat (<= 30 kg). Melanjutkan validasi tujuan...")

    kota_antar = cari_di_tuple(paket["tujuan"], TUJUAN_ANTAR_PULAU)
    kota_luar = cari_di_tuple(paket["tujuan"], TUJUAN_LUAR_PULAU)

    if kota_antar:
        paket["kategori"] = "Antar Pulau"
        paket["tujuan"] = kota_antar  
        paket["tarif_per_kg"] = TARIF_ANTAR_PULAU
        paket["total_biaya"] = int(paket["berat"] * TARIF_ANTAR_PULAU)
        paket["biaya_mc"] = paket["total_biaya"]
        if paket.get("status_pembayaran") == "Lunas":
            paket["status"] = "Diterima (Diproses)"
        else:
            paket["status"] = "Diterima (Menunggu Pembayaran)"
        print(f"[+] Tujuan '{kota_antar}' terdaftar (Kategori: Antar Pulau). Status: {paket['status']}.")
    elif kota_luar:
        paket["kategori"] = "Luar Pulau"
        paket["tujuan"] = kota_luar  
        paket["tarif_per_kg"] = TARIF_LUAR_PULAU
        paket["total_biaya"] = int(paket["berat"] * TARIF_LUAR_PULAU)
        paket["biaya_mc"] = paket["total_biaya"]
        if paket.get("status_pembayaran") == "Lunas":
            paket["status"] = "Diterima (Diproses)"
        else:
            paket["status"] = "Diterima (Menunggu Pembayaran)"
        print(f"[+] Tujuan '{kota_luar}' terdaftar (Kategori: Luar Pulau). Status: {paket['status']}.")
    else:
        paket["status"] = "Ditolak (Tujuan Tidak Terjangkau)"
        print(f"[-] Tujuan '{paket['tujuan']}' tidak ada dalam jangkauan rute. Status: DITOLAK.")


def ubah_status_admin(data_paket):
    print("\n--- UPDATE STATUS PENGIRIMAN ---")
    tampilkan_data(data_paket)
    
    try:
        cari_id = input("\nMasukkan ID Resi yang ingin diupdate statusnya: ").strip().upper()
    except KeyboardInterrupt:
        print("\n[!] Update status dibatalkan.")
        return

    paket = next((p for p in data_paket if p["id"] == cari_id), None)
    
    if not paket:
        print("ID Resi tidak ditemukan!")
        return

    if "Ditolak" in paket["status"]:
        print(f"[!] Paket ini telah berstatus '{paket['status']}' dan tidak dapat diproses lebih lanjut.")
        return

    print(f"\nID Resi       : {paket['id']}")
    print(f"Nama Pemesan  : {paket['nama']}")
    print(f"Status Saat Ini: {paket['status']}")
    print(f"Status Bayar  : {paket.get('status_pembayaran', '-')}")
    print("\nPilih status baru:")
    print("1. Sedang Dikirim")
    print("2. Sampai Tujuan")
    print("3. Batalkan Pengiriman")

    try:
        pilih = input("Pilih (1/2/3): ").strip()
    except KeyboardInterrupt:
        print("\n[!] Update status dibatalkan.")
        return
    
    if pilih == "1":
        paket["status"] = "Sedang Dikirim"
    elif pilih == "2":
        paket["status"] = "Sampai Tujuan"
    elif pilih == "3":
        paket["status"] = "Dibatalkan Admin"
    else:
        print("Pilihan tidak valid, pembaharuan dibatalkan!")
        return
            
    simpan_file(file_pengiriman, data_paket)
    print(f"[+] Status resi {paket['id']} berhasil diupdate menjadi: {paket['status']}")


def hapus_data(data_paket):
    print("\n--- HAPUS DATA PENGIRIMAN ---")
    tampilkan_data(data_paket)
    
    if len(data_paket) == 0:
        return
        
    try:
        cari_id = input("\nMasukkan ID Resi yang mau dihapus: ").strip().upper()
    except KeyboardInterrupt:
        print("\n[!] Penghapusan data dibatalkan.")
        return
    
    for i in range(len(data_paket)):
        if data_paket[i]["id"] == cari_id:
            try:
                konfirmasi = input(f"Apakah yakin menghapus resi {cari_id}? (y/n): ")
            except KeyboardInterrupt:
                print("\n[!] Penghapusan data dibatalkan.")
                return

            if konfirmasi.lower() == "y":
                data_paket.pop(i)
                simpan_file(file_pengiriman, data_paket)
                print("Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
            return
        
    print("ID Resi tidak ditemukan!")


def menu_admin(user_login, data_user):
    while True:
        data_paket = baca_file(file_pengiriman, [])
        print("\n========================================")
        print("           DASHBOARD ADMIN")
        print(f"Login sebagai: {user_login['username']} (ADMIN)")
        print("========================================")
        print("1. Lihat Semua Data Pengiriman")
        print("2. Input Pengiriman Langsung (Pelanggan Offline / Walk-in)")
        print("3. Validasi Pengajuan Pengiriman Baru (Validasi Berat & Tujuan)")
        print("4. Update Status Perjalanan (Sedang Dikirim / Selesai)")
        print("5. Hapus Data Pengiriman")
        print("6. Logout")
        print("========================================")
        
        try:
            pilihan = input("Pilih menu (1-6): ").strip()
        except KeyboardInterrupt:
            print("\n[!] Logout otomatis dari Admin.")
            break
        
        if pilihan == "1":
            tampilkan_data(data_paket)
            try:
                input("\nTekan Enter untuk kembali...")
            except KeyboardInterrupt:
                print()
        elif pilihan == "2":
            ajukan_pengiriman_admin(data_paket, user_login)
        elif pilihan == "3":
            validasi_pengiriman_admin(data_paket, data_user)
        elif pilihan == "4":
            ubah_status_admin(data_paket)
        elif pilihan == "5":
            hapus_data(data_paket)
        elif pilihan == "6":
            print("Berhasil logout dari Admin.")
            break
        else:
            print("Pilihan menu tidak valid!")


def menu_user(user_login, data_user):
    while True:
        data_paket = baca_file(file_pengiriman, [])
        saldo_sekarang = user_login.get("saldo", 0)
        
        print("\n========================================")
        print("           DASHBOARD PELANGGAN")
        print(f"Login sebagai : {user_login['username']} (USER)")
        print(f"Saldo MC Anda : {saldo_sekarang} MC ({format_rupiah(saldo_sekarang * KURS_MC_RUPIAH)})")
        print("========================================")
        print("1. Cek Status Pengiriman Saya")
        print("2. Ajukan Pengiriman Barang Baru")
        print("3. Bayar Tagihan Pengiriman (Sesuai Struk)")
        print("4. Cetak Struk Bukti Pengiriman")
        print("5. Top Up Saldo MC (1 MC = Rp 1.000)")
        print("6. Logout")
        print("========================================")
        
        try:
            pilihan = input("Pilih menu (1-6): ").strip()
        except KeyboardInterrupt:
            print("\n[!] Logout otomatis dari User.")
            break
        
        if pilihan == "1":
            tampilkan_data(data_paket, filter_username=user_login["username"])
            try:
                input("\nTekan Enter untuk kembali...")
            except KeyboardInterrupt:
                print()
        elif pilihan == "2":
            ajukan_pengiriman_user(data_paket, user_login, data_user)
        elif pilihan == "3":
            bayar_tagihan_user(data_paket, user_login, data_user)
        elif pilihan == "4":
            tampilkan_data(data_paket, filter_username=user_login["username"])
            try:
                cari_id = input("\nMasukkan ID Resi yang ingin dicetak struknya: ").strip().upper()
            except KeyboardInterrupt:
                print("\n[!] Batal mencetak struk.")
                continue

            paket = next((p for p in data_paket if p["id"] == cari_id and p.get("username") == user_login["username"]), None)
            if paket:
                cetak_struk(paket)
            else:
                print("ID Resi tidak ditemukan atau bukan milik akun Anda!")
            try:
                input("\nTekan Enter untuk kembali...")
            except KeyboardInterrupt:
                print()
        elif pilihan == "5":
            top_up_saldo(user_login, data_user)
        elif pilihan == "6":
            print("Berhasil logout dari User.")
            break
        else:
            print("Pilihan menu tidak valid!")


def main():
    data_awal_user = [
        {"username": "admin", "password": "123", "role": "admin", "saldo": 0}
    ]
    data_user = baca_file(file_user, data_awal_user)
    
    for u in data_user:
        if "saldo" not in u:
            u["saldo"] = 0
    simpan_file(file_user, data_user)

    while True:
        print("\n==================================")
        print("  SISTEM PENGIRIMAN KARGO LOGISTIK")
        print("==================================")
        print("1. Login")
        print("2. Registrasi (User Baru)")
        print("3. Keluar")
        print("==================================")
        
        try:
            pilihan = input("Pilih menu (1-3): ").strip()
        except KeyboardInterrupt:
            print("\n\nTerima kasih sudah menggunakan program ini.")
            break
        
        if pilihan == "1":
            user_login = login(data_user)
            if user_login:
                if user_login["role"] == "admin":
                    menu_admin(user_login, data_user)
                else:
                    menu_user(user_login, data_user)
        elif pilihan == "2":
            registrasi(data_user)
        elif pilihan == "3":
            print("Terima kasih sudah menggunakan program ini.")
            break
        else:
            print("Pilihan salah, masukkan angka 1 sampai 3!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")