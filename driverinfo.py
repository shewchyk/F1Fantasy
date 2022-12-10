#Name, car number
drivers = [["Verstappen", 1], ["Ricciardo", 3],["Norris", 4], ["Vettle", 5], ["Latifi", 6], ["Gasly", 10], ["Perez", 11], ["Alonso", 14], ["Leclerc", 16], ["Stroll", 18], ["Magnussen", 20], ["Tsunoda", 22], ["Albon", 23], ["Zhou", 24], ["Ocon", 31],["Hamilton", 44], ["Schumacher", 47], ["Sainz", 55], ["Russell", 63], ["Bottas", 77]]

sprint_wk = input("Is it a sprint format weekend?: ")

#input FP finishing positions, extend to drivers' list
def fp_points(driver_index, list):
    print("Enter FP finishing positions for", str(list[driver_index][0]))
    fp1, fp2, fp3 = [int(x) for x in input().split()]
    fp_point_by_session = list[driver_index].extend([fp1, fp2, fp3])
    return fp_point_by_session

#Sprint weekend function
def fp_sprint(driver_index, list):
    print("Enter FP finishing positions for", str(list[driver_index][0]))
    fp1 = [int(x) for x in input().split()]
    fp_point_by_session = list[driver_index].extend([fp1]) 
    return fp_point_by_session

#p/s = index of driver list

if sprint_wk == "yes":
    s = 0
    while s < len(drivers):
     fp_sprint(s, drivers)
     s += 1
else:
     p = 0       
     while p < len(drivers):
      fp_points(p, drivers)
      p += 1

#constructors = [["Alfa Romeo"], ["Alpha Tauri"], ["Alpine"], ["Aston Martin"], ["Ferrari"], ["Haas"], ["McLaren"], ["Mercedes"], ["Red Bull"], ["Williams"]]