import random
#allow user to input number of rounds and
#questions for a quizzo game and this will generate categories of questions


questions = input("How Many Questions Would you Like Generated? ")
questionNum = int(questions)
categoryList = ["Hockey", "Olympics", "WorldCup", "Basketball", "Baseball", "Football", "Other Sport",
                               "US History", "Wars", "Presidents", "World History", "Capitals", "Locations", "Bodies of Water", "Landmarks",
                                "Mountains", "Deserts", "Chemistry", "Biology", "Astronomy", "Nature", "Weather", "Math", "Measurement",
                                "Medicine", "Technology" "Pop Culture News",  "Pop Culture Movies", "Pop Culture Birthdays"," Pop Culture Holidays",
                                "Pop Culture TV", "Pop Culture Music", "Music", "Movies", "TV", "Literature", "FineArt", "Mythology", "Language",
                                "Cars", "Games", "Companies", "Food", "Drink"]
gameList =  random.choices(categoryList, k = questionNum)
print("Here are your categories", gameList)

