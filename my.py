from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,headless_browser=True,
		  disable_image_load=True,want_check_browser=False)
session.login()

# set up all the settings
session.set_relationship_bounds(enabled=True,
				 potency_ratio=None,
				  delimit_by_numbers=True,
				   max_followers=5000,
				    max_following=8000,
				     min_followers=45,
				      min_following=77)

session.set_skip_users(skip_private=False,
			private_percentage=0,
                      	skip_no_profile_pic=True,
                       	no_profile_pic_percentage=100)


session.set_do_like(enabled=True, percentage=94)


session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
session.follow_user_followers(['____sasindu____'], amount=10, randomize=False, interact=True)
session.set_do_like(enabled=True, percentage=94)


#session.interact_user_followers(['____.dika.____'], amount=50, randomize=True )


# end the bot session
session.end()
