class Solution(object):
    def distinctIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """

        board = []
        board.append(n)
        x = 0
        while True:
         
            for i in range(2,board[x]):
                if board[x] % i == 1 and i not in board:
                    board = self.addData(board, i)
                    x = -1                
            
            x += 1
            
            if x == len(board):
                break


            

        return len(board)


    def addData(self,board,value):

        myList = []
        myList = board
        
        for i in range(len(myList)):
            if value > myList[i]:
                continue
            else:
                myList.insert(i,value)
                break
        return myList
        









sol = Solution()

print(sol.distinctIntegers(4))