class Solution:

    def encode(self, strs: List[str]) -> str:
        #neet|code|love|
        
    #     combinedWord = ''
    #     wordlength = []
    #     i = 0
    #     while i < len(strs):
    #         if not i == len(strs)-1:
    #             combinedWord += strs[i] + '|'
    #             print (i)
    #         else:
    #             combinedWord += strs[i]
    #         i+=1

    #     print (combinedWord)
    #     return combinedWord

    # def decode(self, s: str) -> List[str]:
    #     finalList = []
    #     if len(s) > 0:
    #         finalList = s.split("|")      
    #     return finalList
    
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
