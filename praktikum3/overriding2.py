class Idol_Kpop:
    def __init__(self,nama_grup,jenis,jumlah_anggota,nama_fandom):
        self.nama_grup = nama_grup
        self.jenis = jenis
        self.jumlah_anggota = jumlah_anggota
        self.nama_fandom = nama_fandom

    def display(self):
        print('\n\tIdol Kpop\t\n', '=' *30)
        print('Nama Grup\t: ',self.nama_grup)
        print('Jenis\t\t: ',self.jenis)
        print('Jumlah Anggota\t: ',self.jumlah_anggota,)
        print('Nama Fandom\t: ',self.nama_fandom,)



class boygroup(Idol_Kpop):
    def __init__(self,nama_grup,jenis,jumlah_anggota,nama_fandom):
        super().__init__(nama_grup,jenis,jumlah_anggota,nama_fandom)
        

class girlgroup(Idol_Kpop):
    def __init__(self,nama_grup,jenis,jumlah_anggota,nama_fandom):
        super().__init__(nama_grup,jenis,jumlah_anggota,nama_fandom)
        


idolkpop1 = boygroup('BTS','Boygroup','7', 'Army')
idolkpop1.display()

idolkpop2 = girlgroup('Blackpink','Girlgroup','4', 'Blink')
idolkpop2.display()

idolkpop3 = boygroup('Enhypen','Boygroup','7', 'Engene')
idolkpop3.display()

idolkpop4 = boygroup('TXT','Boygroup','5', 'Moa')
idolkpop4.display()

idolkpop5 = girlgroup('NewJeans','Girlgroup','5', 'Bunnies')
idolkpop5.display()