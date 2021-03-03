from instapy import InstaPy

insta_username = 'username'
insta_password = 'password'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,headless_browser=True,disable_image_load=True,want_check_browser=False)
session.login()

# set up all the settings ,want_check_browser=False
session.set_skip_users(skip_private=False,
                       private_percentage=100)

#session.set_user_interact(amount=2, randomize=True, percentage=90, media='Photo')
#session.set_do_like(True, percentage=100)

custom_list = ["divyansh2706", "anurag_jayant", "s_a_s_i_n_d_u_madushan", "desitadhka", "_senu_x.__", "x__sk_____x____", "nadun_2.0", "nadipathi_silva", "chanaka__dilshan", "bs.gram_", "sandun_sonu_prasanna", "kv.creativ", "steevy__1", "_.manusha_", "seven.official.lk", "_osanka", "ashendion", "crustandcuppies", "divyanjalie_7_", "wmc_abhiman", "musamakhan111", "__s_a_j_i__96", "mr__k_e_v_i_n__", "arjun366", "sashini19", "hashii_sha", "elina.abhi", "iroshaudantha2004", "vilasiiiii", "sweet_choco90", "meliza_xi_", "tomorrowisbeauty", "ashishbansal1990", "_saajth_jr", "_t_a_s_h_e_n", "s_h_e_h_a_n__t_h_i_w_a", "perera.diyon", "_.mr.suppa._", "ishini__gunasekera", "ohmyplattersl", "jewellbyindii", "_ni.pp.ha_", "campus_diary", "__nihara.athukorala___", "evanzz_owns", "__ashi_521", "vihanga_kaushan", "gopro_kasuna_", "baita_66_", "s_e_l___4", "__nalaka__d", "paddle_srilanka", "b__a__w__a__", "_p.a.s.i_", "kaushi_senavirathna", "praveen_dilan_", "_ravindu_n_a_", "_chami__01", "dinith_dabarera", "c__chord", "cheths__", "poorna_methmi", "duwashi_attanayaka", "_damitu_rajapaksha_", "ishi_madusanka", "_____.chathu_", "king_s_a_m_m_a", "lakshaniiweerasinghee", "maduka___96", "__shihan__twis___", "davidauer_", "always__nd__forever", "prabashii_", "lurk.lk_official", "bloggers.sl", "angelo_peiris", "amy_grace565", "c.h.o.x", "_sayuri_rajapaksha_", "v.i.v.i.d_s.h.o.t.s", "vima__boy", "pra_sha_29", "riyuu_uu_20", "ishan_ikaushalya", "alok_samarasinghe", "yumiiii_99", "esana_lk", "shami_sathindra", "itsmemaleesha", "dewumi_prarthana", "momma_loves_ceylon", "sandu_nimh", "_r_a_s_h_u___", "akilaluvs_", "menushasubanissanka", "i_s_k_98", "______malsha", "__i_m_a_l_k_a___2000_", "mj_hunter_63", "jonassilvahede", "suryabhushansingh_sr", "mr.hasaranga", "imthihan", "d_i_l_h_a_n_thanuj._", "y_e_n_u_l__", "prem_anie", "born__a__warrior", "_pr_a_sa_", "_virun_k", "maleesha.c_", "_iam_kaveesh_", "____heshi_cute15", "_________juthika_j_", "art_galore_lk", "miss__rukhsar__22", "clicks_by_yasa", "isuru__malshan", "land_of_kings_cafe_restaurant", "tiranbashitha", "timschwa", "kanchanaanuradhi", "manee_sewwandi_", "chathurangikamanosha", "ravidu____", "saxfuth", "devindi_siwurathna", "_____kaveesha_____", "_.devni_ranasinghe._", "tharanilokuge", "tharindusupun.herath1999", "mr_sahil_8301", "_.bineth._", "arifahmadlone883", "mr.jack461", "cooking_girl_diaries", "kksaggela", "arman.hossain.26", "pasan___senarathne", "__bhathiii", "chathu190", "_khush_arts"]

session.unfollow_users(custom_list_enabled=True, custom_list=custom_list, custom_list_param="all", style="RANDOM", unfollow_after=60*60*48, sleep_delay=600,amount=1000)




#session.follow_by_list(custom_list, times=2, sleep_delay=120, interact=True)
#session.set_user_interact(amount=7, randomize=True, percentage=90, media='Photo')
#session.set_do_like(True, percentage=100)
#session.interact_by_users(custom_list, amount=7, randomize=False)

# end the bot session
session.end()
