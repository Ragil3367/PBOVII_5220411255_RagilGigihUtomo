class perpusitem:
    def __init__(self,judul,subjek):
        self.judul=judul
        self.subjek=subjek
    def LokasiPenyimpanan(_):
        print("disimpan pada.....")
    def info(self):
        print(f'judul :{self.judul},\n subjek :{self.subjek}')

class Buku(perpusitem):
    def __init__(self,judul,subjek,isbn,pengarang,jmlHal,ukuran):
        super().__init__(judul,subjek)
        self.isbn=isbn
        self.pengarang=pengarang
        self.jmlHal=jmlHal
        self.ukuran=ukuran
    def info(self):
        super().info()
        print('ISBN :',self.isbn)
        print('pengarang :',self.pengarang)
        print('jumlah halaman :',self.jmlHal)
        print('ukuran :',self.ukuran)

class majalah(perpusitem):
    def __init__(self,judul,subjek,volume,issue):
        super().__init__(judul,subjek)
        self.volume=volume
        self.issue=issue
    def info(self):
        super().info()
        print('volume :',self.volume)
        print('issue :',self.issue )


class DVD(perpusitem):
    def __init__(self,judul,subjek,aktor,genre):
        super().__init__(judul,subjek)
        self.aktor=aktor
        self.genre=genre
    def info(self):
        super().info()
        print('aktor :',self.aktor)
        print('genre :',self.genre)

class katalog():
    def cari():
        print('mencari katalog...')

class pengarang(Buku):
    def __init__(self,nama):
        self.nama=nama
    def info(self):
        print('nama pengarang ',self.nama)
    def cari():
        print('mencari pengarang.....')


buku1=Buku('Harry Potter','buku','55291','J.K. Rowling','100','40x40')
majalah1=majalah('komputer','majalah','5','A')
dvd1=DVD('Spider-Man','film','peter','action')

buku1.LokasiPenyimpanan()
majalah1.LokasiPenyimpanan()
dvd1.LokasiPenyimpanan()

buku1.info()
majalah1.info()
dvd1.info()