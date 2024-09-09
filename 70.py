#https://leetcode.com/problems/climbing-stairs/

# naive recursive sol
def climbstairs(n):
    if n <= 1:
        return n
    return climbstairs(n-2) + climbstairs(n-1)

print(climbstairs(9 + 1))


