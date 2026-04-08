def combine_and_filter(lst, threshold):
    # Write code here
    result = []
    lst.sort()
    for i in lst.copy():  # iterate over a copy to avoid modifying list while looping
        if i <= threshold:
            lst.remove(i)  # remove the element, not pop by index
        else:
            result.append(i)
    return result

    #*otra manera:
    # def combine_and_filter(lst, threshold):
    # filtered = []
    # for i in range(0, len(lst)):
    #     if lst[i] > threshold:
    #         filtered.append(lst[i])
    # filtered.sort()
    # return filtered

lst = [1, 5, 3, 8, 2, 7, 4, 6]
threshold = 4
print(combine_and_filter(lst, threshold))
