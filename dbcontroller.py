import pymongo, certifi

from config import Config
from user import User

class DBController:
    '''
    class to interact with the mongoDB databases
    '''
    def __init__(self):
        uri = "mongodb+srv://admin:gJp1hbBR0wtAJY0u@cluster0.sd2zwqa.mongodb.net/?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
        db = self.client['project_database']
        self.usersCollection = db['users']
        self.achievementsCollection = db['achievements']
        self.analysisCollection = db['analysis']
    
    def createUser(self, username, password, email, fname=None, lname=None):
        '''
        creates a new user file in the database
        :param username: (str) the user's username
        :param password: (str) the user's password
        :param email: (str) the user's email
        :opt param fname: (str) the user's first name
        :opt param lname: (str) the user's last name
        :returns: (int) the insert id for the document
        '''
        # check to see if a user already exists with the given username or email address
        if self.checkIfUserExists(username, email):
            print('User already exists')
            return

        # each newly created user is assigned an object id by the system to act as the
        #   primary key
        userData = {
            'username':username,
            'password':password,
            'email':email,
            'fname':fname,
            'lname':lname,
            'achievements':[],
            'friends':[],
            'analyses':[]
        }
        insertID = self.usersCollection.insert_one(userData)
        return insertID

    def checkIfUserExists(self, username, email):
        '''
        check if a user with a given username or email already exists in the database
        :param username: (str) the user's username
        :param email: (str) the user's email
        :returns: (boolean) True if user is in db, else False
        '''
        userData = {'$or': [{'username':username},{'email':email}]}
        user = self.usersCollection.find_one(userData)
        if user is not None:
            return True
        return False
    
    def getUser(self, username, password):
        '''
        get user data given a username and password
        :param username: (str) the username of the user
        :param password: (str) the password of the user
        :returns: user object
        '''
        userData = {'username':username, 'password':password}
        user = self.usersCollection.find_one(userData, {'password':0})
        if user is not None:
            userObj = User(user['_id'], user['username'], 
                user['email'], user['fname'], user['lname'], user['friends'], 
                user['achievements'], user['analyses'])
            return userObj
        return None

    def giveUserAchievement(self, user, ach_name):
        '''
        add an achievement to a user's list of achievements
        :param user: (user) the user object
        :param ach_oid: (object id) the object id for the achievement
        :returns: (boolean) True if added, else False
        '''
        achName = {'name':ach_name}
        achievement = self.achievementsCollection.find_one(achName)

        # return False is user already has achievement
        if achievement in user.getAchievements():
            return False

        user.giveAchievement(achievement)
        userData = {'_id':user.getOid()}
        achData = {'$set':{'achievements':user.getAchievements()}}
        self.usersCollection.update_one(userData, achData)
        return True

    def uploadAnalysis(self, user, analysisVal, analysisString):
        '''
        upload an analysis for a user
        :param user: (user) the user object
        :param analysis: (analysis) the analysis object
        '''
        post = {"value": analysisVal, "string": analysisString}
        self.analysisCollection.insert_one(post)
        anlName = {'string': analysisString}
        analy = self.analysisCollection.find_one(anlName)
        user.giveAnalysis(analy)
        userData = {'_id': user.getOid()}
        anlData = {'$set': {'analysis': user.getAnalysis()}}
        self.usersCollection.update_one(userData, anlData)
        return True


if __name__ == '__main__':
    mgr = DBController()
    mgr.createUser('collinmatz',12345,'collin.matz.a@gmail.com','Collin','Matz')
    user = mgr.getUser('collinmatz',12345)