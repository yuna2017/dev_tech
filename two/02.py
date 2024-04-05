def add_student():
    print("添加学员")
def delete_student():
    print("删除学员")
def modify_student():
    print("修改学员信息")
def query_student():
    print("查询学员信息")
def display_all_students():
    print("显示所有学员信息")
def exit_system():
    print("退出系统")

while True:
    print("""
    欢迎来到学生管理系统
    1. 添加学员
    2. 删除学员
    3. 修改学员信息
    4. 查询学员信息
    5. 显示所有学员信息
    6. 退出系统
    请选择：""")
    choice = input()

    if choice == '1':
        add_student()
    elif choice == '2':
        delete_student()
    elif choice == '3':
        modify_student()
    elif choice == '4':
        query_student()
    elif choice == '5':
        display_all_students()
    elif choice == '6':
        exit_system()
    else:
        print("无效输入，请重新选择")

