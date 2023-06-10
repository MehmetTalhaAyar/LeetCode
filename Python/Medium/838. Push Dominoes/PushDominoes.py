class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)


        forces = [0] * n
        result = ""

        force = 0
        for i in range(n):
            if dominoes[i] == "R":
                force = n
                forces[i] += force
            elif dominoes[i] == "L":
                force = 0
            else:
                if force > 0:
                    forces[i] += force
                    force -= 1  

        force = 0
        for i in range(n-1,-1,-1):
            if dominoes[i] == "L":
                force = -n
                forces[i] += force
            elif dominoes[i] == "R":
                force = 0
            else:
                if force < 0:
                    forces[i] += force
                    force += 1  

        
        for i in forces:
            if i < 0:
                result += "L"
            elif i > 0:
                result += "R"
            else:
                result += "."

        return result



        



sol = Solution()


print(sol.pushDominoes(".L.R...LR..L.."))

