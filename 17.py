class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        outputs = []
        mapping = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if digits == "": return []
        def pick(i,choices):
            nonlocal outputs
            if i == len(digits):
                outputs.append(str(chocies))
            for c in mapping[digits[i]]:
                choices.append(c)
                pick(i+1,choices)
                choices.remove(c)
        return outputs
