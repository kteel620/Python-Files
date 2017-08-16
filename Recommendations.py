Lion_King = {"Name": "Lion King", "Year": 1997, "IMDB Rating": 9.6}
The_Dark_Knight = {"Name": "The Dark Knight", "Year": 2008, "IMDB Rating": 9.5}
Whiplash = {"Name":"Whiplash", "Year": 2015, "IMDB Rating": 9.0}
SawXX = {"Name":"Saw XX", "Year":2032, "IMDB Rating":4.2 }

Movies = [Lion_King, Whiplash, The_Dark_Knight, SawXX]

for title in Movies:
    if (title["IMDB Rating"] >= 5.0):
        print("You should watch " + title["Name"])