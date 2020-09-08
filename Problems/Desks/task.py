# put your python code here
import math

group_1 = int(input())
group_2 = int(input())
group_3 = int(input())

group_1_result = math.ceil(group_1 / 2)
group_2_result = math.ceil(group_2 / 2)
group_3_result = math.ceil(group_3 / 2)

print(group_1_result + group_2_result + group_3_result)
