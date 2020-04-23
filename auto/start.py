
# what do we want to run first when the app boots? 

# 1. check if there's an internet connection

# 2. load neccessary configurations

# 3. load updates ahead of time 

# 4. resume last action
import urllib.request as request

" Check if there's an internet connection"
def is_connected(_url = "https://google.com"):

    try:
        request.urlopen(_url)
        return True
    except:
        return False