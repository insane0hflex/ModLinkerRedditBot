import praw
import pprint
import time
import datetime
from mod import Mod

# for comment in praw.helpers.comment_stream(r, "skyrimmods"):
    # if was_a_mod_mentioned(comment) != "":
        # bot_action(comment)

# def was_a_mod_mentioned(comment):
    # text = comment.body
    # text_tokens = text.split()
    
    # for mod in skyrim_mods:
        # if mod.mod_name.lower() in text_tokens:
            # return mod
        # else:
        #   # return ""

# def bot_action(comment, mod):
    # reply_text = mod.get_mod_link()
    # reply_text += "\n"
    # reply_text += "Skyrim Mod Linker bot by /u/insane0hflex \n"
    # comment.reply(reply_text)


SKYRIM = "skyrim"
FALLOUTNV = "falloutnv"
FALLOUT3 = "fallout3"
FALLOUT4 = "fallout4"

R_SKYRIMMODS = "skyrimmods"
R_FALLOUTMODS = "falloutmods"

def end_reply_text():
    reply =  "    ---------------------------------------- \n"
    reply += "    Mod Linker by /u/insane0hflex \n"
    reply += "    Send a message to /u/insane0hflex if something went wrong.\n"
    return reply


# currently these mods are in memory here
# maybe in the future do a sqlite or a plain JSON text file with mod information
# these simple arrays are mainly for testing
# also people usually mention the "big top 50ish" mods
skyrim_mods = []

skyrim_mods.append(Mod("SkyUI", 3863, SKYRIM))
skyrim_mods.append(Mod("iHUD", 3222, SKYRIM, ["immersive hud", "i hud"]))

# i wonder if the space in the name will mess up the text in comment search?
skyrim_mods.append(Mod("Enhanced Camera", 57859, SKYRIM, ["ec"]))

# skyrim_mods.append(Mod("", 1, SKYRIM)



fallout4_mods = []
# fallout4.append(Mod("", 57859, SKYRIM))


for mod in skyrim_mods:
    mod.print_out()
    print(mod.get_mod_link())
    
    # json like print out - maybe to disk or something?
    # pprint.pprint(mod.get_mod_info_as_json())


print("Starting...")

r = praw.Reddit("skyrim mod linker bot by /u/insane0hflex")

username = "modlinkerbot"
password = ""

with open("password.txt", "r") as f:
    password = f.readline().strip() #strip might be uneccessary here.

#print password

print("Logging into reddit as " + username)

r.login(username, password, disable_warning=True)

print("Logged in successfully!")

# already_done = set()

# while True:

    # all_comments = r.get_comments("skyrimmods")

    # print ("Retrieved " + str(len(all_comments)) + " comments total.")

    # # this flatten_tree may not be needed
    # comments = praw.helpers.flatten_tree(all_comments)

    # for comment in comments:
        # if comment.id not in already_done:

            # reply_text = ""

            # for mod in skyrim_mods:
                # if mod.mod_name.lower() in body.lower():
                    # print ("Found a mod name match!" + str(datetime.now()))
                    # mod.print_out()
                    # reply_text += mod.get_mod_link() + "\n"
                    # already_done.add(comment.id)

            # if reply_text != "":
                # reply_text += end_reply_text()
                # comment.reply(reply_text)
                # print("Replied with" + reply_text + "\n\n")
                # print("Sleeping for 10 minutes now\n")
                # time.sleep(605)
            # else:
                # print ("No matches found.")








