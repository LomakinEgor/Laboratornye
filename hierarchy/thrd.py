from people import *
import threading
import time
from multiprocessing import Process

mylist = []
mylist2 = []
mylist3 = []
def crt (name):
    st = Student(None,None,None,None,None)
    st.create()
    mylist.append(st)
    #print('Поток {} добавил элемент'.format(name))

def crt2 (name):
    st = Student(None,None,None,None,None)
    st.create()
    mylist3.append(st)
    
def av(par, name):
    avg = par.avg()
    yield avg

#t = Thread(target=crt, name='thred 1', args=('2'))
#t.start()
#if __name__ == '__main__':
thread_list = []
strt = time.time()
for i in range(1000):
    t = threading.Thread(target=crt, name='thred {}'.format(i), args=('2'))
    #print('{} started'.format(t.name))
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

end = time.time()
print('All time {}'.format(end-strt))
print('Количество элементов {}'.format(mylist.__len__()))
strt2 = time.time()
for i in range(10000):
    st = Student(None,None,None,None,None)
    mylist2.append(st.create())
end2 = time.time()
print('All time2 {}'.format(end2-strt2))

stime = time.time()
proces = []
#for i in range(10):
 #   proc = Process(target=crt2, args=('2'))
 #   proces.append(proc)
 #   proc.start()
 #   print('{}'.format(i))


etime = time.time()
#print('All time3 {}'.format(etime-stime))

thread_list2 = []
strt = time.time()
for i in mylist:
    t = threading.Thread(target=av, name='thred {}'.format(i), args=(i,'tread'))
    #print('{} started'.format(t.name))
    t.start()
    thread_list2.append(t)

for t in thread_list2:
    t.join()

end = time.time()
print('AVG time thread {}'.format(end-strt))

strt2=time.time()
for i in mylist:
    av(i,'cycle')
end2 = time.time()
print('AVG time cycle {}'.format(end2-strt2))