N = int(input())
hights = list(map(int, input().split()))
maxSum = 2 * 10e5
aInd = 0
bInd = 0

for i in range(len(hights) - 1):
    a = sum(hights[:i + 1]) / len(hights[:i + 1])
    b = sum(hights[i + 1:]) / len(hights[i + 1:])

    deltaA = sum([i - a for i in hights[:i + 1] if i > a])
    deltaB = sum([i - b for i in hights[i + 1:] if i > b])

    if deltaA + deltaB < maxSum:
        maxSum = deltaB + deltaA
        aInd = len(hights[:i + 1])
        bInd = len(hights[i + 1:])

print(aInd, bInd)
