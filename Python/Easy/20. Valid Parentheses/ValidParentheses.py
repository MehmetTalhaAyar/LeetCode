class Solution(object):
    def isValid(self, s):
        heap = 0
        pointer = 0
        if len(s) % 2 == 1:
            return False

        while True:
            heap = len(s)
            for y in range(len(s)):
                if s[y] == "(" or s[y] == "{" or s[y] == "[":     
                    pointer = y

            if s[pointer] == "(":
                for i in range(pointer+1,len(s)):
                    if s[i] == ")":
                        if len(s[pointer+1:i]) %2 == 1:
                            return False
                        s = s[0:pointer]+ s[pointer+1:i] +s[i+1:]                        
                        break
                    
            elif s[pointer] == "[":
                for i in range(pointer+1,len(s)):
                    if s[i] == "]":
                        if len(s[pointer+1:i]) %2 == 1:
                            return False
                        s = s[0:pointer]+ s[pointer+1:i] +s[i+1:]
                        break     
            elif s[pointer] == "{":
                for i in range(pointer+1,len(s)):
                    if s[i] == "}":
                        if len(s[pointer+1:i]) %2 == 1:
                            return False
                        s = s[0:pointer]+ s[pointer+1:i] +s[i+1:]
                        break


        
            if len(s) == 0:
                return True
            elif heap == len(s):
                return False
        
        
     
     











