fiona_tarquinio = {'name':'Fiona Teresa Tarquinio', 'age':43, 'nationality': 'Australian/Italian', 'place of birth':'Bendigo', 'place of residence':'Sunshine', 'favourite colour':'green', 'favourite number': 18, 'occupation':'Engineer', 'hobby':'tap dancing'}
fiona_child = {'nationality':'Australian', 'place of residence':'Bendigo', 'hobby':'netball'}
fiona_student = {'place of residence':'Parkville', 'occupation':'student', 'hobby':'volleyball'}

year = input("Enter year: ")
fiona_tarquinio['age'] = int(year)-1980

if int(year) < 1980:
    fiona_tarquinio.clear()
    print('I was not born yet')
elif int(year) < 1999:
    fiona_tarquinio.update(fiona_child)
    del fiona_tarquinio['occupation']
    if int(year) < 1986:
        del fiona_tarquinio['hobby']
        del fiona_tarquinio['favourite colour']
        del fiona_tarquinio['favourite number']
elif int(year) < 2005:
    fiona_tarquinio.update(fiona_student)
elif int(year) < 2009:
    fiona_tarquinio['place of residence'] = 'North Melbourne'
    fiona_tarquinio['hobby'] = 'swimming'
  
for key, value in fiona_tarquinio.items():
    print(f'My {key} is {value}')


