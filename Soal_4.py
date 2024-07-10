class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def set_nama(self, nama):
        self.nama = nama

    def set_warna(self, warna):
        self.warna = warna

    def set_rasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f'Buah: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}'

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def set_vitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        return f'Buah: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}, Vitamin: {self.vitamin}'

mangga = Mangga("Mangga Arumanis", "Kuning", "Manis", "Vitamin C")
print(mangga.information())

mangga.set_nama("Mangga Gadung")
mangga.set_warna("Hijau")
mangga.set_rasa("Asam Manis")
mangga.set_vitamin("Vitamin A")
print(mangga.information())
