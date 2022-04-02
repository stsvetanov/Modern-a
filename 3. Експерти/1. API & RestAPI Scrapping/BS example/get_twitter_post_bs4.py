import time

from bs4 import BeautifulSoup
import requests
# handle = input('Input your account name on Twitter: ')
# ctr = int(input('Input number of tweets to scrape: '))

handle = "Pokemon"
ctr = 3

messages = set()

while True:
  res=requests.get('https://twitter.com/'+ handle)
  bs=BeautifulSoup(res.content,'lxml')
  all_tweets = bs.find_all('div',{'class':'tweet'})
  if all_tweets:
    for tweet in all_tweets[:ctr]:
      context = tweet.find('div',{'class':'context'}).text.replace("\n"," ").strip()
      content = tweet.find('div',{'class':'content'})
      header = content.find('div',{'class':'stream-item-header'})
      user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
      tweet_time = header.find('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'}).find('span').text.replace("\n", " ").strip()
      message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
      footer = content.find('div',{'class':'stream-item-footer'})
      stat = footer.find('div',{'class':'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()
      if message not in messages:
        if context:
          print(context)
        print(user, tweet_time)
        print(message)
        print(stat)
        print()
      messages.add(message)
  else:
    print("List is empty/account name not found.")
  time.sleep(5)
