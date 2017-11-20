from piston.steem import Steem
from piston.steem import BroadcastingError
import threading
import time
import random

# vote_list is regular favorites get a .001 sbd tip
vote_list = ["bitboss",  "user2", "user3", "etc"]
my_favorites = ["noly"]

my_subscriptions = top_writers + my_favorites

#put your details here only put the active key if you want to tip people in your favorites list
account = ""
posting_key = ""
active_key = ""
#the number of seconds to wait after a post is published before you vote 1800 seconds = 30 minutes
vote_delay = 1800

upvote_history = []

def feed():
    print("Waiting for new posts by %s\n" % my_subscriptions)
    steem = Steem(wif=posting_key, node="wss://node.steem.ws")
    for comment in steem.stream_comments():

        if comment.author in my_subscriptions:
            if len(comment.title) > 0:

                # check if we already upvoted this.
                if comment.identifier in upvote_history:
                    continue

                print("New post by @%s %s" % (comment.author, url_builder(comment)))
                workerThread = threading.Thread(name=comment.identifier, target=worker, args=(comment,))
                workerThread.start()

# tip the best guys
def send_a_tip(author):
    steem = Steem(wif=active_key)
    steem.transfer(author, 0.001, "SBD", memo="Here is a small gift for you.", account=account)

def url_builder(comment):
    return "https://steemit.com/%s/%s" % (comment.category, comment.identifier)

def worker(worker_comment):
     time.sleep(vote_delay)
     try:
       worker_comment.vote(50, account)
       print("====> Upvoted")
       worker_comment.reply('You have been upvoted by Prosper-ai! Enjoy!')
       upvote_history.append(worker_comment.identifier)
     except BroadcastingError as e:
       print("Upvoting failed...")
       print("We have probably reached the upvote rate limit.")
       print(str(e))

     if comment.author in my_favorites:
       send_a_tip(comment.author)
       print("====> Sent $0.001 SBD to @%s" % comment.author)


if __name__ == "__main__":
    while True:
        try:
            feed()
        except (KeyboardInterrupt, SystemExit):
            print("Quitting...")
            break
        except Exception as e:
            traceback.print_exc()
            print("### Exception Occurred: Restarting...")
