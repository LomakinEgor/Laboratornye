class RecordBook (object):


    def __init__(self, name, surname, patron, rating, cours):
        self.name = name
        self.surname = surname
        self.patron = patron
        self.rating = rating
        self.cours = cours

    def avgrate(self):
        avg = 0
        for key in self.rating.keys():
            avg = avg + self.rating[key]
        avg = avg / len(self.rating)
        return "Средний балл: %s" % (avg)

    def show(self):
        str = "Студент: %s %s %s\nКурс: %s\nПредметы" % (self.name, self.surname, self.patron, self.cours)
        for key in self.rating.keys():
            str += "\n%s: %s" % (key, self.rating[key])
        return str


if __name__ == "__main__":
    stud = RecordBook("As", "Sd", "Jp", {'Матан': 5, 'Матан2': 3, 'Матан3': 4}, 5)
    print(stud.avgrate())
    print(stud.show())