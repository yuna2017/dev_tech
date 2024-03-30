import random,os

def basicprint(taap,mode0):
    print("已进入设置模式"+"\n")
    print("请选择默认模式，目前模式为"+"\""+ mode0[taap] +"\""+"："+"\n")
    print(" 等概率模式输入0"+"\n")
    print(" 概率被调整模式输入1"+"\n")
    print(" 显示调整概率输入2"+"\n")
    print(" 调整概率输入3"+"\n")

def find(k,a):
    l = len(a)
    for i in range(l):
        if a[i] == k :
            return i
            break

mode0=["等概率模式","概率被调整模式","显示调整概率","调整概率"]

#模式判断读取
judge1 = []
judge = open(r'data\judge1.txt')
for line in judge:
    line = line.replace("\n", "")
    judge1.append(line)
judge.close()

taap = int(judge1[0])

i=0
name1=[]
na = open("名单.txt")#基础名单输入
for line in na:
    line = line.replace("\n","")
    name1.append(1)
    name1[i] = line
    i=i+1
na.close()

kind=[]
number=[]

for i in range(len(name1)):#种类数量 统计
    k=name1[i]
    a=kind
    len1=len(kind)
    if i ==0:
        kind.append(1)
        kind[0]=name1[0]
        number.append(1)
    elif k in a ==False:
        kind.append(1)
        kind[len1]=k
        number.append(1)
    elif k in a ==True:
        number[find(k,a)]=number[find(k,a)]+1
###



print("输入回车开始抽取，输入option进行设置")
mode=input("输入stop停止程序，默认模式为"+" "+mode0[taap]+" "+"\n")
kp=[0]

while 1:
    if mode=="stop":
        break

    if mode=="option":
        os.system("cls")
        basicprint(taap,mode0)
        print("如果该次模式调整需要保存，请先输入sav，回车后输入模式")
        print("另：如果你进行了概率调整或者保存模式调整，请一定打stop退出，不然下次会崩溃")
        modejudgement = input("mode=")
        if modejudgement=="sav":  
            mode2 = input("mode=")
            f=open(r'd:\data\judge1.txt',"w+")
            f.write(str(taap))
            f.close
            taap=int(mode2)
        else:
            taap=int(modejudgement)
        print("\n"+"当前模式为"+mode0[taap]+"\n")
        mode = input("确定该模式，请输入回车")

    if taap == 0 :
        os.system("cls")
        mode=taap
        print("\n"+"==抽取开始=="+"\n"+"\n"+"\n")
        while mode!="stop" and mode!="option":
            print("=="+random.choice(kind)+"=="+"\n")
            mode=input("输入stop停止抽取,输入option进行设置:")
            print("\n")

    if taap == 3:
        os.system("cls")
        for listline in range(len(kind)):
            l=1+int(listline)
            print(str(l)+' '+kind[listline]+' 次数:'+str(number[listline]))
        print("调整当前概率请输入change，若不调整请输入回车")
        bool0=input()
        bool1=0
        if bool0 == "change":
            while bool1!="ok":
                i1 = int(input('输入需要调整人的序号'))-1
                i2 = int (input('输入需要的次数（不能小于0）'))
                bool1=input('调整完请输入ok，继续请回车')
                number[i1]=i2
            
        k=open(r'd:\data\list1.txt',"w+")
        changekind=[]#重置change数列
        changenumber=[]
        for line in range(len(kind)):
            k.write(kind[line]+' '+str(number[line])+"\n")
            changekind.append(1)
            changenumber.append(1)
            changekind[line]=kind[line]
            changenumber[line]=number[line]
        k.close
        
        bool2=input('将按照该概率进行抽取，确认请输入回车，继续调整请输入change，使用等概率请输入back'+"\n")
        taap=1
        if bool2=="change":
            taap=3
        elif bool2=="back":
            taap=0
        kp[0]=kp[0]+1
            
    if taap ==1:
        #读取改变的名单
        if kp[0]!=0:
            changekind=changekind
            changenumber=changenumber
        else:
            kp[0]=0
            changedata={ }                                
            f=open(r'd:\data\list1.txt')
            for line in f:
                list1=[]
                line = line.replace("\n","")
                list1=line.split(" ")
                changedata[list1[0]]=list1[1]
            f.close() 

            changekind=list(changedata.keys())
            changenumber=list(changedata.values())
        
        os.system("cls")
        rangelist=[]

        for lenth in range(len(kind)):
            if changenumber[lenth] == 0:
                break
            else :
                for i in range(int(changenumber[lenth])):
                    rangelist.append(1)
                    rangelist[len(rangelist)-1]=changekind[lenth]
        mode=taap
        while mode!="stop" and mode!="option":
            print("=="+random.choice(rangelist)+"=="+"\n")
            mode=input("输入stop停止抽取,输入option进行设置:")
            print("\n")

    if taap == 2:
        os.system("cls")
        for listline in range(len(changekind)):
            l=1+int(listline)
            print(str(l)+' '+changekind[listline]+' 次数:'+str(changenumber[listline]))
        bool2=input('将按照该概率进行抽取，确认请输入回车，使用等概率请输入back'+"\n")
        taap=1
        if bool2=="back":
            taap=0