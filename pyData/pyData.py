from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, H, doctor, spec, simpt, patient, depart, dep_simpt, pat_doc, pat_dep')

+(doctor['Dr. Alex'] == 'Lor')
+(doctor['Dr. Mary'] == 'Oculist')
+(doctor['Dr. Mitch'] == 'Therapist')
+(doctor['Dr. Marty'] == 'Orthopedist')
+(doctor['Dr. Kenny'] == 'Cardiologist')
+(spec['Nose'] == 'Lor')
+(spec['Ears'] == 'Lor')
+(spec['Throat'] =='Lor')
+(spec['Eye'] == 'Oculist')
+(spec['Stomach'] == 'Therapist')
+(spec['Liver'] == 'Therapist')
+(spec['Foot'] == 'Orthopedist')
+(spec['Back'] == 'Orthopedist')
+(spec['Heart'] == 'Cardiologist')
+(depart['Dr. Alex'] == '1')
+(depart['Dr. Mary'] == '1')
+(depart['Dr. Mitch'] == '2')
+(depart['Dr. Marty'] =='2')
+(depart['Dr. Kenny'] == '3')
(simpt[X] == Y) <= (spec[X] == Z) & (doctor[Y] == Z)
#print(simpt[X] == Y)
(dep_simpt[X] == Y) <= (simpt[X] == Z) & (depart[Z] == Y)
#print(dep_simpt[X] == Y)
+(patient['Dalas'] == 'Nose')
+(patient['Erik'] == 'Foot')
+(patient['Bill'] == 'Back')
+(patient['Ana'] == 'Heart')
+(patient['Sony'] == 'Eye')
+(patient['Saly'] == 'Ears')
(pat_doc[X] == Y) <= (patient[X] == Z) & (simpt[Z] == Y)
print('Вывод врача для пациента:\n')
print(pat_doc[X] == Y)
(pat_dep[X] == Y) <= (patient[X] == Z) & (dep_simpt[Z] == Y)
print('\nВывод номера отделения для пациента:\n')
print(pat_dep[X] == Y)
