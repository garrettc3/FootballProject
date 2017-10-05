import sqlite3

conn = sqlite3.connect('Player.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE PLAYER 
            (   NUMB        INT                  NOT NULL,
                FNAME       CHAR(40)            NOT NULL,
                LNAME       CHAR(40)            NOT NULL,
                POS         CHAR(3)             NOT NULL,
                TEAM        CHAR(20)            NOT NULL,
                NATION      CHAR(20)            NOT NULL,
                DOB         CHAR(10)            NOT NULL,
                WINJOINED   CHAR(3)             NOT NULL,
                MINPLAYED   INT                 NOT NULL,
                GOALS       INT                 NOT NULL,
                ASSISTS     INT                 NOT NULL,
                PRIMARY KEY (NUMB, TEAM) ); ''')
print "Table created successfully";

conn.close();