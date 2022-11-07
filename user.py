class User:
    '''
    class to contain the data for each user. These fields are populated with data from the database when a user logs in
    '''
    def __init__(self, oid, username, email, fname, lname, achievements, analyses):
        self.__oid = oid
        self.__username = username
        self.__email = email
        self.__fname = fname
        self.__lname = lname
        self.__achievements = achievements
        self.__analyses = analyses

    # getter methods
    def getOid(self): return self.__oid
    def getUsername(self): return self.__username
    def getFirstName(self): return self.__fname
    def getLastName(self): return self.__lname
    def getAchievements(self): return self.__achievements
    def getAnalysis(self): return self.__analyses
    def getEmail(self): return self.__email

    # setter methods
    def giveAchievement(self, ach):
        self.__achievements.append(ach)
    def giveAnalysis(self, ach):
        self.__analyses.append(ach)