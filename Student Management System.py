import json
while True:
        student={}
        with open('Data file for student management system.json','r') as f:
                students=json.load(f)
        print('''\n"1 or add" to Add Student''')
        print('''"2 or edit" to Edit Student''')
        print('''"3 or delete" to Delete Student''')
        print('''"4 or search" to Search Student''')
        print('''"5 or display" to Display all Students''')
        while True:
                try:
                        option=str(input('''\nPlease enter any option given above:'''))
                        if option not in ['1','2','3','4','5','add','delete','edit','search','display']:
                                print('''\n"Please select a correct options"''')
                        else:
                                break
                except ValueError:
                        print('''"Please enter a correct number only"''')
        if option in ['1','add']:
                student["Name"] = input ("\nStudent's Name:").title()
                student["F.Name"] = input ("Father's Name:").title()
                while True:
                        try:
                                student["Age"]=int(input("Age:"))
                        except ValueError:
                                print('''\n"Please enter only number"''')
                        else:
                                break
                student["Address"] = input ("Address:").title()
                students.append(student)
                with open('Data file for student management system.json','w') as f:
                        json.dump(students,f)
                student={}
                print('''\n"Addition Successful"''')
        elif option in ['2','edit']:
                enum=0
                Name=input("\nPlease type name:").title()
                while True:
                        f=input("\nWhih field you wanna you wanna change?\n\nName,F.Name,Age,Address:").title()
                        if f not in ['Name','F.Name','Age','Address']:
                                print('''\n"Please enter correct field"''')
                        else:
                                break
                for s in list(students):
                        for k,v in s.items():
                                if s['Name']==Name:
                                        enum+=1
                                        if f=='Name':
                                                new_name=input("\nEnter the new name:").title()
                                                s['Name']=new_name
                                                print('''\n"Edit Successful"''')
                                                with open('Data file for student management system.json','w') as f:
                                                        json.dump(students,f)
                                        elif f=='F.Name':
                                                new_f_name=input("\nEnter the new F.Name:").title()
                                                s['F.Name']=new_f_name
                                                print('''\n"Edit Successful"''')
                                                with open('Data file for student management system.json','w') as f:
                                                        json.dump(students,f)
                                        elif f=='Age':
                                                while True:
                                                        try:
                                                                new_age=int(input("\nEnter new age:"))
                                                        except ValueError:
                                                                print('''\n"Please enter only number"''')
                                                        else:
                                                                break
                                                s['Age']=new_age
                                                print('''\n"Edit Successful"''')
                                                with open('Data file for student management system.json','w') as f:
                                                        json.dump(students,f)
                                        elif f=='Address':
                                                new_add=input("\nEnter new address:").title()
                                                s['Address']=new_add
                                                print('''\n"Edit Successful"''')
                                                with open('Data file for student management system.json','w') as f:
                                                        json.dump(students,f)
                if enum==0:
                        print('''\n"Student not found"''')
        elif option in ['3','delete']:
                inum=0
                del_name=input("\nPlease type name of student you want to delete:").title()
                for s in list(students):
                        for d in s:
                                if s['Name']==del_name:
                                        ind=students.index(s)
                                        inum+=1
                                        while True:
                                                sure=input('\nAre you sure you want to delete?\n\nYes or No:').lower()
                                                if sure in ['yes','y']:
                                                        del students[ind]  
                                                        print('''\n"Deletion Successful"''')
                                                        with open('Data file for student management system.json','w') as f:
                                                                json.dump(students,f)
                                                        break
                                                elif sure in ['no','n']:
                                                        print('''\n"Student data not deleted"''')
                                                        break
                                                else:
                                                        print('''\n"Please enter a coorect option"''')
                                        break
                if inum==0:
                        print('''\n"Student not found"''')
        elif option in ['4','search']:
                inum=0
                s_name=input("\nEnter name of student:").title()
                for d in students:
                        for k,v in d.items():
                                pass                
                                if d['Name']==s_name:
                                        print(" ___________________________________________________________________________________________________________________________")
                                        print("|                                                                                                                           |")
                                        print("|                                              Student   Management   System                                                |")
                                        print("|___________________________________________________________________________________________________________________________|")
                                        print("|___________________________________________________________________________________________________________________________|")
                                        print("|        |                          |      |                                 |                                              |")
                                        print("|  S-No  |              Name        |  Age |            F.Name               |                     Address                  |")
                                        print("|________|__________________________|______|_________________________________|______________________________________________|")
                                        print(f"|{d['S-No']: <8}|{d['Name']: <26}|{d['Age']: <6}|{d['F.Name']: <33}|{d['Address']: <46}|")
                                        print("|________|__________________________|______|_________________________________|______________________________________________|")
                                        break
                                elif d['Name']!=s_name:
                                        inum+=1
                                        break  
                if inum==len(students):
                        print('''\n"Student not found"''')
        elif option in ['5','display']:
                print(" ___________________________________________________________________________________________________________________________")
                print("|                                                                                                                           |")
                print("|                                              Student   Management   System                                                |")
                print("|___________________________________________________________________________________________________________________________|")
                print("|___________________________________________________________________________________________________________________________|")
                print("|        |                          |      |                                 |                                              |")
                print("|  S-No  |              Name        |  Age |            F.Name               |                     Address                  |")
                print("|________|__________________________|______|_________________________________|______________________________________________|")
                for s in students:
                        for k,v in s.items():
                                pass        
                        print(f"|{s['S-No']: <8}|{s['Name']: <26}|{s['Age']: <6}|{s['F.Name']: <33}|{s['Address']: <46}|")
                        print("|________|__________________________|______|_________________________________|______________________________________________|")
        for i in range(len(students)):
                try:
                        del students[i]['S-No']
                except KeyError:
                        pass
        for i in range(len(students)):
                students[i]['S-No']=i+1
        with open('Data file for student management system.json','w') as f:
                json.dump(students,f)
        while True:
                Repeat=input("\nDo you want to repeat?\n\nYes or No:")
                Repeat=Repeat.lower()
                if Repeat not in ["yes","y","no","n"]:
                        print("\nPlease select correct option")
                else:
                        break
        if Repeat in ["yes","y"]:
                continue
        else:
                if Repeat in ["no","n"]:
                        print("\n-----Thank you for using-----")
                        input()
                        break