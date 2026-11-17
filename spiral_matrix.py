class Solution:
    def spiralOrder(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])

        visited=set()
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        r,c=0,0
        direction=0

        result=[]
        for i in range(rows*cols):
            result.append(matrix[r][c])
            visited.add((r,c))

            nr=r+dir[direction][0]
            nc=c+dir[direction][1]

            if(nr<0 or nr>=rows or nr<0 or nc>=cols or (nr,nc)in visited):
                direction=(direction +1)%4
                nr=r+dir[direction]
                nc=c+dir[direction][1]

                r,c=nr,nc
    return result

#optimised solution
def solve(self, matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse right across the top row
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # Traverse down the rightmost column
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # Traverse left across the bottom row
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        # Traverse up the leftmost column
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result
