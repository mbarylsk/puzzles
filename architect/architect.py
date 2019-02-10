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
import dataprocessing

GAS_CANDIDATE = 1
GAS_HOUSE_NORTH = 2
GAS_HOUSE_EAST = 3
GAS_HOUSE_SOUTH = 4
GAS_HOUSE_WEST = 5

class Architect:

    def __init__(self, dp, me, mg, mh, wg, h, w, verbosity):
        self.dp = dp
        self.matrix_excluded = me
        self.matrix_gas = mg
        self.matrix_house = mh
        self.wages = wg
        self.h = h
        self.w = w
        self.verbose = verbosity
        self.score = 0
        self.matrix_excluded_temp = me
        self.matrix_gas_temp = mg
        self.matrix_house_temp = mh

    def print (self, print_temp):
        print ("\n")
        border = "+"
        for i in range(self.w):
            border += "---"
        border += "+"
        print (border)
        if print_temp:
            print ("Best score so far...\n")
        for i in range(self.h):
            line = " "
            for j in range(self.w):
                if self.is_house(i, j, print_temp):
                    line+= " H "
                elif self.is_gas_any (i, j, print_temp):
                    line+= " o "
                elif self.is_excluded (i, j, print_temp):
                    line+= " . "
                if not self.is_excluded (i, j, print_temp) and not self.is_gas_any (i, j, print_temp) and not self.is_house (i, j, print_temp):
                    line+= " _ "
            print (line)
        print (border)
        print ("\nLegend:")
        print (" H - house")
        print (" o - gas")
        print (" . - field excluded from analysis")
        print (" _ - unknown")

    def is_gas (self, x, y, value, use_temp):
        if use_temp:
            if self.dp.is_x_correct (self.matrix_gas_temp, x) and self.dp.is_x_correct (self.matrix_gas_temp, y) and self.matrix_gas_temp [x][y] == 1:
                return True
            return False
        else:
            if self.dp.is_x_correct (self.matrix_gas, x) and self.dp.is_x_correct (self.matrix_gas, y) and self.matrix_gas [x][y] == value:
                return True
            return False

    def is_gas_any (self, x, y, use_temp):
        if use_temp:
            if self.dp.is_x_correct (self.matrix_gas_temp, x) and self.dp.is_x_correct (self.matrix_gas_temp, y) and self.matrix_gas_temp [x][y] > 0:
                return True
            return False
        else:
            if self.dp.is_x_correct (self.matrix_gas, x) and self.dp.is_x_correct (self.matrix_gas, y) and self.matrix_gas [x][y] > 0:
                return True
            return False

    def is_gas_candidate (self, x, y):
        if self.dp.is_x_correct (self.matrix_gas, x) and self.dp.is_x_correct (self.matrix_gas, y) and self.matrix_gas [x][y] == GAS_CANDIDATE:
            return True
        return False

    def is_house (self, x, y, use_temp):
        if use_temp:
            if self.dp.is_x_correct (self.matrix_house_temp, x) and self.dp.is_x_correct (self.matrix_house_temp, y) and self.matrix_house_temp [x][y] > 0:
                return True
            return False
        else:
            if self.dp.is_x_correct (self.matrix_house, x) and self.dp.is_x_correct (self.matrix_house, y) and self.matrix_house [x][y] > 0:
                return True
            return False

    def is_house_without_gas (self, x, y, use_temp):
        if self.is_gas(x-1, y, GAS_HOUSE_SOUTH, False):
            return False
        if self.is_gas(x+1, y, GAS_HOUSE_NORTH, False):
            return False
        if self.is_gas(x, y-1, GAS_HOUSE_EAST, False):
            return False
        if self.is_gas(x, y+1, GAS_HOUSE_WEST, False):
            return False
        return True

    def is_empty (self, x, y, use_temp):
        if not self.is_gas_any (x, y, use_temp) and not self.is_house (x, y, use_temp) and not self.is_excluded(x, y, use_temp):
            return True
        else:
            return False

    def is_house_with_gas (self, x, y):
        if self.is_house (x, y, False):
            if self.is_gas(x-1, y, GAS_HOUSE_SOUTH, False):
                return True
            if self.is_gas(x+1, y, GAS_HOUSE_NORTH, False):
                return True
            if self.is_gas(x, y-1, GAS_HOUSE_EAST, False):
                return True
            if self.is_gas(x, y+1, GAS_HOUSE_WEST, False):
                return True
        return False

    def is_excluded (self, x, y, use_temp):
        if use_temp:
            if self.dp.is_x_correct (self.matrix_excluded_temp, x) and self.dp.is_x_correct (self.matrix_excluded_temp, y) and self.matrix_excluded_temp [x][y] > 0:
                return True
            return False
        else:
            if self.dp.is_x_correct (self.matrix_excluded, x) and self.dp.is_x_correct (self.matrix_excluded, y) and self.matrix_excluded [x][y] == 1:
                return True
            return False

    def set_excluded (self, x, y):
        if self.dp.is_x_correct(self.matrix_excluded, x) and self.dp.is_y_correct(self.matrix_excluded, y):
            self.matrix_excluded [x][y] = 1

    def set_gas_candidate (self, x, y):
        if self.dp.is_x_correct(self.matrix_gas, x) and self.dp.is_y_correct(self.matrix_gas, y):
            self.matrix_gas [x][y] = GAS_CANDIDATE

    def set_gas_with_house (self, x, y, value):
        if self.dp.is_x_correct(self.matrix_gas, x) and self.dp.is_y_correct(self.matrix_gas, y):
            self.matrix_gas [x][y] = value

    def unset_gas (self, x, y):
        if self.dp.is_x_correct(self.matrix_gas, x) and self.dp.is_y_correct(self.matrix_gas, y):
            self.matrix_gas [x][y] = 0

    def set_house_with_gas (self, x, y, value):
        if self.dp.is_x_correct(self.matrix_house, x) and self.dp.is_y_correct(self.matrix_house, y):
            self.matrix_house [x][y] = value

    def cleanup_of_gas_candidates (self):
        for i in range(self.h):
            for j in range(self.w):
                if self.is_gas_candidate (i, j):
                    self.unset_gas (i, j)

    def get_all_not_excluded (self):
        results = []
        for i in range(self.h):
            for j in range(self.w):
                if not self.is_excluded (i, j, False):
                    results.append ((i,j))
        return results

    def is_solved (self):

        # check if wages match number of gas containers - horizontally
        for i in range(self.h):
            temp_sum = 0
            for j in range(self.w):
                if self.is_gas_any (i, j, False):
                    temp_sum += 1
            if temp_sum != self.wages[0][i]:
                return False

        # check if wages match number of gas containers - vertically
        for j in range(self.h):
            temp_sum = 0
            for i in range(self.w):
                if self.is_gas_any (i, j, False):
                    temp_sum += 1
            if temp_sum != self.wages[1][j]:
                return False

        # check if houses and gas containers do not overlap
        temp_sum_gas = 0
        temp_sum_houses = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.is_gas_any (i, j, False) and self.is_house (i, j, False):
                    return False
                if self.is_gas_any (i, j, False):
                    temp_sum_gas += 1
                if self.is_house (i, j, False):
                    temp_sum_houses += 1

        # number of houses must match number of gas containers
        if temp_sum_gas != temp_sum_houses:
            return False

        # check if gas container are not direct neighbours
        for i in range(self.h):
            for j in range(self.w):
                if self.is_gas_any (i, j, False):
                    temp_target_3 = numpy.zeros ((3, 3))
                    temp_target_3[1][1] = 1
                    temp_current_3 = self.dp.change_matrix_nonzero_to_value (self.dp.get_submatrix_3 (self.matrix_gas, i, j), 1)
                    if not self.dp.are_matrices_equal (temp_current_3, temp_target_3):
                        return False

        # TBD - number of houses with gas matches number of gas containers
    
        return True

    def get_number_of_houses (self, with_gas, use_temp):
        output_sum = 0
        for i in range(self.h):
            for j in range(self.w):
                if use_temp:
                    #print (self.matrix_house_temp)
                    if with_gas:
                        if self.matrix_house_temp [i][j] == 2:
                            output_sum += 1
                    else:
                        if self.matrix_house_temp [i][j] == 1:
                            output_sum += 1
                else:
                    if with_gas:
                        if self.matrix_house [i][j] == 2:
                            output_sum += 1
                    else:
                        if self.matrix_house [i][j] == 1:
                            output_sum += 1
        return output_sum

    # Returns True if method was able to update any location with gas
    # Otherwise returns False
    def update_gas_in_all_certain_places (self, use_temp):

        # Approach #1 - locate free places (by checking all fields one-by-one)
        # that has no other options - gas must be here
        for i in range(self.h):
            for j in range(self.w):
                c = 0
                x = 0
                y = 0
                value = 0
                if self.is_house (i, j, use_temp):
                    if self.dp.is_x_correct (self.matrix_gas, i-1) and self.is_empty (i-1, j, use_temp):
                        c += 1
                        x = i-1
                        y = j
                        value = GAS_HOUSE_EAST
                    if self.dp.is_x_correct (self.matrix_gas, i+1) and self.is_empty (i+1, j, use_temp):
                        c += 1
                        x = i+1
                        y = j
                        value = GAS_HOUSE_WEST
                    if self.dp.is_y_correct (self.matrix_gas, j-1) and self.is_empty (i, j-1, use_temp):
                        c += 1
                        x = i
                        y = j-1
                        value = GAS_HOUSE_NORTH
                    if self.dp.is_y_correct (self.matrix_gas, j+1) and self.is_empty (i, j+1, use_temp):
                        c += 1
                        x = i
                        y = j+1
                        value = GAS_HOUSE_SOUTH
                if c == 1 and not use_temp:
                    self.set_gas_with_house (x, y, value)
                    return True

        # Approach #2 - locate free places in lines (by checking both vertical and horizontal lines)
        # If there is one free place left and there is still one more gas to place, gas must in this location

        # horizontally
        for i in range(self.h):
            temp_sum_gas = 0
            temp_sum_not_excluded = 0
            x = 0
            y = 0
            for j in range(self.w):
                if self.is_gas_any (i, j, False):
                    temp_sum_gas += 1
                if not self.is_excluded (i, j, False):
                    temp_sum_not_excluded += 1
                    x = i
                    y = j

            if self.wages[0][i] - temp_sum_gas == 1 and temp_sum_not_excluded == 1:
                if self.dp.is_x_correct (self.matrix_house, x-1) and self.is_house_without_gas (x-1, y, False):
                    value = GAS_HOUSE_WEST
                elif self.dp.is_x_correct (self.matrix_house, x+1) and self.is_house_without_gas (x-1, y, False):
                    value = GAS_HOUSE_EAST
                elif self.dp.is_y_correct (self.matrix_house, y-1) and self.is_house_without_gas (x-1, y, False):
                    value = GAS_HOUSE_SOUTH
                elif self.dp.is_y_correct (self.matrix_house, y+1) and self.is_house_without_gas (x-1, y, False):
                    value = GAS_HOUSE_NORTH
                self.set_gas_with_house (x, y, value)
                return True

        # vertically
        for j in range(self.h):
            temp_sum_gas = 0
            temp_sum_not_excluded = 0
            x = 0
            y = 0
            for i in range(self.w):
                if self.is_gas_any (i, j, False):
                    temp_sum_gas += 1
                if not self.is_excluded (i, j, False):
                    temp_sum_not_excluded += 1
                    x = i
                    y = j

            if self.wages[1][j] - temp_sum_gas == 1 and temp_sum_not_excluded == 1:
                if self.dp.is_x_correct (self.matrix_house, x-1) and self.is_house_without_gas (x-1, y, False):
                    value = GAS_HOUSE_WEST
                elif self.dp.is_x_correct (self.matrix_house, x+1) and self.is_house_without_gas (x-1, y, False):
                    value = GAS_HOUSE_EAST
                elif self.dp.is_y_correct (self.matrix_house, y-1) and self.is_house_without_gas (x-1, y, False):
                    value = GAS_HOUSE_SOUTH
                elif self.dp.is_y_correct (self.matrix_house, y+1) and self.is_house_without_gas (x-1, y, False):
                    value = GAS_HOUSE_NORTH
                self.set_gas_with_house (x, y, value)
                return True

        return False

    def update_excluded (self):

        # case 1: exlude fields where is either house or gas
        for i in range(self.h):
            for j in range(self.w):
                if self.is_house(i, j, False):
                    self.set_excluded (i, j)
                if self.is_gas_any(i, j, False):
                    self.set_excluded (i, j)

        # case 2: if wages are 0 - horizontally and vertically
        for i in range(self.h):
            if self.wages[0][i] == 0:
                for j in range(self.w):
                    self.set_excluded (i, j)
        for j in range(self.w):
            if self.wages[1][j] == 0:
                for i in range(self.w):
                    self.set_excluded (i, j)

        # case 3: each gas container must have space around
        for i in range(self.h):
            for j in range(self.w):
                if self.is_gas_any (i, j, False):
                    if self.dp.is_x_correct (self.matrix_gas, i-1):
                        self.set_excluded (i-1, j)
                    if self.dp.is_x_correct (self.matrix_gas, i+1):
                        self.set_excluded (i+1, j)
                    if self.dp.is_y_correct (self.matrix_gas, j-1):
                        self.set_excluded (i, j-1)
                    if self.dp.is_y_correct (self.matrix_gas, j+1):
                        self.set_excluded (i, j+1)
                    if self.dp.is_x_correct (self.matrix_gas, i-1) and self.dp.is_y_correct (self.matrix_gas, j-1):
                        self.set_excluded (i-1, j-1)
                    if self.dp.is_x_correct (self.matrix_gas, i+1) and self.dp.is_y_correct (self.matrix_gas, j+1):
                        self.set_excluded (i+1, j+1)
                    if self.dp.is_x_correct (self.matrix_gas, i-1) and self.dp.is_y_correct (self.matrix_gas, j+1):
                        self.set_excluded (i-1, j+1)
                    if self.dp.is_x_correct (self.matrix_gas, i+1) and self.dp.is_y_correct (self.matrix_gas, j-1):
                        self.set_excluded (i+1, j-1)

        # case 4: exclude fields that are too far from houses
        for i in range(self.h):
            for j in range(self.w):
                if not self.is_excluded (i, j, False):
                    if self.dp.is_matrix_zeroed (self.dp.get_submatrix_3 (self.matrix_house, i, j)):
                        self.set_excluded (i, j)
                
        # case 5: exclude fields that are close to houses which are already connected to gas
        #         and there is no other option for gas available
        for i in range(self.h):
            for j in range(self.w):
                if not self.is_excluded (i, j, False):
                    sum_available_houses = 0
                    if self.dp.is_x_correct (self.matrix_house, i-1) and self.is_house (i-1, j, False) and not self.is_house_with_gas (i-1, j):
                        sum_available_houses += 1
                    if self.dp.is_x_correct (self.matrix_house, i+1) and self.is_house (i+1, j, False) and not self.is_house_with_gas (i+1, j):
                        sum_available_houses += 1
                    if self.dp.is_y_correct (self.matrix_house, j-1) and self.is_house (i, j-1, False) and not self.is_house_with_gas (i, j-1):
                        sum_available_houses += 1
                    if self.dp.is_y_correct (self.matrix_house, j+1) and self.is_house (i, j+1, False) and not self.is_house_with_gas (i, j+1):
                        sum_available_houses += 1
                    if sum_available_houses == 0:
                        self.set_excluded (i, j)

    def update_best_score (self):
        score = self.get_number_of_houses (True, True)
        # print (score)
        if score > self.score:
            self.matrix_excluded_temp = self.matrix_excluded
            self.matrix_gas_temp = self.matrix_gas
            self.matrix_house_temp = self.matrix_house
            self.score = score
            return True
        return False

    def solve (self):
        all_combinations_checked = False
        max_combinations = 20000000
        start_from_combination = 0
        
        self.update_excluded ()
        self.print (False)
        
        gas_updated = True
        while gas_updated:
            gas_updated = self.update_gas_in_all_certain_places (False)
            if self.verbose and gas_updated:
                print ("\n---> Found new place for gas 1 !!!\n")
                self.update_excluded ()
                self.print (False)

        self.print (False)
    
        solved = False

        empty_fields = self.get_all_not_excluded ()
        houses_to_be_fixed = self.get_number_of_houses (False, False)
            
        while not solved or not all_combinations_checked:

            combinations_to_check = self.dp.get_combinations (empty_fields, houses_to_be_fixed, max_combinations, start_from_combination)
            for combination in combinations_to_check:
                for field in combination:
                    (x, y) = field
                    self.set_gas_candidate (x, y)
            
                self.update_excluded ()
                gas_updated = True
                #while gas_updated:
                #    gas_updated = self.update_gas_in_all_certain_places (False)
                #    if self.verbose and gas_updated:
                #        print ("\n---> Found new place for gas !!!\n")
                #        self.print (False)
                solved = self.is_solved ()
                if solved:
                    if self.verbose:
                        print ("\n---> Found solution !!!\n")
                    break
                #else:
                    #score_improved = self.update_best_score ()
                    #if self.verbose and score_improved:
                    #    self.print (True)
                    #self.cleanup_of_gas_candidates()

            start_from_combination += max_combinations

            if not combinations_to_check:
                all_combinations_checked = True
                if not solved:
                    if self.verbose:
                        print ("\n--> Solution not found !!!\n")
                break

        self.print (False)
