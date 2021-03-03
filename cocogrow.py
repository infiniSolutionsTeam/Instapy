from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor

session = InstaPy(username=insta_username, password=insta_password,headless_browser=True,disable_image_load=True,want_check_browser=False)
session.login()

# set up all the settings
session.set_skip_users(skip_private=True,
                       private_percentage=100)

session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=1000,
                                    max_following=2950,
                                    min_followers=150,
                                    min_following=150)

session.set_do_like(True, percentage=100)
session.set_user_interact(amount=15, randomize=True, percentage=100, media='Photo')
session.follow_user_following([ 'trips_n_tips_'], amount=150, randomize=False, sleep_delay=60,interact=True)
#session.follow_by_tags(['anuradhapur', 'travelsrilanka','ruwanwalisaya','ruwanwelisaya'], amount=10, interact=True,skip_top_posts=True,randomize=True)

#session.unfollow_users(amount=50,  style="FIFO",unfollow_after=12 * 60 * 60, sleep_delay=601)
#session.unfollow_users(amount=200, nonFollowers=True, style="LIFO", sleep_delay=65,unfollow_after=12 * 60 * 60)

#session.like_by_feed(amount=100, randomize=False, unfollow=False, interact=True)
# end the bot session
session.end()
