from typing import Union
import unittest

Num = Union[int, float]


def sum3(x: Num, y: Num, z: Num) -> Num:
    return x + y + z


def avg3(x: Num, y: Num, z: Num) -> Num:
    return sum3(x, y, z) / 3


class Test1(unittest.TestCase):
    def test_sum3(self):
        self.assertEqual(sum3(1, 2, 3), 6)

    def test_avg3(self):
        self.assertEqual(avg3(1, 2, 3), 2)


if __name__ == "__main__":
    unittest.main()
