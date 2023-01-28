import time


def two_sum(nums: list[int], target: int) -> list[int]:
    output = []
    for i in nums:
        idx = [x[0] for x in enumerate(nums) if x[1] == i]
        if len(idx) >= 2:
            if nums[idx[0]] + nums[idx[1]] == target:
                output = idx

        for j in nums:
            if nums.index(i) != nums.index(j):
                if i + j == target:
                    output.append(nums.index(i))
                    output.append(nums.index(j))
    return output[:2]


start_time = time.time()
print(two_sum([1,5,7,3,6,5,1,3,4,5], 9))
print("--- %s seconds ---" % (time.time() - start_time))
