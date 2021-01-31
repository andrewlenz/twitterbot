import tweepy
from tkinter import Tk, Entry, Label, Button

# consumer_key = "1YlQR4s1xhodnQevmEyiADn85"
# consumer_secret = "0YOyhqdGedRCsGSyu1FqrROPjbbbLqb2ramTgkXH68uhrc8n8f"
#
# access_token = "954776702751621120-yoah0tyRyhLrpJq9x9z03Og1GX7Azeg"
# access_token_secret = "4Sz31tseXPZdOXNtyEOo59fkISktwaRhYu8m6QKLOsB4P"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.name)

root = Tk()
label1 = Label(root, text="Search")
E1 = Entry(root, bd=5)
label2 = Label(root, text="Number of Tweets")
E2 = Entry(root, bd=5)
label3 = Label(root, text="Response")
E3 = Entry(root, bd=5)
label4 = Label(root, text="Reply?")
E4 = Entry(root, bd=5)
label5 = Label(root, text="Retweet?")
E5 = Entry(root, bd=5)
label6 = Label(root, text="Favorite?")
E6 = Entry(root, bd=5)
label7 = Label(root, text="Follow?")
E7 = Entry(root, bd=5)


def getE1():
    return E1.get()


def getE2():
    return E2.get()


def getE3():
    return E3.get()


def getE4():
    return E4.get()


def getE5():
    return E5.get()


def getE6():
    return E6.get()


def getE7():
    return E7.get()


def mainFunction():  # The main code
    search = getE1()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    response = getE3()
    phrase = str(response)
    reply = getE4()
    retweet = getE5()
    favorite = getE6()
    follow = getE7()

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
                print("Replied with " + phrase)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    if retweet == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.retweet()
                print('Retweeted the tweet')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    if favorite == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.favorite()
                print('Favorited the tweet')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    if follow == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.user.follow()
                print('Followed the tweet')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit = Button(root, text="Submit", command=mainFunction)
submit.pack()
root.mainloop()
