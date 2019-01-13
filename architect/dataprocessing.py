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

import numpy

class DataProcessing:

    def get_submatrix_3 (self, i_m, i_c_x, i_c_y):
        o_m = numpy.zeros ((3,3))
        shape_x = i_m.shape[0]
        shape_y = i_m.shape[1]
        
        if i_c_x - 1 >= 0 and i_c_y - 1 >= 0 and i_c_x - 1 < shape_x and i_c_y - 1 < shape_y:
            o_m[0][0] = i_m[i_c_x - 1][i_c_y - 1]
        if i_c_x >= 0 and i_c_y - 1 >= 0 and i_c_x < shape_x and i_c_y - 1 < shape_y:
            o_m[1][0] = i_m[i_c_x][i_c_y - 1]
        if i_c_x + 1 >= 0 and i_c_y - 1 >= 0 and i_c_x + 1 < shape_x and i_c_y - 1 < shape_y:
            o_m[2][0] = i_m[i_c_x + 1][i_c_y - 1]

        if i_c_x - 1 >= 0 and i_c_y >= 0 and i_c_x - 1 < shape_x and i_c_y < shape_y:
            o_m[0][1] = i_m[i_c_x - 1][i_c_y]
        if i_c_x >= 0 and i_c_y >= 0 and i_c_x < shape_x and i_c_y <= shape_y:
            o_m[1][1] = i_m[i_c_x][i_c_y]
        if i_c_x + 1 >= 0 and i_c_y >= 0 and i_c_x + 1 < shape_x and i_c_y < shape_y:
            o_m[2][1] = i_m[i_c_x + 1][i_c_y]
            
        if i_c_x - 1 >= 0 and i_c_y + 1 >= 0 and i_c_x - 1 < shape_x and i_c_y + 1 < shape_y:
            o_m[0][2] = i_m[i_c_x - 1][i_c_y + 1]
        if i_c_x >= 0 and i_c_y + 1 >= 0 and i_c_x < shape_x and i_c_y + 1 < shape_y:
            o_m[1][2] = i_m[i_c_x][i_c_y + 1]
        if i_c_x + 1 >= 0 and i_c_y + 1 >= 0 and i_c_x + 1 < shape_x and i_c_y + 1 < shape_y:
            o_m[2][2] = i_m[i_c_x + 1][i_c_y + 1]

        return o_m

    def are_matrices_equal (self, m1, m2):
        return numpy.allclose(m1, m2)

    def is_matrix_zeroed (self, m):
        if numpy.count_nonzero(m) > 0:
            return False
        else:
            return True

    def is_x_correct (self, m, x):
        shape_x = m.shape[0]
        if x >= 0 and x < shape_x:
            return True
        else:
            return False

    def is_y_correct (self, m, y):
        shape_y = m.shape[1]
        if y >= 0 and y < shape_y:
            return True
        else:
            return False
