from student_manage import Student, StudentManageSytem
import unittest


class Test2(unittest.TestCase):
    def test_add_student(self):

        sms = StudentManageSytem([["miaooo", 233], Student("genshin", 666)])
        sms.add_student(Student("mihoyo", 123))
        self.assertEqual(
            set(sms.students),
            set(
                (
                    Student("miaooo", 233),
                    Student("genshin", 666),
                    Student("mihoyo", 123),
                )
            ),
        )
        self.assertEqual(sms.ids, set((233, 666, 123)))

    def test_delete_student_by_id(self):
        sms = StudentManageSytem([["miaooo", 233], Student("genshin", 666)])
        sms.del_student_by_id(666)
        self.assertEqual(sms.students, [Student("miaooo", 233)])
        self.assertEqual(sms.ids, set((233,)))

    def test_del_student_by_name(self):
        sms = StudentManageSytem([["miaooo", 233], Student("genshin", 666)])
        sms.del_student_by_name("genshin")
        print([str(s) for s in sms.students], [str(Student("miaooo", 233))])
        self.assertEqual(sms.students, [Student("miaooo", 233)])
        self.assertEqual(sms.ids, set((233,)))


if __name__ == "__main__":
    unittest.main()
