#Fuction to loop through various lists (finishing positions, names)
def dr_fpr(drivers, index):
    return [i[index] for i in drivers]  

#Sprint weekend control
sprint_wk = input("Is it a sprint format weekend?: ")