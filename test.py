array = [10,7,8,2]
k = 12
array_sorted = sorted(array)
start_r = 0
end_r = len(array_sorted)
start_c = 0
end_c = len(array_sorted)
import random as rd
for r in range(end_r):
    r_index = rd.randint(start_r,end_r)
    if array_sorted(r_index) > k:
        end_r = r_index
    else:
        start_r = r_index
    c_target = k - array_sorted
    for c in range(end_c):
        c_index = rd.randint(start_c,end_c)
        if array_sorted(c_index) > k - array_sorted(r_index)
