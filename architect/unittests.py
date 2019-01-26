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
import sys
import architect
import dataprocessing

#############################################################
# Unit tests
#############################################################

class TestMethods(unittest.TestCase):
    def test_is_solved_positive(self):
        print ("\n TEST CASE:", sys._getframe().f_code.co_name)
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

        dp = dataprocessing.DataProcessing ()
        a = architect.Architect(dp, matrix_excluded, matrix_gas, matrix_house, wages, h, w)
    
        self.assertTrue(a.is_solved ())

        a.update_excluded()
        a.print()

    def test_is_solved_negative (self):
        print ("\n TEST CASE:", sys._getframe().f_code.co_name)
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

        dp = dataprocessing.DataProcessing ()
        a = architect.Architect(dp, matrix_excluded, matrix_gas, matrix_house, wages, h, w)
    
        self.assertFalse(a.is_solved ())

        a.update_excluded()
        a.print()

    def test_is_matrix_zeroed (self):
        print ("\n TEST CASE:", sys._getframe().f_code.co_name)

        dp = dataprocessing.DataProcessing ()

        m = numpy.zeros((10, 10))
        self.assertTrue(dp.is_matrix_zeroed(m))

    def test_is_matrix_zeroed_negative (self):
        print ("\n TEST CASE:", sys._getframe().f_code.co_name)
        dp = dataprocessing.DataProcessing ()

        m = numpy.zeros((10, 10))
        m[2][2] = 1
        self.assertFalse(dp.is_matrix_zeroed(m))

    def test_are_matrices_equal (self):
        print ("\n TEST CASE:", sys._getframe().f_code.co_name)

        dp = dataprocessing.DataProcessing ()

        m1 = numpy.zeros((10, 10))
        m1[1][2] = 1
        m2 = numpy.zeros((10, 10))
        m2[1][2] = 1
        self.assertTrue(dp.are_matrices_equal(m1, m2))

    def test_are_matrices_equal_negative (self):
        print ("\n TEST CASE:", sys._getframe().f_code.co_name)

        dp = dataprocessing.DataProcessing ()

        m1 = numpy.zeros((10, 10))
        m1[1][2] = 1
        m2 = numpy.zeros((10, 10))
        self.assertFalse(dp.are_matrices_equal(m1, m2))

    def test_get_submatrix_3 (self):
        print ("\n TEST CASE:", sys._getframe().f_code.co_name)
        matrix_gas = numpy.zeros((6, 6))
        matrix_gas[0][2] = 1
        matrix_gas[2][2] = 1
        matrix_gas[2][4] = 1
        matrix_gas[3][0] = 1
        matrix_gas[4][3] = 1
        matrix_gas[4][5] = 1
        matrix_gas[5][1] = 1

        temp_target_3 = numpy.zeros ((3, 3))
        temp_target_3[1][1] = 1
        
        dp = dataprocessing.DataProcessing ()

        result1 = numpy.allclose(dp.get_submatrix_3(matrix_gas, 2, 2), temp_target_3)
        self.assertTrue(result1)

        result2 = numpy.allclose(dp.get_submatrix_3(matrix_gas, 0, 2), temp_target_3)
        self.assertTrue(result2)

        result3 = numpy.allclose(dp.get_submatrix_3(matrix_gas, 5, 1), temp_target_3)
        self.assertTrue(result3)

    def test_get_combinations (self):
        print ("\n TEST CASE:", sys._getframe().f_code.co_name)

        dp = dataprocessing.DataProcessing ()

        c1 = dp.get_combinations ([(1,1),(2,3),(3,2)], 1)
        self.assertEqual (c1, [((1,1),), ((2,3),), ((3,2),)])

        c2 = dp.get_combinations ([(1,1),(2,3),(3,2)], 2)
        self.assertEqual (c2, [((1,1),(2,3),), ((1,1),(3,2)), ((2,3),(3,2),)])

        c3 = dp.get_combinations ([(1,1),(2,3),(3,2)], 3)
        self.assertEqual (c3, [((1,1),(2,3),(3,2),)])

#############################################################
# Main - run unit tests
#############################################################

unittest.main()
