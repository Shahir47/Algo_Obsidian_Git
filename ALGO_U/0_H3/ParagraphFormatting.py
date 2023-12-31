def ParaFormat(ip, k, start, curr):
    if start>len(ip)-1:
        return 0 if curr == 0 else (k - curr)**3

    sum = 0

    if curr+ip[start]+1 > k:
        if start < mx:
            sum = ParaFormat(ip, k, start+1, ip[start])
        return sum + (k-curr)**3

    if curr == 0:
        sum = min((k-ip[start])**3 + ParaFormat(ip, k, start+1, 0), ParaFormat(ip, k, start+1, ip[start]))
        return sum
    
    else:
        sum = min(ParaFormat(ip, k, start+1, curr+ip[start]+1), (k-curr)**3+ParaFormat(ip, k, start+1, ip[start]))
        return sum
        

def max_last(ip, k):
    sum_ = ip[len(ip)-1]
    for i in range(len(ip)-2, -1, -1):
        sum_ += ip[i] + 1
        if(sum_ > k):
            break
    return i+1

ip = [3, 3, 2, 2, 2, 11] #abc def gh ij kl mnopqrstuvw
k = 13
mx = max_last(ip.copy(), k)
print(ParaFormat(ip, k, 0, 0))

ip = [3,2,4,7] #abc def gh ij kl mnopqrstuvw
k = 10
mx = max_last(ip.copy(), k)
print(ParaFormat(ip, k, 0, 0))

ip = [3,2,2] #abc def gh ij kl mnopqrstuvw
k = 6
mx = max_last(ip.copy(), k)
print(ParaFormat(ip, k, 0, 0))

ip = [3,2,2, 3, 3] #abc def gh ij kl mnopqrstuvw
k = 11
mx = max_last(ip.copy(), k)
print(ParaFormat(ip, k, 0, 0))



    # if start>end:
    #     return (k - curr)**3
    # sum = 0
    # if curr == 0:
    #     sum = ParaFormat(ip, k, start+1, end, ip[start])
    #     return sum

    # if (curr+ip[start]+1) <= k:
    #     sum = ParaFormat(ip, k, start+1, end, curr+ip[start]+1)
    #     return sum
    # else:
    #     sum = ParaFormat(ip, k, start+1, end, ip[start])
    #     return sum + (k-curr)**3