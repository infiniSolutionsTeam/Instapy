from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,headless_browser=True, disable_image_load=True,want_check_browser=False)
session.login()

# set up all the settings
#session.set_relationship_bounds(enabled=True,
#				 potency_ratio=None,
#				  delimit_by_numbers=True,
#				   max_followers=40590,
#				    max_following=50555,
#				     min_followers=45,
#				      min_following=77)
session.set_user_interact(amount=15, randomize=True, percentage=100,
                              media='Photo')
session.set_do_follow(enabled=True, percentage=20)
session.set_comments(["Beautiful", "Superb!"])
session.set_do_comment(enabled=True, percentage=80)
session.set_do_like(True, percentage=100)
#session.comment_by_locations(['242146142'], amount=100, skip_top_posts=True)
#session.interact_by_users(['priyanath_goonetileke','dylan_dema', 'namu_darra','praveen_himantha_'], amount=10, randomize=True, media='Photo')
session.interact_user_followers(['dinakshie','agasidewni_official','shanudrie'], amount=100)
# end the bot session
session.end()