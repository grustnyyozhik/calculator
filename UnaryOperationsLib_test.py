__author__ = ''

import unittest
import UnaryOperationsLib


class MyTestCase(unittest.TestCase):

    knownValues_negate = (
        ('1+', '', '1+', ''),
        ('1+3', '3',  '1+ -3', ' -3'),
        ('0', '0', '0', '0'),
        ('1+8.', '8.', '1+ -8.0', ' -8.0'),
        ('1+ -8.2', ' -8.2', '1+8.2', '8.2'),
    )

    knownValues_square = (
        ('1+', '', '1+', ''),
        ('1+3', '3',  '1+1.73205080757', '1.73205080757'),
        ('0', '0', '0.0', '0.0'),
        ('1+8.', '8.', '1+2.82842712475', '2.82842712475'),
        ('1+ -8.2', ' -8.2', '1+ -8.2', ' -8.2'),
    )

    knownValues_percent = (
        ('1+', '', '1+', ''),
        ('1+3', '3',  '1+0.03', '0.03'),
        ('0', '0', '0.0', '0.0'),
        ('1+8.', '8.', '1+0.08', '0.08'),
        ('1+ -8.2', ' -8.2', '1+ -0.082', ' -0.082'),
    )


    def test_negate_operation(self):

        for exp, value_to_update, res, res_val in self.knownValues_negate:
            res_exp, res_value_to_update = UnaryOperationsLib.negate_operation(exp, value_to_update)
            self.assertEqual(res_exp, res)
            self.assertEqual(res_value_to_update, res_val)

    def test_square_operation(self):

        for exp, value_to_update, res, res_val in self.knownValues_square:
            res_exp, res_value_to_update = UnaryOperationsLib.square_operation(exp, value_to_update)
            self.assertEqual(res_exp, res)
            self.assertEqual(res_value_to_update, res_val)

    def test_percent_operation(self):
        for exp, value_to_update, res, res_val in self.knownValues_percent:
            res_exp, res_value_to_update = UnaryOperationsLib.percent_operation(exp, value_to_update)
            self.assertEqual(res_exp, res)
            self.assertEqual(res_value_to_update, res_val)



if __name__ == '__main__':
    unittest.main()
