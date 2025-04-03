n = int(input())
numbers = input().split()
if n == 1:
    print(max(numbers))
else:
    pairs = [numbers[i:i+2] for i in range(0, len(numbers), 2)]
    total_sum = 0
    max_nums = []
    for pair in pairs:
        max_num = max(int(pair[0]), int(pair[1]))
        max_nums.append(max_num)
        total_sum += max_num
    
    print(f"{' + '.join(str(num) for num in max_nums)} = {total_sum}")