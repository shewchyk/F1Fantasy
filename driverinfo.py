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
          
#constructors = [["Alfa Romeo"], ["Alpha Tauri"], ["Alpine"], ["Aston Martin"], ["Ferrari"], ["Haas"], ["McLaren"], ["Mercedes"], ["Red Bull"], ["Williams"]]