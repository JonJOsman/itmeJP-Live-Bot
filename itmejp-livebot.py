#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import praw
import json
import urllib2
from config import *
 
print
 
stream = json.load(urllib2.urlopen('https://api.twitch.tv/kraken/streams/itmejp.json'))
 
r = praw.Reddit('itmeJP Live Bot by /u/Orschmann')
r.login(u, p)
subreddit = r.get_subreddit("itmeJP")
settings = r.get_settings(subreddit)
sidebar = settings['description']
 
sidebarLines = sidebar.split('\n')
lastLine = sidebarLines[-1]
 
if(stream['stream'] != None and lastLine != "[](http://www.twitch.tv/itmejp#sidebar)"):
    sidebar += "\n[](http://www.twitch.tv/itmejp#sidebar)"
    subreddit.edit_wiki_page('config/sidebar',sidebar,reason="JP Live Bot: JP goin' live.")
elif(stream['stream'] == None and lastLine == "[](http://www.twitch.tv/itmejp#sidebar)"):    
    sidebar = "\n".join(sidebarLines[:-1])
    subreddit.edit_wiki_page('config/sidebar',sidebar,reason="JP Live Bot: JP goin' offline.")