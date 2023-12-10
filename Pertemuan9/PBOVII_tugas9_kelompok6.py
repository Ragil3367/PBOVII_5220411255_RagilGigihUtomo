class Animal:
    def __init__(self,nama,sifat,ukuran,jumlah_kaki):
        self.nama=nama
        self._sifat=sifat
        self.ukuran=ukuran
        self.jumlah_kaki=jumlah_kaki
    def getInfo(self):
        return(f"nama = {self.nama}\nsifat = {self._sifat}\nukuran = {self.ukuran}\njumlah kaki = {self.jumlah_kaki}")

class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki,bisa_jalan,jenis_mamalia):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_jalan=bisa_jalan
        self.jenis_mamalia=jenis_mamalia
    def getInfo(self):
        print(f"{super().getInfo()}\nbisa jalan = {self.bisa_jalan}\njenis = {self.jenis_mamalia}")

class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki,bisa_terbang,jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_terbang=bisa_terbang
        self.jenis_aves=jenis_aves
    def getInfo(self):
        print(f"{super().getInfo()}\nbisa terbang = {self.bisa_terbang}\njenis = {self.jenis_aves}")

class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves,bisa_diadu,jenis_ayam):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.bisa_diadu=bisa_diadu
        self.jenis_ayam=jenis_ayam
    def getInfo(self):
        print(f"{super().getInfo()}bisa terbang = {self.bisa_terbang}\njenis = {self.jenis_aves}")
        print(f"bisa diadu = {self.bisa_diadu}\njenis ayam = {self.jenis_ayam}")

class Merpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
    def getInfo(self):
        print(f"{super().getInfo()}bisa terbang = {self.bisa_terbang}\njenis = {self.jenis_aves}")


mamalia1=Mamalia('sapi','herbivora','3meter','4','bisa','mamalia')
aves1=Aves('elang','karnivora','70cm','2','bisa','aves')
ayam1=Ayam('ayam','omnivora','50cm','2','bisa','aves','tidak','ayam hias')
merpati1=Merpati('merpati','omnivora','40cm','2','bisa','aves')

mamalia1.getInfo()
aves1.getInfo()
ayam1.getInfo()
merpati1.getInfo()
