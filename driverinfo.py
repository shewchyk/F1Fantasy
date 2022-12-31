#Name, car number
drivers = [["Verstappen", 1], ["Ricciardo", 3], ["Norris", 4], ["Vettle", 5], ["Latifi", 6], ["Gasly", 10], ["Perez", 11], ["Alonso", 14], ["Leclerc", 16], ["Stroll", 18], ["Magnussen", 20], ["Tsunoda", 22], ["Albon", 23], ["Zhou", 24], ["Ocon", 31],["Hamilton", 44], ["Schumacher", 47], ["Sainz", 55], ["Russell", 63], ["Bottas", 77]]

#2023 driver line-up changes, 100+ numbers denotes driver hasn't chosen race number
drivers_out = ["Ricciardo", 3], ["Vettle", 5], ["Latifi", 6], ["Schumacher", 47]
drivers_in = ["Piastri", 101], ["Hulkenberg", 27], ["de Vries", 102], ["Sargeant", 103]

#remove drivers (do - driver out) from 2023 lineup 
for do in drivers_out:
    while do in drivers:
        drivers.remove(do)

#add new drivers (di - driver in) to 2023 lineup
for di in drivers_in:
    drivers.append(di)

drivers_2023 = drivers
          
#Sprint weekend control
sprint_wk = input("Is it a sprint format weekend?: ")

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

#Sprint weekend function
def fp_sprint(driver_index, list):
    print("Enter FP finishing positions for", str(list[driver_index][0]))
    fp1 = [int(x) for x in input().split()]
    fp_point_by_session = list[driver_index].extend(fp1) 
    return fp_point_by_session

#p/s = index of driver list
if sprint_wk == "yes":
    s = 0
    while s < len(drivers_2023):
     fp_sprint(s, drivers_2023)
     s += 1
else:
     p = 0       
     while p < len(drivers_2023):
      fp_points(p, drivers_2023)
      p += 1

#constructors = [["Alfa Romeo"], ["Alpha Tauri"], ["Alpine"], ["Aston Martin"], ["Ferrari"], ["Haas"], ["McLaren"], ["Mercedes"], ["Red Bull"], ["Williams"]]