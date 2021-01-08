
import numpy as np
import datetime

year=[]
month=[]
day=[]
for i in range(4):
    x=datetime.datetime(np.random.randint(1940,2020), np.random.randint(1,12), np.random.randint(1,30))
    year.append(x.year)
    month.append(x.month)
    day.append(x.day)

peopellist={'Shangol':[year[0],month[0],day[0]],
            'Mangol':[year[1],month[1],day[1]],
            'HabeAngoor':[year[2],month[2],day[2]],
            'AghaGorgeh':[year[3],month[3],day[3]]}
E=1
while E != 'exit':
    class Birthday:
        def __init__(self, info:dict  ):
            self.info=info
    
        def showInfo(self):
            for key in self.info.keys():
                print(key ,'\nBirthdate:', self.info[key])
                print('\n----------------------------------\n ')
        def printnew(self):
            cont='y'
            while cont=='y':
                name=input('Enter name: ')
                year=int(input('Enter birth year: '))
                if year<=1800 or year>=2021:
                    print('Invalid year number')
                    break
                
                month=int(input('Enter birth number of month : '))
                if month<=1 or month>=12:
                    print('Invalid month number')
                    break
                
                day=int(input('Enter number of birth day: '))
                if day<=1 or day>=30:
                    print('Invalid day numder')
                    break
                    
                self.info.update({name:[year,month,day]})#{'a':1}
                print('\n      **new person**')
                print( name,'\nBirthdate:', self.info[name])
                print('\n----------------------------------\n ')
                cont=input('Do you want to contineu adding peopel (y/n): ')
    
        def findbirth(self):
            cont='y'
            while cont=='y':
                year=int(input('Enter birth year: '))
                if year<=1800 or year>=2021:
                    print('Invalid year number')
                    break
                
                month=int(input('Enter birth number of month : '))
                if month<=1 or month>=12:
                    print('Invalid month number')
                    break
                
                day=int(input('Enter number of birth day: '))
                if day<=1 or day>=30:
                    print('Invalid day numder')
                    break
            
                for key, value in self.info.items():
                    if value == [year,month,day]:
                        keeper=1
                
                if keeper==1:
                    print('his name is', key)
                else:
                    print('There is no person with this birth date in list')
                print('\n----------------------------------\n ')
                cont=input('Do you want to continue adding peopel (y/n): ')
    
        def findpers(self):
            cont='y'
            keep=0
            while cont=='y':
                name=input('Enter name: ')   
                for key in self.info.keys():
                    if key==name:
                        keep=1

                if keep==1:
                     print('he is born in',self.info[key])    
                else:
                    print('There is no such a person in list')

                
                print('\n----------------------------------\n ')
                cont=input('Do you want to contineu adding peopel (y/n): ')
   
    x=Birthday(peopellist)
    print('to see information type (1)')
    print('to add new person type (2)')
    print('to find somone with birthdate type (3)')
    print('to find somone with name type (4)')
    inp=int(input('type here:'))
    if inp==1 :
        x.showInfo()
    if inp==2 :
        x.printnew()
    if inp==3 :
        x.findbirth()
    if inp==4 :
        x.findpers()
    E=input('Do you want to stay in Birthdate class? (if no type exit):')





