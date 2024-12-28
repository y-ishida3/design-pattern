import os
import sys
import unittest

sys.path.append(os.path.abspath(__name__).replace('__main__', ''))
from src.singleton import NormalSingleton, LobustSingleton


class TestNormalSingleton(unittest.TestCase):

    def test_success_one_construct(self):
        value1 = 1
        value2 = 5
        ns1: NormalSingleton = NormalSingleton(value1=value1, value2=value2)
        ns2: NormalSingleton = NormalSingleton(value1=value1*3, value2=value2*3)

        self.assertEqual(ns1.value1, ns2.value1)
        self.assertEqual(ns1.value2, ns2.value2)
        self.assertEqual(ns1, ns2)


class TestLobustSingleton(unittest.TestCase):

    def test_success_one_construct(self):
        value1 = 1
        value2 = 5
        ls1: LobustSingleton = LobustSingleton(value1=value1, value2=value2)
        ls2: LobustSingleton = LobustSingleton()

        self.assertEqual(ls1.value1, ls2.value1)
        self.assertEqual(ls1.value2, ls2.value2)
        self.assertEqual(ls1, ls2)

    def test_success_raise_type_error(self):
        value1 = 1
        value2 = 5
        ls1: LobustSingleton = LobustSingleton(value1=value1, value2=value2)
        with self.assertRaises(TypeError):
            ls2: LobustSingleton = LobustSingleton(value1=value1*3, value2=value2*3)

    def test_success_raise_frozen_instance_error(self):
        from dataclasses import FrozenInstanceError

        value1 = 1
        value2 = 5
        ls1: LobustSingleton = LobustSingleton(value1=value1, value2=value2)
        with self.assertRaises(FrozenInstanceError):
            ls1.value1 = 5


if __name__ == '__main__':
    unittest.main()
