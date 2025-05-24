Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
nums = [25, 12, 36, 95, 14]
nums
[25, 12, 36, 95, 14]
nums[0]
25
nums[4]
14
nums[2:]
[36, 95, 14]
nums[-1]
14
nums[-5]
25
names = ["Emmanuel", "Oiza", "Chuks"]
names
['Emmanuel', 'Oiza', 'Chuks']
>>> values = [9.5, "Emmanuel", 25]
>>> values
[9.5, 'Emmanuel', 25]
>>> mil = [nums, names]
>>> mil
[[25, 12, 36, 95, 14], ['Emmanuel', 'Oiza', 'Chuks']]
>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45]
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45]
>>> nums.pop()
45
>>> 
>>> nums
[25, 77, 36, 95]
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29, 12, 14, 36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
