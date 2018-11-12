#
# nums = [[1,2,3],[4,5,6],[7,8,9]]
# k=0
# for i in range(len(nums)):
#     for j in range(k,len(nums[i])):
#         if not(i == j):
#             nums[i][j],nums[j][i] = nums[j][i],nums[i][j]
#     k += 1
# print(nums)

# nums = [[1,2,3],[4,5,6]]
# nums_end= []
# for i in enumerate(range(3)):
#    nums_end.append(list(i))
# flag = 0
# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         nums_end[j][flag] = nums[i][j]
#     flag +=1
# print(nums_end)


nums = [[1,2,3],[4,5,6]]
nums_end = [[0 for row in range(len(nums))]for col in range(len(nums[0]))]
print(nums_end)

for i in range(len(nums_end)):
    for j in range(len(nums)):
        nums_end[i][j] = nums[j][i]

print(nums_end)
