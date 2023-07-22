#remaining 2023 races
#!!!future race URLs are estimated!!! URLs are not published until after the session
#Name of country race where the race is being held in all lowercase letters
#For USA and Italy races use city name
race_name = input("What race is it?: ")
if race_name == "austria" or race_name == "belgium" or race_name == "quatar" or race_name == "austin" or race_name == "brazil":
        print(race_name, "is a sprint weekend, only FP1 is valid for fantasy scoring.")
else: 
        print(race_name, "is a regular weekend and all FP sessions are valid for fantasy scoring.")

spain = ["https://www.formula1.com/en/results.html/2023/races/1211/spain/practice-1.html", "https://www.formula1.com/en/results.html/2023/races/1211/spain/practice-2.html", "https://www.formula1.com/en/results.html/2023/races/1211/spain/practice-3.html"]
canada = ["https://www.formula1.com/en/results.html/2023/races/1212/canada/practice-1.html", "https://www.formula1.com/en/results.html/2023/races/1212/canada/practice-2.html", "https://www.formula1.com/en/results.html/2023/races/1212/canada/practice-3.html"]
austria = ["https://www.formula1.com/en/results.html/2023/races/1213/austria/practice-1.html"]
greatbritain =["https://www.formula1.com/en/results.html/2023/races/1214/great-britain/practice-1.html", "https://www.formula1.com/en/results.html/2023/races/1214/great-britain/practice-2.html", "https://www.formula1.com/en/results.html/2023/races/1214/great-britain/practice-3.html"]
hungary = ["https://www.formula1.com/en/results.html/2023/races/1215/hungary/practice-1.html", "https://www.formula1.com/en/results.html/2023/races/1215/hungary/practice-2.html", "https://www.formula1.com/en/results.html/2023/races/1215/hungary/practice-3.html"]

#def race(race_name):
match race_name:
    case "spain":
        race_name = spain
    case "canada":
        race_name = canada    
    case "austria":
        race_name = austria
    case "greatbritain":
        race_name = greatbritain
    case "hungary":
        race_name = hungary


