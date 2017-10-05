import sqlite3

def getLines(fil):
    li = []
    for line in fil:
        li.append(line[:-1])
    return li

def insertPlayers(li):
    conn = sqlite3.connect('Player.db')
    print "Database opened successfully";
    for item in li:
        elts = []
        elt = ""
        count = 1
        for c in item:
            if c == ',':                    #separate by comma
                elts.append(elt)
                elt = ""
            elif count == len(item):        #if end of item
                elt += c
                elts.append(elt)
            else:                           #build element char by char
                elt += c
            count += 1
        print elts
        statement = "INSERT INTO PLAYER (NUMB,FNAME,LNAME,POS,TEAM,NATION,DOB,WINJOINED,MINPLAYED,GOALS,ASSISTS) \
                      VALUES (" + elts[0] + ", " + elts[1] + ", " + elts[2] + "," + elts[3] + ", " + elts[4] + ", " \
                    + elts[5] + ", " + elts[6] + ", " + elts[7] + ", " + elts[8] + "," + elts[9] + ", " + elts[10] \
                    + ")";
        conn.execute(statement);
    conn.commit()
    print "Records created successfully";
    conn.close()

#fil = open("Chelsea.txt")
fil = open("ManCity.txt")
li = getLines(fil)
insertPlayers(li)
#insertPlayers(li)