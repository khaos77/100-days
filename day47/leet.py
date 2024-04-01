dic = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in dic:
            return [dic[diff], i]
        dic[num] = i
    return
