from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,headless_browser=True,disable_image_load=False,want_check_browser=False)
session.login()

# set up all the settings
session.set_relationship_bounds(enabled=True,
				 potency_ratio=-0.21,
				  delimit_by_numbers=True,
				   max_followers=40590,
				    max_following=50555,
				     min_followers=45,
				      min_following=77)
session.set_do_follow(enabled=True, percentage=80)
session.follow_by_tags(['followtofollow', 'followtolike','follow4follow'], amount=50)

# end the bot session
session.end()
