import datetime
from functools import reduce
import random
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
    
    def show_rec(self):
        res = ''
        for x in self.record_book:
            res += "\n   " + x + ': ' + str(self.record_book[x])
        return res

    def show(self):
        return "Студент: %s %s %s \nДата рождения: %s\nЗачетная книжка: %s" % (self.name, self.surnamne, self.patron, self.both_date, self.show_rec())

    def __repr__(self):
        return '%s(%r, %r, %r, %r,%r)' % (self.__class__.__qualname__, self.name, self.surnamne, self.patron, self.both_date, self.record_book)

    def avg(self):
        return reduce(lambda x, z: (x+z)/2, self.record_book.values())

    def create(self):
        namem = ['Игорь', 'Петя', 'Иван', 'Кирилл', 'Сергей', 'Антон', 'Филипп', 'Олег']
        surnamem = ['Иванов', 'Кузнецов', 'Сидоров', 'Пупкин', 'Цветков', 'Романов', 'Рыбаков', 'Перин']
        patr = ['Игоревич', 'Петрович', 'Иванович', 'Кириллович', 'Сергеевич', 'Антонович', 'Филиппович', 'Олегович']
        subj = [{ 'История' : 5 , 'Иинформатика' : 3 , 'Философия' : 3 }, {'История' : 5 , 'Иинформатика' : 4 , 'Философия' : 3, 'Базы данных' : 4},
                { 'История' : 5 , 'Иинформатика' : 3 , 'Философия' : 5 }, { 'История' : 5 , 'Иинформатика' : 4 , 'Философия' : 4 }
                ]
        self.name = namem[random.randint(0,7)]
        self.surnamne = surnamem[random.randint(0,7)]
        self.patron = patr[random.randint(0,7)]
        self.both_date = datetime.date(random.randint(1990,2000),random.randint(1,12), random.randint(1,27))
        self.record_book = subj[random.randint(0,3)]

if __name__ == "__main__":
    #x = People('qwe','sdf','bvxc',datetime.date(2000,12,12))
    #print(x.__repr__())
    y = Student('Петров','Андрей','Олегович',datetime.date(2001,4,23), { 'История' : 5 , 'Иинформатика' : 3 , 'Философия' : 3 })
    group = [Student('Петров','Андрей','Олегович',datetime.date(2001,4,23), { 'История' : 5 , 'Иинформатика' : 3 , 'Философия' : 3 }),
            Student('Власов','Петр','Владимирович',datetime.date(2001,4,23), { 'История' : 5 , 'Иинформатика' : 4 , 'Философия' : 3, 'Базы данных' : 4 }),
            Student('Сидоров','Игорь','Михайлович',datetime.date(2001,4,23), { 'История' : 5 , 'Иинформатика' : 3 , 'Философия' : 5 }),
            Student('Грушин','Константин','Кириллович',datetime.date(2001,4,23), { 'История' : 5 , 'Иинформатика' : 4 , 'Философия' : 4 })
            ]
    #print(y.__repr__())
    print(y.show())
    print('Среднее занчение оценок в зачетной книжке:')
    for i in group:
        print(i.surnamne +" "+ i.name +" "+ i.patron +" "+ str(reduce(lambda x, z: (x+z)/2, i.record_book.values())))
    print('\n\nВывод через функцию высшего порядка')
    print('\n'.join(map(Student.show,group)))
    print(y.avg())
    #st = Student(None, None, None, None, None)
    #st.create()
    #print(st.show())