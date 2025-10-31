def findKPerm(nums, k):
    res=[]
    used=[False]*len(nums)

    def helper(path):
        if len(path)==k:
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i]=True
                path.append(nums[i])
                helper(path)
                path.pop()
                used[i]=False

    helper([])
    return res
