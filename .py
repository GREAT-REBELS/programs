---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
arr = list(map(int, input().split()))
K = int(input())

left, right = 0, K
minInd1, minInd2 = 0, K
maxInd1, maxInd2 = 0, K
subArr_sum = sum(arr[:K])
min_sum, max_sum = subArr_sum, subArr_sum

while right < N:
    subArr_sum += arr[right] - arr[left]
    left += 1
    right += 1
    if subArr_sum > max_sum:
        max_sum = subArr_sum
        maxInd1 = left
        maxInd2 = right

    if subArr_sum < min_sum:
        min_sum = subArr_sum
        minInd1 = left
        minInd2 = right

print(*arr[minInd1:minInd2])
print(*arr[maxInd1:maxInd2])
