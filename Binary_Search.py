pos = -1
def Binary_Search (lst,n):
    L = 0
    U = len(lst)-1
    while L <= U:
        mid = (L+U) // 2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                L = mid
            else:
                U = mid

lst = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
n = 14
if Binary_Search(lst, n):
    print("found",pos+1)
else:
    print("not found")
