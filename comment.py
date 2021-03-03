from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,headless_browser=True,want_check_browser=False)
session.login()

# set up all the settings
session.set_relationship_bounds(enabled=True,
				 potency_ratio=-1.21,
				  delimit_by_numbers=True,
				   max_followers=4590,
				    max_following=5555,
				     min_followers=45,
				      min_following=77)
session.set_do_comment(True, percentage=10)
session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
session.set_dont_include(['friend1', 'friend2', 'friend3'])
session.set_dont_like(['pizza', 'girl'])

# do the actual liking

#session.follow_user_followers(['go_lk', 'lerevedhikka', 'marinard3'], amount=5, randomize=False, interact=False)

#session.like_by_tags(['sriLanka', 'cocogardenhh'], amount=10)
#session.set_comments(['Nice shot!'], media='Photo')
#session.set_do_comment(True, percentage=25)
#session.set_comments(['Awesome', 'Really Cool', 'I like your stuff'])

session.set_do_follow(False, percentage=50)
#session.set_comments(["Cool", "Super!"])
session.set_do_comment(False, percentage=80)
session.set_do_like(True, percentage=70)
session.interact_by_users(['shanudrie', '__dumikasun__', 'shanudrie'], amount=5, randomize=True, media='Photo')

#session.interact_user_followers(['dinuk_wik'], amount=3)

# end the bot session
session.end()
