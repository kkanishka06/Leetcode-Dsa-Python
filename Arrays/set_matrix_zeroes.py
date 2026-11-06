#brute force
class Solution:
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Find original zeroes
        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] == 0:

                    # Step 2: Mark entire row
                    for k in range(cols):
                        if matrix[i][k] != 0:
                            matrix[i][k] = -1

                    # Step 3: Mark entire column
                    for k in range(rows):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -1

        # Step 4: Convert -1 into 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

#brute force
class Solution:
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        row = [0] * rows
        col = [0] * cols

        # Step 1: Identify zeroes
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # Step 2: Set elements to zero
        for i in range(rows):
            for j in range(cols):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

#optimal solution with o(1) space
class Solution:
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        first_row = False
        first_col = False

        # Step 1: Check first row
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row = True

        # Step 2: Check first column
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col = True

        # Step 3: Mark zeroes using first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: Set inner matrix zeroes
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 5: Set first row to zero
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 6: Set first column to zero
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0