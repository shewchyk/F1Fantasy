from driverinfo import drivers_2023
from functions import dr_fpr, sprint_wk
#input FP finishing positions, extend to drivers' list
def fp_points(driver_index, list):
    print("Enter FP finishing positions for", str(list[driver_index][0]))
    fp1, fp2, fp3 = [int(x) for x in input().split()]
    #below is the reserve driver control, a 0 input in any FP session denotes a reserve driver served for the regular driver in that session
    avg = int(round((fp1 + fp2 + fp3) / 2, 0))
    if fp1 == 0:
        fp1 = avg
    if fp2 == 0:
        fp2 = avg
    if fp3 == 0:
        fp3 = avg
    fp_point_by_session = list[driver_index].extend((fp1, fp2, fp3))
    return fp_point_by_session

#p = index of driver list
if sprint_wk != "yes":
     p = 0       
     while p < len(drivers_2023):
      fp_points(p, drivers_2023)
      p += 1

if sprint_wk != "yes":
    points_fp1 = dr_fpr(drivers_2023, 2)
    points_fp2 = dr_fpr(drivers_2023, 3)
    points_fp3 = dr_fpr(drivers_2023, 4)
    sumindex_rw = [sum(fp_total) for fp_total in zip(points_fp1, points_fp2, points_fp3)]