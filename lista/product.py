def prod(lst):
    # Write code here
    res = 1
    for i in range(0, len(lst)):
        res *= lst[i]
        print(res)
    

lst = [1, 2, 3]
prod(lst)