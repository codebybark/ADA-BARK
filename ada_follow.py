USERNAME = "vodkablink"
PASSWORD = "RAjBhRQf%qDcqK24"

import logging
from instagrapi import Client, exceptions
from time import sleep
import random
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='follow_bot.log',
    filemode='a',
    format='%(asctime)s [%(levelname)s] %(message)s'
)
# List of usernames to follow
usernames_to_follow = [
    "coldwarmagazine", "brutgroup", "slavsquat",
    "soviet.visuals", "kalashnikov.group", "kazakh.view", "rus_mil_art", "chernobyl_guide",
    "acoldwall", "techwear.intern", "gothictechwear", "rickowensonline", "helmutlang",
    "darkwear_fashion", "militaryvibes", "cyberdogofficial", "acronym_official", "blvckparis",
    "liquidverve", "brandontakesphotos", "peterlindbergh", "vuhlandes", "ryanmuirhead",
    "neonnoir.mag", "joelfentonphoto", "cinestillfilm", "sashalevin", "noir.camera",
    "ptsdsupportandawareness", "woundedwarriorproject", "mentalhealthamerica", "headstrongproject", "mission_22",
    "mentalhealthmemes", "realdepressionproject", "thefightwithinher", "broken_light_collective", "mentalhealthmatch",
    "agentprovocateur", "playboy", "savagexfenty", "lasciviouslingerie", "bondagecouture",
    "fleurdu.mal", "intimissimi", "victoriassecret", "nudamag", "darkromance",
    "love.death.and.robots", "witchernetflix", "blackmirror.netflix", "atomicblondemovie", "theboys",
    "netflixdark", "johnwickmovie", "killbillofficial", "matrixmovie", "strangerthingstv",
    "smirnoff", "absolutvodka", "stoli", "greygoose", "vodka_soda",
    "cocktailchemistry", "licensed_to_distill", "thevodkapost", "thetipsybartender", "imbibe",
    "shitheadsteve", "daquan", "sarcasm_only", "epicfunnypage", "dankmemes",
    "girlswithguns", "scarymommy", "bitch", "worst.buy", "overheardla"
]

def safe_follow(client, username):
    """
    Attempt to follow a user.
    1) Check if we are already following them.
       - If yes, skip.
    2) If login_required arises, re-login and retry once.
    """

    def _do_follow():
        user_id = client.user_id_from_username(username)
        user_info = client.user_info(user_id)

        # Check if we are already following this user
        if user_info.followed_by_viewer:
            msg = f"{username} already following, skipped"
            print(msg)
            logging.info(msg)
            return

        # Not followed yet, proceed
        client.user_follow(user_id)
        msg = f"Followed: {username}"
        print(msg)
        logging.info(msg)

    try:
        _do_follow()
    except Exception as e:
        if "login_required" in str(e).lower():
            msg = f"'{username}' follow failed with login_required; reattempting login..."
            print(msg)
            logging.warning(msg)
            try:
                client.login(USERNAME, PASSWORD)
                logging.info("Re-login successful, retrying follow.")
                _do_follow()
            except Exception as e2:
                err_msg = f"Re-login failed or could not follow {username}: {e2}"
                print(err_msg)
                logging.error(err_msg)
        else:
            err_msg = f"Error following {username}: {e}"
            print(err_msg)
            logging.error(err_msg)

def main():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    print("Login successful!")
    logging.info("Login successful!")

    for username in tqdm(usernames_to_follow, desc="Following users", unit="user"):
        safe_follow(cl, username)
        # Random delay between 30 minutes (1800s) and 2 hours (7200s)
        random_delay = random.randint(30 * 60, 2 * 60 * 60)
        print(f"Sleeping for {random_delay} seconds before next follow...")
        sleep(random_delay)

if __name__ == "__main__":
    main()

