def count_nest_trees(heights):
    count = 0
    n = len(heights)
    nest_trees = []

    if not (heights[0] < heights[1]):
        count += 1
        nest_trees.append(0)

    for i in range(1, n-1):
        if not (heights[i] < heights[i-1] or heights[i] < heights[i+1]):
            count += 1
            nest_trees.append(i)

    if not (heights[n-1] < heights[n-2]):
        count += 1
        nest_trees.append(n-1)

    return count, nest_trees

n = int(input())
heights = list(map(int, input().split()))

result, nest_trees = count_nest_trees(heights)
print(result)