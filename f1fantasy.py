# Phase 1 - Program will determine recommended fantasy moves based on a point system from a total of FP performance for standard weekends
# Phase 2 - Include update to account for sprint weekends
# Phase 3 - account for reserve drivers

from driverinfo import drivers_2023
from functions import dr_fpr, sprint_wk
if sprint_wk != "yes":
    from regwken import sumindex_rw 
    sumindex = sumindex_rw
else: 
    from sprintwken import sumindex_sw
    sumindex = sumindex_sw

#Final result
drivers_names = dr_fpr(drivers_2023, 0)

for d, s in zip(drivers_names, sumindex):
    print("Driver/points:", s, d)