# 代码很抽象但是能跑
# 代码跑不了也没事毕竟我也能跑qaq


def Menu():
    print('-' * 10)
    print('a: 添加学员')
    print('b: 删除学员')
    print('c: 修改学员信息')
    print('d: 查询学员信息')
    print('e: 显示所有学员信息')
    print('f: 退出系统')
    print('-' * 10)


def searchId(target_id):  # 查询id为 *** 的学生
    for i in studentInfo:
        if i['id'] == target_id:
            print(i)
            return
        else:
            print('The student is not in the list.')


def addStudent():  # 添加id为 *** 的学生信息
    global studentInfo

    addId = int(input('Put id number here:'))
    addName = input('Put name here:')

    for i in studentInfo:
        if i['id'] == addId:
            print("The student already exits.")
            return

    stu_dict = {'name': addName, 'id': addId}

    studentInfo.append(stu_dict)

    print(studentInfo)


def delStudent():  # 删除id为 *** 的学生信息
    print(studentInfo)
    delId = int(input('Put the id here:'))
    studentInfo.pop(searchId(delId))
    print(studentInfo)


def changeStudent():  # 修改id为 *** 的学生信息
    print(studentInfo)
    changeId = int(input('Put the id-to-change here:'))
    for i in studentInfo:
        if i['id'] == changeId:
            changeName = input('Put new name here:')
            i['name'] = changeName
            print(studentInfo)


def searchStudent():  # 查询id为 *** 的学生信息
    target_id = int(input('Put the id here:'))
    searchId(target_id)


def showStudent():
    print(studentInfo)


def main():
    while True:
        Menu()

        MenuFunction = input('Enter a letter to use its function:')

        if MenuFunction == 'a':
            print('Add stu')
            addStudent()
        elif MenuFunction == 'b':
            print('Del stu')
            delStudent()
        elif MenuFunction == 'c':
            print('Change stuinfo')
            changeStudent()
        elif MenuFunction == 'd':
            print('Search stuinfo')
            searchStudent()
        elif MenuFunction == 'e':
            print('Show all the stuinfo')
            showStudent()
        elif MenuFunction == 'f':
            print('Thanks for using this program')
            return
        else:
            print('Unknown function, please enter again')









studentInfo = []
main()
