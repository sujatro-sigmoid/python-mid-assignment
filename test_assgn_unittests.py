import unittest
import python_assgn_exception_tdd


class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        log = python_assgn_exception_tdd.Logger()
        self.assertEqual(log.answer_stream(
            [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]),
            [True, True, False, False, False, True])
        del log

    def test_case_2(self):
        log = python_assgn_exception_tdd.Logger()
        self.assertEqual(log.answer_stream(
            [[1, "foo"], [11, "foo"], [21, "foo"], [31, "foo"], [41, "foo"]]),
            [True, True, True, True, True])
        del log

    def test_case_3(self):
        log = python_assgn_exception_tdd.Logger()
        self.assertEqual(log.answer_stream([]), [])
        del log

    def test_case_4(self):
        log = python_assgn_exception_tdd.Logger()
        self.assertEqual(log.answer_stream(
            [[0, "aaaaa"], [1, "bbbbb"], [21, "aaaaa"], [22, "bbbbb"], [30, "aaaaa"], [32, "bbbbb"]]),
            [True, True, True, True, False, True])
        del log

    def test_case_5(self):  # invalid data types
        log = python_assgn_exception_tdd.Logger()
        self.assertRaises(python_assgn_exception_tdd.InvalidTypeError,
                          log.answer_stream, [[-9, 1.5], [2, "bar"], [3, "foo"]])

    def test_case_6(self):  # inputs violating constraints #1
        log = python_assgn_exception_tdd.Logger()
        self.assertRaises(python_assgn_exception_tdd.InputsViolatingConstraintsError,
                          log.answer_stream, [[-1, "foo"], [2, "boo"], [3, "foo"]])

    def test_case_7(self):  # inputs violating constraints #2
        log = python_assgn_exception_tdd.Logger()
        self.assertRaises(python_assgn_exception_tdd.InputsViolatingConstraintsError,
                          log.answer_stream, [[1, "foo"], [2, "aaaaaaaaaabbbbbbbbbbccccccccccd"], [3, "foo"]])

    def test_case_8(self):  # timestamp not in order
        log = python_assgn_exception_tdd.Logger()
        self.assertRaises(python_assgn_exception_tdd.TimestampsNotInOrderError,
                          log.answer_stream, [[1, "foo"], [5, "boo"], [3, "foo"]])


if __name__ == '__main__':
    unittest.main()

    
