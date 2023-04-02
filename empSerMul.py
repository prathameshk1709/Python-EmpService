def createEmpMul():
    a = str(input('Do you want to enter emp details: y or n '))
    empdetails={}
    if a == 'y':
        num = int(input('Enter number of employees to be entered '))
        for i in range(0,num):
            id = int(input('Enter emp id '))
            name = str(input('Enter emp name '))
            salary = int(input('Enter emp salary '))
            age = int(input('Enter emp age '))
            dept = str(input('Enter emp dept '))
            empdetails[id]={'id':id, 'name':name, 'salary':salary, 'age':age, 'dept':dept}
            #print('Employee details for employee no ',id, '\nId',empdetails[id]['id'], '\nName',empdetails[id]['name'],'\nSalary',empdetails[id]['salary'], '\nAge',empdetails[id]['age'], '\nDept',empdetails[id]['dept'])
        displayEmp(empdetails)
        #displayEmpVal(empdetails)
        return empdetails
    else:
        print('Emp entry not to be done')

def changeEmpSal(empdetails):
    b= str(input('Do you wish to change emp salary: y or n '))
    if b == 'y':
        id = int(input('Enter which emp id, salary to be changed? '))
        newsal= int(input('Enter the new salary '))
        empdetails[id]['salary']=newsal
        #print('Updated salary is ',empdetails[id]['salary'])
        #displayEmp(empdetails)
        displayEmpVal(empdetails)
    else:
        print('Salary update is not required')

def delEmp(empdetails):
    c=int(input('Enter the emp id which you want to delete '))
    empdetails.pop(c)
    return empdetails

def displayEmp(empdetails):
    for y in empdetails:
        print('ID: ',y, empdetails[y])

def displayEmpVal(empdetails):
    for i in empdetails.values():
        print(i)
    
    