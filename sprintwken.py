#
#Note there are no reserve drviers on sprint weekends in FP1 (the only FP session that counts on sprint weekends in this program)
from driverinfo import drivers_2023
from functions import dr_fpr, sprint_wk

#Sprint weekend function
def fp_sprint(driver_index, list):
    print("Enter FP finishing positions for", str(list[driver_index][0]))
    fp1 = [int(x) for x in input().split()]
    fp_point_by_session = list[driver_index].extend(fp1) 
    return fp_point_by_session

#s = index of driver list
if sprint_wk == "yes":
    s = 0
    while s < len(drivers_2023):
     fp_sprint(s, drivers_2023)
     s += 1

if sprint_wk == "yes": 
    points_fp1 = dr_fpr(drivers_2023, 2)
    sumindex_sw = points_fp1
