import unittest
from io import StringIO
import sys

class Test2ndWeek(unittest.TestCase):
    
    def test_print_statements(self):
        # Capture the output during the test
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        print('pg4e >> do it noch....mall...und.., noch!!')
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(), 'pg4e >> do it noch....mall...und.., noch!!')

    def test_conditional_steps(self):
        x = 5
        result = []
        if x < 10:
            result.append('smaller.')
        if x > 20:
            result.append('Bigger.')
        result.append('Finish!')
        self.assertEqual(result, ['smaller.', 'Finish!'])
    
    def test_repeated_steps(self):
        n = 5
        result = []
        while n > 0:
            result.append(n)
            n = n - 1
        result.append('Blastoff!')
        self.assertEqual(result, [5, 4, 3, 2, 1, 'Blastoff!'])

if __name__ == '__main__':
    unittest.main()