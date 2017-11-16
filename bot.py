from steem.steem import Steem
from steem.steem import BroadcastingError
import threading
import time
import random
import csv
 
my_subscriptions = []
 
with open('votelist.txt', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        v = rows[0]
        my_subscriptions.append(v)
        
        # accounts and passwords
account = ["account_goes_here"]
posting_key = ["password_goes_here"]
# delay in seconds when the bot votes
vote_delay = random.randrange(1200,1800)

upvote_history = []
 
def feed():
    print("Waiting for new posts by %s\n\n\nGo Oprah!\nGo Winfrey!" % my_subscriptions)
    steem = Steem(wif=posting_key[0])
    for comment in steem.stream_comments():
 
        if comment.author in my_subscriptions:
            # Comments don't have titles. This is how we can know if we have a post or a comment.
            if len(comment.title) > 0:
 
                # check if we already upvoted this. Sometimes the feed will give duplicates.
                if comment.identifier in upvote_history:
                    continue
 
                print("New post by @%s %s" % (comment.author, url_builder(comment)))
                workerThread = threading.Thread(name=comment.identifier, target=worker, args=(comment,))
                workerThread.start()
 

def url_builder(comment):
    return "https://steemit.com/%s/%s" % (comment.category, comment.identifier)
 
def worker(worker_comment):
     time.sleep(vote_delay)
     try:
       for (k,v) in enumerate(account):
         worker_steem = Steem(wif=posting_key[k])
         upvote_comment = worker_steem.get_content(worker_comment.identifier)
         # vote weight 100 full power vote -100 full power flag
         upvote_comment.vote(100, v)
         print("@%s====> ^Upvoted^" % upvote_comment.author)
         upvote_history.append(upvote_comment.identifier)
     except BroadcastingError as e:
       print("@%s<- failed" % upvote_comment.author)
       print(str(e))

 
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
