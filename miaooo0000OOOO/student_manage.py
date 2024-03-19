class Student:
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    def __eq__(self, __value) -> bool:
        return self.name == __value.name and self.id == __value.id

    def __hash__(self) -> int:
        # unsafe hash
        # but fast
        return hash(self.name) + self.id

    def __str__(self):
        return 'Student(name: "{}", id: {})'.format(self.name, self.id)


def stu_from(t) -> Student:
    return Student(t[0], t[1])


class StudentManageSytem:
    def __init__(self, students) -> None:
        if students is None:
            self.students = []
        else:
            self.students = students
        for i in range(len(self.students)):
            if type(self.students[i]) != Student:
                self.students[i] = stu_from(self.students[i])
        self.ids = set([stu.id for stu in self.students])
        if len(self.ids) != len(self.students):
            raise ValueError

    def add_student(self, stu: Student) -> bool:
        if stu.id in self.ids:
            return False
        self.ids.add(stu.id)
        self.students.append(stu)
        return True

    def del_student_by_id(self, id: int) -> bool:
        if id not in self.ids:
            return False
        for i, stu in enumerate(self.students):
            if stu.id == id:
                break
        self.students.pop(i)
        self.ids.discard(id)
        return True

    def del_student_by_name(self, name) -> bool:
        for i, stu in enumerate(self.students):
            if stu.name == name:
                id_del = stu.id
                break
        else:
            return False
        self.students.pop(i)
        self.ids.discard(id_del)

    def get_student_by_id(self, id):
        for i, stu in enumerate(self.students):
            if stu.id == id:
                return stu
        return None

    def get_student_by_name(self, name):
        for i, stu in enumerate(self.students):
            if stu.name == name:
                return stu
        return None

    def set_student_by_id(self, id, stu):
        if id == stu.id:
            return False
        for i, stu in enumerate(self.students):
            if stu.id == id:
                self.students[i] = stu
                return True
        return False

    def set_student_by_name(self, name, stu):
        for i, stu in enumerate(self.students):
            if stu.name == name:
                self.students[i] = stu
                return True
        return False

    def print(self):
        for stu in self.students:
            print(str(stu))

    def gui_once(self) -> bool:
        print(
            """1: 添加学员
2: 删除学员
3: 修改学员信息
4: 查询学员信息
5: 显示所有学员
6: 退出系统"""
        )
        key = int(input())
        if key == 6:
            return False
        if key == 1:  # 添加学员
            print("请输入学员学号和姓名(空格分隔)")
            id, name = input().split()
            id = int(id)
            if self.add_student(Student(name, id)):
                print("已添加")
            else:
                print("学号重复")
        elif key == 2:
            print("请输入要删除的学号或姓名")
            i = input()
            try:
                i = int(i)
                if self.del_student_by_id(i):
                    print("已删除")
                else:
                    print("您所输入的学号不存在")
            except ValueError:
                if self.del_student_by_name(i):
                    print("已删除")
                else:
                    print("您所输入的姓名不存在")
        elif key == 3:
            print("请输入要修改的学号")
            i = int(input())
            if not i in self.ids:
                print("没有此学号")
            else:
                print("请输入学员学号和姓名(空格分隔)")
                id, name = input().split()
                id = int(id)
                if self.set_student_by_id(i, Student(name, id)):
                    print("已添加")
                else:
                    print("学号重复")
        elif key == 4:
            print("请输入要查询的学号或姓名")
            i = input()
            try:
                i = int(i)
                stu = self.get_student_by_id(i)
                if stu is None:
                    print("您所输入的学号不存在")
                else:
                    print(str(stu))
            except ValueError:
                stu = self.get_student_by_name(i)
                if stu is None:
                    print("您所输入的姓名不存在")
                else:
                    print(str(stu))
        elif key == 5:
            self.print()
        return True

    def gui(self):
        while self.gui_once():
            print()


if __name__ == "__main__":
    sms = StudentManageSytem(None)
    sms.gui()
