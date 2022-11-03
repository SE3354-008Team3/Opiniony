class User:
    '''
    class to contain the data for each user
    '''
    def __init__(self, oid, username, email, fname, lname, friends, achievements, analyses):
        self.__oid = oid
        self.__username = username
        self.__email = email
        self.__fname = fname
        self.__lname = lname
        self.__friends = friends
        self.__achievements = achievements
        self.__analyses = analyses

    # getter methods
    def getOid(self): return self.__oid
    def getUsername(self): return self.__username
    def getFirstName(self): return self.__fname
    def getLastName(self): return self.__lname
    def getAchievements(self): return self.__achievements
    def getFriends(self): return self.__friends

    # setter methods
    def giveAchievement(self, ach):
        self.__achievements.append(ach)
    def giveAnalysis(self, ach):
        self.__analyses.append(ach)