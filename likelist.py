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


# custom_list = ["dylan_dema"]

#session.unfollow_users(amount=20, custom_list_enabled=True, custom_list=custom_list, custom_list_param="all", style="RANDOM", unfollow_after=60*60*48, sleep_delay=120)

#session.remove_follow_requests(amount=200, sleep_delay=60)
session.set_do_like(True, percentage=100)
session.interact_by_users([ "dkulasooriya", "__tvabby__", "dandiliony11", "aadxl.00", "fahad_zehen01", "_sachiii_jayasekara", "_.kithuxy._", "i_s_h_a_r_a__eranda", "_pasi__dilshan_", "pramoo_", "___aakshe___", "fajaskhan_", "madushani_gunasekara", "shazny_shz", "travel_with_wife", "senali.desilva", "samadi_pathirana", "malith.jayasinghe", "kasun__lak9756", "sanduni_rathnapala", "_._uzy_7_._", "savii_chamuu", "dil_miii99", "harinieyy.__96", "nathaa_shaa_", "charukaa_lalithyaa", "ranish_20_", "_j.a_n.u_", "basurakavi", "deshu99_", "madu.nadeeshan", "sadunperera_", "aashaf__", "peniel_07", "_disali_.vino_", "nethma_oshadi", "madhavee_herath_", "umanda.s", "my3____", "shehdezoysa", "kaveeshasadruvan", "hashii_dwyer", "andy_livinya", "sh_x_han", "dilanka_liyanage", "ranuga_.vw", "mr_alankara", "_nipu_rathnayaka_", "h.bhagya", "sandy.yy__", "__.h_a_n_siii.__", "ayomishanelka", "yayeshamadumali", "chathukaushi", "deerasingha", "chathurinipunika1186", "oditha98", "keshara_thanthirimalage_", "iam_sanupraveen", "moohamed___hadhil_06", "ze_zimam", "_____sandun_____99", "iamilangoilangovan", "chandi_era__", "hustlin_luc", "__manoj_lakshan_", "t.ruwanpriya", "d1l7uksh4n", "rushee.___", "i.am.prav", "aishuhamsi_23", "milan.pasindu", "babie_girl______", "gayan.dm", "global5208", "damindakapila", "dil_sandu_99", "_madhini_hm", "____parindya____", "_.hiru._11", "zii_ser", "____.hiru_prabha_fdo.___", "sewwandik191", "shehanidickumbura", "_sudeshi_rathnaweera_", "_____heshi", "_naveen.klhara_", "hanee.spamm", "shenu_weerasingha_", "madhusani9", "biguniyehansa", "geeshani_binu", "_ranu.li_", "tani.ya9217", "liliyaa_ss", "___.niko._____", "vish.mii", "isururandeniya92", "_prince_of_srilanka_", "irajw", "______bhashi______", "___im__randhi___", "walisunfara", "nethmisandeepa12", "cutey_aani", "kavishka_jayawardhana", "_kaviii98_", "kavindirasanjali", "tatyanaljr", "ravindu_wanigasekara", "kosala_96", "cocogardenhh", "ama_jayasooriya_", "nilakshie_", "cw.pramuditha", "ucsc.pahasara", "sans_tagram_"], amount=10, randomize=True, media='Photo')


#session.follow_by_list(custom_list, times=2, sleep_delay=120, interact=True)
#session.set_user_interact(custom_list, amount=2, randomize=True, percentage=90, media='Photo')
#session.set_do_like(True, percentage=10)
# end the bot session
session.end()
