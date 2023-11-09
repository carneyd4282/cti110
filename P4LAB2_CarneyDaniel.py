# CTI 110
# P4LAB2 - Output Range with an Increment of 5
# Daniel Carney
# 2023-11-02

start = int(input())
end = int(input())
if start <= end:
    for x in range(start, end + 1, 5):
        print(x, end=' ')
    print('')
else:
    print("Second integer can't be less than the first.")