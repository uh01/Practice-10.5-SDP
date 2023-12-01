from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    # d = {'name' : 'Fahman', 'age' : 30}

    # d = {'courses' : [
    #     {
    #         'id' : 1,
    #         'name' : 'Django',
    #         'fee' : 5000
    #     },
    #     {
    #         'id' : 2,
    #         'name' : 'Python',
    #         'fee' : 3000
    #     },
    #     {
    #         'id' : 3,
    #         'name' : 'C++',
    #         'fee' : 2000
    #     },
    #     ]}

    d = {
        'lst' : ['It', 'is', 'a', 'list', 'of', 'string'], 
        'birthday' : datetime.datetime.now(), 
        'val1' : 10, 
        'val2' : 'earthly',
        'val3' : 'January - February - March',
        'val4' : [{'name': 'Josh', 'age': 19},{'name': 'Dave', 'age': 22},{'name': 'Joe', 'age': 31},],
        'val5' :  ['Apple', 'Mango', 'Orange'],
        'val6' :  ['Apple', 'Mango', 'Orange'],
        'val7' :  ['Banana', 'Apple', 'Mango', 'Orange'],
        'val8' :  'Humpty Dumpty sat on the Wall',
        'val9' :  'humpty dumpty sat on the wall',
        'val10' :  'Django rest framework',
        'val11' :  ['Father', 'Mother', 'Child'],
        'val12' :  ['Father', 'Mother', 'Child'],
        'val13' :  datetime.datetime.now(),
        'val14' :  'Happy coding'
        } 

    return render(request, 'home.html', d)
    
   
