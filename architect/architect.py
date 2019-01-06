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

class Architect:

    def __init__(self, me, mc, mh, wg, h, w):
        self.matrix_excluded = me
        self.matrix_container = mc
        self.matrix_house = mh
        self.wages = wg
        self.h = h
        self.w = w

    def print (self):
        print ("\n")
        border = "+"
        for i in range(self.w):
            border += "---"
        border += "+"
        print (border)
        for i in range(self.h):
            line = " "
            for j in range(self.w):
                if self.matrix_house[i][j] == 1:
                    line+= " H "
                elif self.matrix_container[i][j] == 1:
                    line+= " o "
                elif self.matrix_excluded[i][j] == 1:
                    line+= " . "
                if self.matrix_excluded[i][j] == 0 and self.matrix_container[i][j] == 0 and self.matrix_house[i][j] == 0:
                    line+= " _ "
            print (line)
        print (border)
        print ("\nLegend:")
        print (" H - house")
        print (" o - gas")
        print (" . - field excluded from analysis")
        print (" _ - unknown")
        

    def is_solved (self):

        # check if wages match number of containers - horizontally
        for i in range(self.h):
            temp_sum = 0
            for j in range(self.w):
                temp_sum += self.matrix_container[i][j]
            if temp_sum != self.wages[0][i]:
                return False

        # check if wages match number of containers - vertically
        for j in range(self.h):
            temp_sum = 0
            for i in range(self.w):
               temp_sum += self.matrix_container[i][j]
            if temp_sum != self.wages[1][j]:
                return False

        # check if houses and containers do not overlap
        temp_sum_containers = 0
        temp_sum_houses = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.matrix_container[i][j] == 1 and self.matrix_house[i][j] == 1:
                    return False
                temp_sum_containers += self.matrix_container[i][j]
                temp_sum_houses += self.matrix_house[i][j]

        # number of houses must match number of containers
        if temp_sum_containers != temp_sum_houses:
            return False

        # check if containers are not direct neighbours
        for i in range(self.h):
            for j in range(self.w):
                if self.matrix_container[i][j] == 1:
                    temp_submatrix_3 = self.get_submatrix_3 (self.matrix_container, i, j)
                    temp_target_3 = numpy.zeros ((3, 3))
                    temp_target_3[1][1] = 1
                    if not numpy.allclose(temp_submatrix_3, temp_target_3):
                        return False
    
        return True

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

    def update_excluded (self):

        # exlude fields where is either house or container
        for i in range(self.h):
            for j in range(self.w):
                if self.matrix_house[i][j] == 1:
                    self.matrix_excluded[i][j] = 1

                if self.matrix_container[i][j] == 1:
                    self.matrix_excluded[i][j] = 1

        # if wages are 0
        for i in range(self.h):
            if self.wages[0][i] == 0:
                for j in range(self.w):
                    self.matrix_excluded[i][j] = 1

        for j in range(self.w):
            if self.wages[1][j] == 0:
                for i in range(self.w):
                    self.matrix_excluded[i][j] = 1

        # each containes must have space around
        shape_x = self.matrix_container.shape[0]
        shape_y = self.matrix_container.shape[1]
        for i in range(self.h):
            for j in range(self.w):
                if self.matrix_container[i][j] == 1:
                    if i-1 >= 0:
                        self.matrix_excluded[i-1][j] = 1
                    if i+1 < shape_x:
                        self.matrix_excluded[i+1][j] = 1
                    if j-1 >= 0:
                        self.matrix_excluded[i][j-1] = 1
                    if j+1 < shape_y:
                        self.matrix_excluded[i][j+1] = 1
                    if i-1 >= 0 and j-1 >= 0:
                        self.matrix_excluded[i-1][j-1] = 1
                    if i+1 < shape_x and j+1 < shape_y:
                        self.matrix_excluded[i+1][j+1] = 1
                    if i-1 >= 0 and j+1 < shape_y:
                        self.matrix_excluded[i-1][j+1] = 1
                    if i+1 < shape_x and j-1 >= 0:
                        self.matrix_excluded[i+1][j-1] = 1
