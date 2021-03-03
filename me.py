from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,headless_browser=True,disable_image_load=True,want_check_browser=False)
session.login()

# set up all the settings

session.set_do_comment(True, percentage=1)
session.set_comments(['aMEIzing!','Nicey!'])
session.set_dont_include(['friend1', 'friend2', 'friend3'])
session.set_dont_like(['pizza', 'girl'])

# do the actual liking
session.like_by_tags(['anuradhapura', 'travel'], amount=1)

# end the bot session
session.end()
