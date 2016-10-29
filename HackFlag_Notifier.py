# Import all Libraries
import feedparser
from time import sleep, gmtime, strftime
import hashlib
import platform
import _thread as thread

# Check if OS is Windows and if it is, then import the balloontip library.
if platform.system() == "Windows":
    from balloontip import WindowsBalloonTip

# Set all Variables
rss_url = "https://hackflag.org/forum/syndication.php" # URL to get the RSS feed.
old_feed = [] # Just put all articles in an array so we can check if something changed!
limit = 1 # Set a limit on the articles
start_complete = False

def get_feed(rss_url, limit, start_complete):
    global old_feed
    feed = feedparser.parse(rss_url) # Get the feed from the RSS Provider
    for index, item in enumerate(feed.entries):
        if index == limit:
            break # Exit the for loop
        if item.title not in old_feed: # If the item title is not in the handled feed array yet
            old_feed.append(item.title) # Add the threadname to the array of articles we already handled.
            if start_complete == True: # Do not show the latest thread until 1 loop has been completed
                print("[{0}] New Thread! {1}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),item.title))  # Print the data to the console!
                if platform.system() == "Windows": # Check if OS is Windows
                    WindowsBalloonTip.balloon_tip("New thread on HackFlag!", item.title) # Send the notification!
    

while True:
    try:
        thread.start_new_thread(get_feed,(rss_url, limit, start_complete)) # Use Multithreading to make sure the script doesn't lock up when displaying a bubble (Might put this in the balloontip.py tho)
        start_complete = True
        sleep(1) # Sleep for 1 second to decrease load on both system and RSS provider
    except KeyboardInterrupt: # Catcha  KeyboardInterupt (CRTL+C for example)
        print("")
        print("Goodbye!")
        break # Exit the script


# Shameless notepad:


# WindowsBalloonTip.balloon_tip("test", "test message")

# print(hashlib.sha512((python_wiki_rss_url).encode('utf-8')).hexdigest())
