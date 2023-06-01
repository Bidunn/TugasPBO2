class Universitas:
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas   
        # Inisialisasi atribut 'nama_universitas' dengan nilai yang diberikan saat objek dibuat
        self.daftar_jurusan = []  
        # Inisialisasi atribut 'daftar_jurusan' sebagai list kosong

    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)   
        # Menambahkan objek 'jurusan' ke dalam list 'daftar_jurusan'

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di", self.nama_universitas)   
        # Menampilkan nama universitas
        if self.daftar_jurusan:   # Cek apakah list 'daftar_jurusan' tidak kosong
            for jurusan in self.daftar_jurusan:  
                # Iterasi melalui setiap objek jurusan dalam list
                print("- ", jurusan.nama_jurusan)   
                # Menampilkan nama setiap jurusan
        else:
            print("Belum ada jurusan terdaftar.")   
            # Menampilkan pesan jika list 'daftar_jurusan' kosong
class Jurusan:
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan   
        # Inisialisasi atribut 'nama_jurusan' dengan nilai yang diberikan saat objek dibuat
        self.daftar_mahasiswa = []         
        # Inisialisasi atribut 'daftar_mahasiswa' sebagai list kosong

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)   
        # Menambahkan objek 'mahasiswa' ke dalam list 'daftar_mahasiswa'

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.nama_jurusan)   
        # Menampilkan nama jurusan
        if self.daftar_mahasiswa:    
            # Cek apakah list 'daftar_mahasiswa' tidak kosong
            for mahasiswa in self.daftar_mahasiswa:  
                # Iterasi melalui setiap objek mahasiswa dalam list
                print("- Nama:", mahasiswa.nama, "| NIM:", mahasiswa.nim)   
                # Menampilkan nama dan nim setiap mahasiswa
        else:
            print("Belum ada mahasiswa terdaftar.")   
            # Menampilkan pesan jika list 'daftar_mahasiswa' kosong
            
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama   
        # Inisialisasi atribut 'nama' dengan nilai yang diberikan saat objek dibuat
        self.nim = nim     
        # Inisialisasi atribut 'nim' dengan nilai yang diberikan saat objek dibuat
        self.jurusan = jurusan   
        # Inisialisasi atribut 'jurusan' dengan nilai yang diberikan saat objek dibuat

    def tampilkan_info(self):
        print("Nama:", self.nama)    
        # Menampilkan nilai atribut 'nama' dari objek
        print("NIM:", self.nim)      
        # Menampilkan nilai atribut 'nim' dari objek
        print("Jurusan:", self.jurusan.nama_jurusan)  
        # Menampilkan nilai atribut 'nama_jurusan' dari objek 'jurusan'

universitas_xyz = Universitas("University of XYZ")   
# Membuat objek 'universitas_xyz' dengan nama "University of XYZ"

jurusan_ti = Jurusan("Teknik Informatika")   
# Membuat objek 'jurusan_ti' dengan nama "Teknik Informatika"

universitas_xyz.tambah_jurusan(jurusan_ti)  
# Menambahkan objek 'jurusan_ti' ke dalam list 'daftar_jurusan' pada objek 'universitas_xyz'

mahasiswa = Mahasiswa("Muhammad Hanif Al Abid", "G10A017042", jurusan_ti)   
# Membuat objek 'mahasiswa' dengan nama "Muhammad Hanif Al Abid", NIM "G10A017042", dan objek 'jurusan_ti' sebagai jurusan

jurusan_ti.tambah_mahasiswa(mahasiswa)   
# Menambahkan objek 'mahasiswa' ke dalam list 'daftar_mahasiswa' pada objek 'jurusan_ti'

universitas_xyz.tampilkan_daftar_jurusan()  
# Memanggil metode 'tampilkan_daftar_jurusan()' pada objek 'universitas_xyz' untuk menampilkan daftar jurusan

jurusan_ti.tampilkan_daftar_mahasiswa()   
# Memanggil metode 'tampilkan_daftar_mahasiswa()' pada objek 'jurusan_ti' untuk menampilkan daftar mahasiswa dalam jurusan tersebut
