# Import all Libraries
from balloontip import WindowsBalloonTip
import feedparser
from time import sleep, gmtime, strftime
import hashlib

# Set all Variables
python_wiki_rss_url = "https://hackflag.org/forum/syndication.php?limit=1"
old_feed = []

while True:
    try:
        feed = feedparser.parse(python_wiki_rss_url)

        for item in feed.entries:
            if item.title not in old_feed:

                print("[{0}] New Thread! {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),item.title))  #Print the data to the console!
                WindowsBalloonTip.balloon_tip("New thread on HackFlag!", item.title)
                old_feed.append(item.title)
        sleep(10)
    except KeyboardInterrupt:
        print("")
        print("Goodbye!")
        break


# Shameless notepad:


# WindowsBalloonTip.balloon_tip("test", "test message")

# print(hashlib.sha512((python_wiki_rss_url).encode('utf-8')).hexdigest())
