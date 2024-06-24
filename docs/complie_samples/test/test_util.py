from unittest import TestCase
import util


class TestUtil(TestCase):

    def test_dict2ins(self):
        class T(object):
            def __init__(self, arg, flag=False):
                self.__arg = arg
                self.__flag = flag

        d = {'arg': 'arg_value', 'flag': True}

        ins = T(d.get('arg'), flag=True)

        self.assertEqual(ins._T__arg, util.dict2ins(d, T)._T__arg)
        self.assertEqual(ins._T__flag, util.dict2ins(d, T)._T__flag)
        self.assertRaises(ValueError, util.dict2ins, *(d, ''))

    def test_execute_in_shell_with_ascii(self):
        cmd = 'echo hello!'
        res = util.execute_in_shell(cmd.split(' '))
        self.assertEqual('hello!\n', res)

    def test_execute_in_shell_with_non_ascii(self):
        cmd = 'echo 你好！'
        res = util.execute_in_shell(cmd.split(' '))
        self.assertEqual('你好！\n', res)

    def test_execute_in_shell_with_wrong(self):
        cmd = 'ech hello!'
        self.assertRaises(FileNotFoundError, util.execute_in_shell, cmd.split(' '))
