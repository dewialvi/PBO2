class netflix:
    def __init__(self,judul,jenis,genre):
        self.judul = judul
        self.jenis = jenis
        self.genre = genre

    def display(self):
        print('\n\tNetflix\t\n', '=' *30)
        print('judul\t: ',self.judul)
        print('jenis\t: ',self.jenis)
        print('genre\t: ',self.genre)



class film(netflix):
    def __init__(self,judul,jenis,genre):
        super().__init__(judul,jenis,genre)
        

class series(netflix):
    def __init__(self,judul,jenis,genre):
        super().__init__(judul,jenis,genre)
        


netflix1 = film('Enola Holmes','Film','Misteri, petualangan')
netflix1.display()

netflix2 = series('Stranger Things','Series','Misteri, horror')
netflix2.display()