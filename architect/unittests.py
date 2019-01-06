#
# Copyright 2019, Marcin Barylski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
# and associated documentation files (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE # LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import unittest
import numpy
import architect

#############################################################
# Unit tests
#############################################################

class TestMethods(unittest.TestCase):
    def test_is_solved_positive(self):
        print ("\ntest_is_solved_positive")
        h = 6
        w = 6
        matrix_excluded = numpy.zeros((h, w))
        matrix_gas = numpy.zeros((h, w))
        matrix_house = numpy.zeros((h, w))
        matrix_house[0][1] = 1
        matrix_house[3][2] = 1
        matrix_house[3][4] = 1
        matrix_house[4][0] = 1
        matrix_house[4][4] = 1
        matrix_house[5][2] = 1
        matrix_house[5][5] = 1
        matrix_gas[0][2] = 1
        matrix_gas[2][2] = 1
        matrix_gas[2][4] = 1
        matrix_gas[3][0] = 1
        matrix_gas[4][3] = 1
        matrix_gas[4][5] = 1
        matrix_gas[5][1] = 1
        wages = [[1,0,2,1,2,1], [1,1,2,1,1,1]]

        a = architect.Architect(matrix_excluded, matrix_gas, matrix_house, wages, h, w)
    
        self.assertTrue(a.is_solved ())

        a.update_excluded()
        a.print()

    def test_is_solved_negative (self):
        print ("\ntest_is_solved_negative")
        h = 6
        w = 6
        matrix_excluded = numpy.zeros((h, w))
        matrix_gas = numpy.zeros((h, w))
        matrix_house = numpy.zeros((h, w))
        matrix_house[0][1] = 1
        matrix_house[3][2] = 1
        matrix_house[3][4] = 1
        matrix_house[4][0] = 1
        matrix_house[4][4] = 1
        matrix_house[5][2] = 1
        matrix_house[5][5] = 1
        matrix_gas[0][2] = 1
        matrix_gas[2][2] = 1
        matrix_gas[2][4] = 1
        matrix_gas[3][0] = 1
        matrix_gas[4][3] = 0
        matrix_gas[4][5] = 1
        matrix_gas[5][1] = 1
        wages = [[1,0,2,1,2,1], [1,1,2,1,1,1]]

        a = architect.Architect(matrix_excluded, matrix_gas, matrix_house, wages, h, w)
    
        self.assertFalse(a.is_solved ())

        a.update_excluded()
        a.print()

    def test_get_submatrix_3 (self):
        print ("\ntest_get_submatrix_3")
        h = 6
        w = 6
        matrix_excluded = numpy.zeros((h, w))
        matrix_gas = numpy.zeros((h, w))
        matrix_house = numpy.zeros((h, w))
        matrix_house[0][1] = 1
        matrix_house[3][2] = 1
        matrix_house[3][4] = 1
        matrix_house[4][0] = 1
        matrix_house[4][4] = 1
        matrix_house[5][2] = 1
        matrix_house[5][5] = 1
        matrix_gas[0][2] = 1
        matrix_gas[2][2] = 1
        matrix_gas[2][4] = 1
        matrix_gas[3][0] = 1
        matrix_gas[4][3] = 1
        matrix_gas[4][5] = 1
        matrix_gas[5][1] = 1
        wages = [[1,0,2,1,2,1], [1,1,2,1,1,1]]

        temp_target_3 = numpy.zeros ((3, 3))
        temp_target_3[1][1] = 1
        
        a = architect.Architect(matrix_excluded, matrix_gas, matrix_house, wages, h, w)

        result1 = numpy.allclose(a.get_submatrix_3(matrix_gas, 2, 2), temp_target_3)
        self.assertTrue(result1)

        result2 = numpy.allclose(a.get_submatrix_3(matrix_gas, 0, 2), temp_target_3)
        self.assertTrue(result2)

        result3 = numpy.allclose(a.get_submatrix_3(matrix_gas, 5, 1), temp_target_3)
        self.assertTrue(result3)

#############################################################
# Main - run unit tests
#############################################################

unittest.main()
