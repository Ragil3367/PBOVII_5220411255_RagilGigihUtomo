class Art:
    def __init__(self,artist,nama,jenis_art,year):
        self._artist = artist
        self.__nama = nama
        self.jenis_art = jenis_art
        self.__year = year
    def get_year(self):
        return self.__year
    def info(self):
        return(f"pencipta : {self._artist}\nnama art : {self.__nama}\njenis art : {self.jenis_art}\ntahun : {self.__year}")

class Lukisan(Art):
    def __init__(self,_artist, nama, jenis_art,year,jenis_lukisan):
        super().__init__(_artist, nama, jenis_art,year)
        self.jenis_lukisan = jenis_lukisan
    def info(self):
        return(f"{super().info()}\njenis lukisan : {self.jenis_lukisan}")
    def usiaLukisan(self):
        print(f"usia lukisan adalah : {2024-self.get_year()} tahun")
    

class Sculpture(Art):
    def __init__(self,_artist, nama, jenis_art,year,material):
        super().__init__(_artist, nama, jenis_art,year)
        self.material = material
    def info(self):
        print(f"{super().info()}\nmaterial : {self.material}")
    def _usiaSculpture(self):
        print(f"usia sculpture adalah : {2024-self.get_year()} tahun")

class landscape(Lukisan):
    def __init__(self,_artist, nama, jenis_art, year, jenis_lukisan,value):
        super().__init__(_artist, nama, jenis_art, year, jenis_lukisan)
        self.value = value
    def info(self):
        print(f"{super().info()}\nvalue : ${self.value}")
    def rupiah(self):
        value = str(self.value)
        if len(value) == 8:
            print(f"harga dalam rupiah : {int(value[0:2])*15} miliar")
        elif len(value) == 7:
            print(f"harga dalam rupiah : {int(value[0:1])*15} miliar")


lukisan1 = landscape('John Constable','The Hay Wain','lukisan',1821,'landscape',9000000)
lukisan2 = landscape('Vincent van Gogh','the Starry Night','lukisan',1889,'landscape',50000000)
sculpture1 = Sculpture('Auguste Rodin','the Thinker','sculpture',1881,'clay')

art_data = []
art_data.append(lukisan1)
art_data.append(lukisan2)
art_data.append(sculpture1)
def total_value(data):
    value = 0
    for i in data:
        if i.jenis_art == 'lukisan' and i.value is not None:
            value += i.value
        elif i.jenis_art == 'sculpture':
            continue
    print(f"total value lukisan adalah : ${value}")

sculpture1.info()
sculpture1._usiaSculpture()
lukisan1.info()
lukisan1.usiaLukisan()
lukisan1.rupiah()
lukisan2.info()
lukisan2.usiaLukisan()
lukisan2.rupiah()
total_value(art_data)