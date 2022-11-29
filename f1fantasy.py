# Phase 1 - Program will determine recommended fantasy moves based on a point system from a total of FP performance for standard weekends
# Phase 2 - Include update to account for sprint weekends
# Phase 3 - errors for entering duplicate and non-existant finishing positions

from driverinfo import drivers

drivers 
def dr_fp1(drivers, x):
    return [i[x] for i in drivers]

#checks to see if there was a reserve driver in any of the FP sessions (0 value denotes reserve driver)
def reserve(session_1, x, session_2, session_3):
     if session_1[x] == 0:
        session_1[x] = int(round((session_2[x] + session_3[x]) / 2, 0))

     if session_2[x] == 0:
        session_2[x] = int(round((session_1[x] + session_3[x]) / 2, 0))
        
     if session_3[x] == 0:
        session_3[x] = int(round((session_1[x] + session_2[x]) / 2, 0))
    
# convert func to int
drivers_names = [i for i in dr_fp1(drivers, 0)]
points_fp1 = [int(i) for i in dr_fp1(drivers, 2)]
points_fp2 = [int(i) for i in dr_fp1(drivers, 3)]
points_fp3 = [int(i) for i in dr_fp1(drivers, 4)]

y = 0
while y < len(points_fp1):
    reserve(points_fp1, y, points_fp2, points_fp3)
    y += 1

sumindex = [sum(elts) for elts in zip(points_fp1, points_fp2, points_fp3)]

for d, s in zip(drivers_names, sumindex):
    print("Driver/points:", s, d)