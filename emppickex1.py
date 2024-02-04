#program for reading employee details from KBD and save then in file by using  pickling process
#emppickex1.py
import pickle
def saveempdata():
    with open("emp.pick","ab") as fp:
        #accept employee details from keyboard
        while(True):
            try:
                print("="*70)
                eno=int(input("enter employee number:"))
                ename=input("employee name:")
                esal=float(input("employee sal:"))
                empdsg=input("employee designation:")
                print("========================================")
                #create an empty object of list
                l=list()
                l.append(eno)
                l.append(ename)
                l.append(esal)
                l.append(empdsg)
                #save or write the list object to the file
                pickle.dump(l,fp)
                print("employee record saved successfully")
                print("===========================================")
                ch=input("do you want to enter the another record in employee file(y/n")
                if(ch.lower()=="no"):
                    break
            except ValueError:
                print("don't enter alnums,strs,symbols for eno and sal")
#main program
saveempdata()
