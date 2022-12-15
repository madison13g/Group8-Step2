# Forum Package Description

**Package Description:** The Forum package will allow users to search through forums (i.e. Reddit) to look at specific users, topics, and posts. It will also allow for special privileges for administrators.

## Subpackages

### **Subpackage 1:** Person

This subpackage will feature all package information surrounding users and admins, and their features and functions.

#### Module 1 - User

This includes the class definition of the user.
The functions in this module include:
* Initialize Class
  * User is composed of a username and a password, and the password is a private attribute.
* displayUser()
  * This formats the printed username when the user is called to be displayed.
* password()
  * This allows the user to access the private attribute and change the password. 

#### Module 2 - Administrator

This includes the class definition of admin, which has inheritance from class User.
The functions in this module include:
* Initialize Class
  * This admin class inherits everything from user, as well as an admin code.
* displayUser()
  * This formats the printed username when the user is called to be displayed.
* displayCount()
  * This checks the number of users currently registered in the system.
* userlist()
  * This allows admins to see a list of registered users in the system.

### **Subpackage 2:** Content

This subpackage will feature all package information surrounding topics and posts, including their features and functions.

#### Module 1 - Topic

This includes the class definition of the topic.
The functions in this module include:
* Initialize Class
  * This topic class includes the tag and username.
* tag()
  * This allows the user to access the private attribute and change the tag.
* show()
  * This displays topic info of the topic ID and topic name.
* search()
  * This searches all topics under a given topic.

#### Module 2 - Post

This includes the class definition of the admin, which has inheritance from class User.
The functions in this module include:
* Initialize Class
  * This class inherits everything from post, as well as details.
* add_comment()
  * Allows users to add a comment to a post.
* add_like()
  * Allows users to add a like to a post.
* check()
  * Allows users to check the number of likes and comments on a post.
* search_all_posts()
  * Shows posts under a given topic.
* search_post()
  * Show posts with given keyword.
