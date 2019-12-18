from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, nurse, helps_the_doctor')

+(nurse ['Mary']=='Dr. Alex')
+(nurse ['John']=='Dr. Mary')
+(nurse ['Mary']=='Dr. Alex')
+(nurse ['Mary']=='Dr. Alex')
+(nurse ['Mary']=='Dr. Alex')

(helps_the_doctor[X]==len_(Y))<=(nurse[Y]==X)
print(helps_the doctor['Nancy']==Z)
