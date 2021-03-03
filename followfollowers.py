from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,headless_browser=True,disable_image_load=True,want_check_browser=False)
session.login()

# set up all the settings
session.set_skip_users(skip_private=False,
                       private_percentage=100)
session.set_relationship_bounds(enabled=True,
				 potency_ratio=-0.21,
				  delimit_by_numbers=True,
				   max_followers=40590,
				    max_following=50555,
				     min_followers=45,
				      min_following=77)
session.set_do_follow(enabled=True, percentage=80)
session.set_do_like(True, percentage=100)
session.set_user_interact(amount=30, randomize=True, percentage=100, media='Photo')
#session.follow_by_tags(['handmadecraft','handmadekeytags','quiling','quilings','resins','resinkeytags','keychains','chains'], amount=10)

session.follow_user_followers([ 'namu_darra','agasidewni_official','shanudrie'], amount=50, randomize=False, sleep_delay=600,interact=True)


# end the bot session
session.end()
