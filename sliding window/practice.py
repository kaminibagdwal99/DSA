def best_time_to_buy_and_Sell(prices):
    buy_price = prices[0]
    profit = 0

    for i in prices[1:]:
        if i<buy_price:
            buy_price=i
        else:
            profit = max(profit, i-buy_price)
    return profit

def lengthOfLongestSubstring(s):
    l=0
    visit = set()
    res=0
    for r in range(len(s)):
        if s[r] in visit:
            visit.remove(s[l])
            l=l+1
        visit.add(s[r])
        res= max(res, r-l+1)
    return res

s = "abcabcbb"
n =lengthOfLongestSubstring(s)
print(n)