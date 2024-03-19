stus=[]
def showmenu():
    print("*"*20)
    print("demo")
    print("添加学员扣1")
    print("删除学员扣2")
    print("修改学员信息扣3")
    print("查询学员信息扣4")
    print("显示所有信息扣5")
    print("退出系统扣0")
    print("*"*20)
class students:
    name="0"
    ID=0
    Tele=0
def addstu():
    s=students()
    print("输入姓名：")
    s.name=input("")
    print("输入ID：")
    s.ID=int(input(""))
    print("输入电话：")
    s.Tele=int(input(""))
    stus.append(s)
def searchstu():
    if len(stus)==0:
        print("无信息！")
        return
    else:
        print("请选择检索方式：1.姓名 2.ID 3.电话")
        a=int(input())
        print("输入相应内容：")
        if a==1:
            b=input()
        else:
            b=int(input())
        Index=-1
        for i in stus:
            Index+=1
            if a==1:
                if b==i.name:
                    print(f"信息:姓名:{i.name} ID:{i.ID} Tele:{i.Tele}")
                    a=0
                    return Index
            if a==2:
                if b==i.ID:
                    print(f"信息:姓名:{i.name} ID:{i.ID} Tele:{i.Tele}")
                    a=0
                    return Index
            if a==3:
                if b == i.Tele:
                    print(f"信息:姓名:{i.name} ID:{i.ID} Tele:{i.Tele}")
                    a=0
                    return Index
            if a!=0:
                print("未检测到相应信息")
                c="一一四五一四"
                return c
def delstu():
    print("删除ing")
    m=searchstu()
    if m!="一一四五一四":
        print("确认删除？（y or n）")
        t=input()
        if t=="y":
            del stus[m]
            print("删除成功")
        else:
            return
    return
def showall():
    for i in range(0,len(stus)):
        print(f"姓名:{stus[i].name} ID:{stus[i].ID} Tele:{stus[i].Tele}")
def changestu():
    print("修改ing")
    m = searchstu()
    if m != "一一四五一四":
        print("输入姓名：")
        stus[m].name = input()
        print("输入ID：")
        stus[m].ID= int(input(""))
        print("输入电话：")
        stus[m].Tele = int(input(""))
        print("修改成功")
showmenu()
while(True):
    showmenu()
    choice=(int)(input())
    match(choice):
        case 1:
            addstu()
            showmenu()
        case 2:
            delstu()
            showmenu()
        case 3:
            changestu()
            showmenu()
        case 4:
            searchstu()
            showmenu()
        case 5:
            showall()
            showmenu()
        case 0:
            exit()
        case _:
            print("重新输入")
