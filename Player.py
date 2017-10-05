class Player:

    Fname = ""
    Lname = ""
    Position = ""
    Nation = ""
    Age = ""
    MinsPlayed = 0
    Goals = 0
    Assists = 0

    def __init__(self, Fname, Lname, Position, Nation, DOB, MinsPlayed, Goals, Assists):

        self.Fname = Fname
        self.Lname = Lname
        self.Position = Position
        self.Nation = Nation
        self.MinsPlayed = MinsPlayed
        self.Goals = Goals
        self.Assists = Assists
        self.Age = 2017 - int(DOB[-4:])

    def __str__(self):
        return self.Fname + " " + self.Lname

    def minsPerGoal(self):

        if self.Goals != 0:
            return self.MinsPlayed / float(self.Goals)
        else:
            return 0.0

    def gamesPerGoal(self):
        if self.Goals != 0:
            return (self.MinsPlayed / float(self.Goals)) * 90.0
        else:
            return 0.0

    def goalsPerGame(self):

        if self.MinsPlayed != 0:
            return (self.Goals / float(self.MinsPlayed)) * 90.0
        else:
            return 0.0

    def goalsPerMin(self):

        if self.MinsPlayed != 0:
            return self.Goals / float(self.MinsPlayed)
        else:
            return 0.0

    def getFname(self):
        return self.Fname
    def setFname(self, fName):
        self.Fname = fName
    def getLname(self):
        return self.Lname
    def setLname(self, lName):
        self.Lname = lName
    def getPosition(self):
        return self.Position
    def setPosition(self, pos):
        self.Position = pos
    def getNation(self):
        return self.Nation
    def setNation(self, nat):
        self.Nation = nat
    def getAge(self):
        return self.Age
    def setAge(self, age):
        self.Age = age
    def getMinsPlayed(self):
        return self.MinsPlayed
    def setMinsPlayed(self, mp):
        self.MinsPlayed = mp
    def getGoals(self):
        return self.Goals
    def setGoals(self, g):
        self.Goals = g
    def getAssists(self):
        return self.Assists
    def setAssists(self, a):
        self.Assists = a