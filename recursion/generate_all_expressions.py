def generate_all_expressions(s, target):
    res = []
    dfs(res, s, '', 0, 0, target)
    return res
    
def dfs(res, remains, curr_str, curr, prev, target):
    if not remains:
        if curr == target:
            res.append(curr_str)
        return

    for i in range(1, len(remains)+1):
        #val = remains[:i]
        if len(curr_str) == 0:
            if not (i > 1 and remains[0]==0):
                dfs(res, remains[i:], remains[:i], int(remains[:i]), int(remains[:i]), target)
        else:
            if not (i>1 and remains[0]==0):
                dfs(res, remains[i:], curr_str+ '+' + remains[:i], curr + int(remains[:i]), int(remains[:i]), target)
                dfs(res, remains[i:], curr_str+ '*' + remains[:i], curr - prev + prev*int(remains[:i]), prev*int(remains[:i]), target)

s = "222"
target = 24

print generate_all_expressions(s, target)
