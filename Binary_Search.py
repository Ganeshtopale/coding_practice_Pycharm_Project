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

lst = [2,4,5,4,27,39,3333,567,45,67,56,89,99,60]
n = 567
if Binary_Search(lst, n):
    print("found",pos+1)
else:
    print("not found")