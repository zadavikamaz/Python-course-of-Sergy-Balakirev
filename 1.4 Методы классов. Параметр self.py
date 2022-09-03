class Translator:
    d = dict()

    def add(self, eng, rus):
        self.d.setdefault(eng, []).append(rus)

    def remove(self, eng):
        del self.d[eng]

    def translate(self, eng):
        return self.d[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))
