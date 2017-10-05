import sqlite3
from Player import Player

conn = sqlite3.connect('Player.db')
print "Opened database successfully";

cursor = conn.execute("SELECT * from PLAYER WHERE TEAM = 'ManCity'")
print "Operation done successfully\n"

players = []
for row in cursor:
    #playa = Player(row[1], row[2], row[3], row[5], row[6], row[8], row[9], row[10])
    #players.append(playa)
    print "Number " + str(row[0]) + ": " + row[1] + " " + row[2]
#for p in players:
    #goalsPerGame = "{0:.2f}".format(p.goalsPerGame())
    #minsPerGoal = "{0:.2f}".format(p.minsPerGoal())
    #print "Player: " + str(p)
    #print "Goals per game: " +str(goalsPerGame)
    #print "Minutes per goal: " + str(minsPerGoal) + "\n"
conn.close()