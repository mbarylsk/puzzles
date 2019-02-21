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
import architect
import dataprocessing

dp = dataprocessing.DataProcessing ()

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
wages = [[1,0,2,1,2,1], [1,1,2,1,1,1]]

a1 = architect.Architect(dp, matrix_excluded, matrix_gas, matrix_house, wages, h, w, True)
a1.print (False)
a1.solve ()
print (a1.matrix_gas)

h = 12
w = 12
matrix_excluded = numpy.zeros((h, w))
matrix_gas = numpy.zeros((h, w))
matrix_house = numpy.zeros((h, w))
matrix_house[0][6] = 1
matrix_house[0][8] = 1
matrix_house[0][10] = 1
matrix_house[1][2] = 1
matrix_house[1][3] = 1
matrix_house[1][6] = 1
matrix_house[1][9] = 1
matrix_house[2][10] = 1
matrix_house[3][1] = 1
matrix_house[3][3] = 1
matrix_house[3][5] = 1
matrix_house[4][6] = 1
matrix_house[4][9] = 1
matrix_house[5][4] = 1
matrix_house[5][10] = 1
matrix_house[6][0] = 1
matrix_house[6][2] = 1
matrix_house[6][9] = 1
matrix_house[8][0] = 1
matrix_house[8][5] = 1
matrix_house[8][9] = 1
matrix_house[9][1] = 1
matrix_house[9][4] = 1
matrix_house[9][7] = 1
matrix_house[9][10] = 1
matrix_house[9][11] = 1
matrix_house[10][2] = 1
matrix_house[11][2] = 1
matrix_house[11][7] = 1
matrix_house[11][9] = 1
matrix_house[11][11] = 1

wages = [[5,1,2,4,0,5,0,4,2,3,2,3], [4,2,2,3,1,3,3,2,1,5,0,5]]

a2 = architect.Architect(dp, matrix_excluded, matrix_gas, matrix_house, wages, h, w, True)
a2.print (False)
a2.solve ()
