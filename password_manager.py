#------------------------------create a text file in python
import os.path

def checkExistence():
    if os.path.exists('info.text'):
        pass
    else:
        file = open('info.text', 'w')
        file.close
checkExistence()
#------------------------------write to file
def appendNew():
    file = open('info.text' , 'a')

    print()
    print()

    user_name = input('please enter the user name : ')
    password = input('please enter the password here : ')
    website = input('please enter the website address here : ')

    print()
    print()

    usrnm = 'user_name : ' + user_name + '\n'
    pwd = 'password : ' + password + '\n'
    web = 'website : ' + website + '\n'


    file.write('--------------------------------------------\n')
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write('--------------------------------------------\n')
    file.write('\n')
    file.close
appendNew()
#------------------------------output the password
def readPassword():
    file = open('info.text' , 'r')
    content = file.read()
    file.close()
    print(content)

readPassword()