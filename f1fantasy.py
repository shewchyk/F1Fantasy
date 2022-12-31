# Phase 1 - Program will determine recommended fantasy moves based on a point system from a total of FP performance for standard weekends
# Phase 2 - Include update to account for sprint weekends
# Phase 3 - errors for entering duplicate and non-existant finishing positions

from driverinfo import drivers_2023, sprint_wk

drivers_2023 

def dr_fp1(drivers, index):
    return [i[index] for i in drivers]  
      
if sprint_wk != "yes":
    points_fp1 = dr_fp1(drivers_2023, 2)
    points_fp2 = dr_fp1(drivers_2023, 3)
    points_fp3 = dr_fp1(drivers_2023, 4)
    sumindex = [sum(fp_total) for fp_total in zip(points_fp1, points_fp2, points_fp3)]
else: 
    points_fp1 = dr_fp1(drivers_2023, 2)
    sumindex = points_fp1

drivers_names = dr_fp1(drivers_2023, 0)

for d, s in zip(drivers_names, sumindex):
    print("Driver/points:", s, d)