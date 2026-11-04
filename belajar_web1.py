class segitiga:
    def __init__ (self):
        self.konstant =  0.5
        self.tinggi = float(input("Masukan Tinggi Segitiga: " ))
        self.alas = float(input("Masukan Alas Segitiga: "))
    def luas (self):
        return self.konstant*self.tinggi*self.alas

if __name__ == "__main__":
    LuasS = segitiga()
    print("Luas Segitiga Adalah: ", LuasS.luas())
