def is_num(z):
    try:
        int(z)
        return True
    except ValueError:
        return False


x = [1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
nums = []
for i in x:
    if is_num(i):
        nums.append(int(i))
print(sum(nums))
