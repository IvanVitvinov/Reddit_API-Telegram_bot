import time
import praw
import re
import json


class RedditPars:

    def __init__(self):
        self.reddit = praw.Reddit(client_id='client_id', client_secret='client_secret', username='username', password='password', user_agent='user_agent')
        self.subreddit_list = ['your_subs']
        self.good_subs = []
        self.data = {'gs_ls': self.good_subs}

    def info_subs(self):

        for subreddit_name in self.subreddit_list:
            # Set search parameters
            subreddit = self.reddit.subreddit(subreddit_name)
            top_posts = subreddit.hot(limit=7)
            # Set the flag
            all_good = True
            # Listing posts of interest
            for post in top_posts:
                if int(time.time()) - int(post.created_utc) >= 28800:
                    # If the publication time is more than 8 hours, good sub
                    pass
                else:
                    if post.score < 50:
                        pass
                    else:
                        all_good = False

            if all_good:
                self.good_subs.append(subreddit_name)

        with open('Data/good_subs.json', 'w') as f:
            json.dump(self.data, f)

    def pars_comment(self):
        subreddit = self.reddit.subreddit('your_sub')
        comments = subreddit.comments(limit=5000)
        comment_set = set()

        for comment in comments:
            comment_set.add(comment.body)

        for comment in comment_set:
            comment_without_emojis = re.sub(r'[^\w\s]','', comment)
            if not any(word.lower() in comment_without_emojis.lower() for word in ['Exceptions words']):
                if 10 <= len(comment_without_emojis) <= 55:
                    print("\"" + comment_without_emojis + "\"\n")


def main():
    rp = RedditPars()
    rp.pars_comment()
    # or
    # rp.pars_comment()


if __name__ == '__main__':
    main()
