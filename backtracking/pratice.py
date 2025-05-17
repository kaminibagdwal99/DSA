def partition(s):
    res =[]
    def palindrom(s):
        return s==s[::-1]
    def helper(ind,ds):
        if ind ==len(s):
            res.append(ds.copy())
        for i in range(ind, len(s)):
            if palindrom(s[ind:i+1]):
                helper(i+1,ds +[s[ind:i+1]])
    helper(0, [])
    return res
            
print(partition(s = "aab"))