class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])
        
        for i in range(n):
            empty = m - 1
            for j in range(m - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty] = '#'
                    empty -= 1

        res = [[0] * n for _ in range(m)]
        for r in range(n):
            for c in range(m):
                res[c][n - 1 - r] = boxGrid[r][c]
        
        return res       
        
        
        
    
    
    