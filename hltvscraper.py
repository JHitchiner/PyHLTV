import requests
from hltvparser import *
from hltvplayer import *

# Useless right now but might find some use for it
BASEURL = 'https://www.hltv.org/stats/players/'
# Need user agent cause HLTV won't accept any connection without one
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}


def scrapePlayer():
	# Currently just takes top playre, can replace this URL with any player
	# Plan to add more players or a search feature
    r = requests.get('https://www.hltv.org/stats/players/7998/s1mple', headers=HEADERS)
    player = parseHTLVhtml(r)
    print(player.Player_Statistics.items())

def main():
    scrapePlayer()
    # Plan to add more scraping such as teams and articles

if __name__ == '__main__':
    main()
