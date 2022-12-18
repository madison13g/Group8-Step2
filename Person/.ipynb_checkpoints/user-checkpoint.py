class User():
    """
    Includes User definition and functions.
    
    Parameters
    ----------
    userCount: count the number of User created
    users: list storing all current users
    usernames: list storing all user names
    """
    
    userCount = 1 
    
    users = [] 

    usernames = []
    
    def __init__(self, user, password):
        """
        Define the class user
        
        Parameters
        ----------
        user: the name of user
        id: the id of user (unique)
        password: personal password for login (private variable)
        """
        if user not in self.usernames:
            self.user = user
            self.id = User.userCount
            self._password = password # password is private 
            #print('Username: {}'.format(self.user))
            User.userCount += 1
            self.users.append(self)
            self.usernames.append(user)
        self.user = user
        
    def displayUser(self):
        """
        Display user info
        
        Returns
        ----------
        The string showing username.
        """
        return f'Username: {self.user}'
        
        # change password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

# Creating database of users
user1 = User('madison13g', 'password1')
user2 = User('amethyst1016', 'password2')
user3 = User('khaladhasan', 'khalad1')
user4 = User('jeffandrews', 'jeff1')
user5 = User('christeldeas', 'christel1')
user6 = User('gemarodriguezperez', 'gema1')
user7 = User('ifeomaadaji', 'ifeoma1')
user8 = User('johnthompson', 'john1')
user9 = User('emeliegustafsson', 'emelie1')
user10 = User('patricialassere', 'patricia1')



