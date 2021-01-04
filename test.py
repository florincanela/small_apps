import unittest
import guessing

class Test(unittest.TestCase):
    def test1(self):
        answer = 5
        guess = 5
        a = 1
        b = 10
        result = guessing.function1(guess, answer, a, b)
        self.assertTrue(result)

    def test2(self):
        answer = 5
        guess = 3
        a = 1
        b = 10
        result = guessing.function1(guess, answer, a, b)
        self.assertFalse(result)

    def test3(self):
        answer = 5
        guess = -1
        a = 1
        b = 10
        result = guessing.function1(guess, answer, a, b)
        self.assertFalse(result)

    def test4(self):
        answer = 5
        guess = '2'
        a = 1
        b = 10
        self.assertRaises(TypeError, guessing.function1, guess, answer, a, b)

if __name__ == '__main__':
    unittest.main()