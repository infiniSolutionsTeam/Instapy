from instapy import InstaPy
from instapy import smart_run

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,headless_browser=True,disable_image_load=True ,want_check_browser=False)
session.login()

# set up all the settings
session.set_skip_users(skip_private=False,
                       private_percentage=100)


#session.remove_follow_requests(amount=200, sleep_delay=60)
session.set_user_interact(amount=5,
				 percentage=100,
                  randomize=True,
                   media='Photo')
session.set_do_like(True, percentage=100)
with smart_run(session):
	session.follow_likers(['1000tattoos_by_layantha'], photos_grab_amount = 1, follow_likers_per_photo = 100, randomize=False, sleep_delay=60, interact=True)
#session.like_by_feed(amount=10, randomize=False, unfollow=False, interact=True)


#session.follow_by_list(custom_list, times=2, sleep_delay=120, interact=True)
#session.set_user_interact(custom_list, amount=2, randomize=True, percentage=90, media='Photo')
#session.set_do_like(True, percentage=10)
# end the bot session

session.end()
