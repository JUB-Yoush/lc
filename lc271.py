def encode(strs)-> str:
    # write your code here
    output:str = ""
    for s in strs:
        output += str(len(s)) + "#" + s
    return output
    

    

def decode(str):
    # write your code here
  
    output:list = []
    while len(str) != 0:
        strLen = int(str[0])
        str = str[2:]
        output.append(str[0:strLen])
        str = str[strLen:]
        
     
        
    return output
        
    

print(decode(encode(["lint","code","love","you"])))