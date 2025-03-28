from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        def start(m, n, board, used, word):
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        used[i][j] = True
                        if dfs(i, j, board, word, used, 1):
                            return True
                        used[i][j] = False
            return False

        def dfs(x, y, board, word, used, depth):
            if depth == len(word):
                return True
            
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and not used[nx][ny]:
                    if board[nx][ny] == word[depth]:
                        used[nx][ny] = True
                        if dfs(nx, ny, board, word, used, depth+1):
                            return True
                        used[nx][ny] = False
            return False

        m = len(board)
        n = len(board[0])
        used = [[False]*n for _ in range(m)]
        return start(m, n, board, used, word)

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABC"
    solution = Solution()
    res = solution.exist(board, word)
    print(res)
