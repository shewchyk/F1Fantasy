# Phase 1 - Program will determine recommended fantasy moves based on a point system from a total of FP performance for standard weekends
# Phase 2 - Include update to account for sprint weekends
# Phase 3 - error~s for entering duplicate and non-existant finishing positions

from driverinfo import drivers, sprint_wk

drivers      

def dr_fp1(drivers, index):
    return [i[index] for i in drivers]
    
#checks to see if there was a reserve driver in any of the FP sessions (0 value in "drivers" denotes reserve driver)
#don't call on Sprint weekends
def reserve(list, driver_index, fp_index):
    avg = int(round((list[driver_index][2] + list[driver_index][3] + list[driver_index][4]) / 3, 0))
    i = 0
    while i < len(list):
        for driver_index in list:
            if driver_index[2] == 0:
                driver_index[2] = avg
            if driver_index[3] == 0:
                driver_index[3] = avg
            if driver_index[4] == 0:
                driver_index[4] = avg
            else: pass
        i += 1

if sprint_wk != "yes":
    reserve(drivers, 0, 2)
    points_fp1 = dr_fp1(drivers, 2)
    points_fp2 = dr_fp1(drivers, 3)
    points_fp3 = dr_fp1(drivers, 4)
    sumindex = [sum(fp_total) for fp_total in zip(points_fp1, points_fp2, points_fp3)]
else: 
    points_fp1 = dr_fp1(drivers, 2)
    sumindex = points_fp1

drivers_names = dr_fp1(drivers, 0)

for d, s in zip(drivers_names, sumindex):
    print("Driver/points:", s, d)