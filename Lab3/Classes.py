import datetime

class People (object):
    
    def __init__(self, name, surname, patron, both_date):
        self.name = name
        self.surnamne = surname
        self.patron = patron
        self.both_date = both_date

    def show(self):
        pass

    def __repr__(self):
        return '%s(%r, %r, %r, %r)' % (self.__class__.__qualname__, self.name, self.surnamne, self.patron, self.both_date)


class Student(People):
    def __init__(self, name, surname, patron, both_date, record_book):
        super().__init__(name, surname, patron, both_date)
        self.record_book = record_book
    
    def show(self):
        return "Студент: %s %s %s \nДата рождения: %s\nНомер зачетной книжки: %s" % (self.name, self.surnamne, self.patron, self.both_date, self.record_book)

    def __repr__(self):
        return '%s(%r, %r, %r, %r,%r)' % (self.__class__.__qualname__, self.name, self.surnamne, self.patron, self.both_date, self.record_book)


class Teacher(People):
    def __init__(self, name, surname, patron, both_date, discipline):
        super().__init__(name, surname, patron, both_date)
        self.discipline= discipline

    def show(self):
        return "Преподаватель: %s %s %s \nДата рождения: %s\nДисциплина: %s" % (self.name, self.surnamne, self.patron, self.both_date, self.discipline)

    def __repr__(self):
        return '%s(%r, %r, %r, %r,%r)' % (self.__class__.__qualname__, self.name, self.surnamne, self.patron, self.both_date, self.discipline)


if __name__ == "__main__":
    x = People('qwe','sdf','bvxc',datetime.date(2000,12,12))
    print(x.__repr__())
    y = Student('aa','vv','bb',datetime.date(2001,4,23), "14235")
    print(y.__repr__())
    z = Teacher('Bbb','Aaa','Ccc', datetime.date(1969,6,15), "Иностранный язык")
    print(z.__repr__())
    print(y.show())
    print(z.show())
