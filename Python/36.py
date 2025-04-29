class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in d.keys():
                        d[board[i][j]] = 1
                    else:
                        return False
        for i in range(9):
            d = {}
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] not in d.keys():
                        d[board[j][i]] = 1
                    else:
                        return False
        d = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                k = i // 3
                k2 = j // 3
                k3 = 3 * k + k2
                if board[i][j] != '.':
                    if board[i][j] not in d[k3].keys():
                        d[k3][board[i][j]] = 1
                    else:
                        return False
        return True