# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google Search For This Template
# Modified: NGB
#
#
# to find url of channel view channel source then find data-channel-external-id=
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.scamabc'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "UCBNG0osIBAprVcZZ3ic84vw" 
YOUTUBE_CHANNEL_ID_2 = "UCC9EjyMN_hx5NdctLBx5X7w" 
YOUTUBE_CHANNEL_ID_3 = "UCUZb_t6bIRSwyUeEaU6e5xQ" 
YOUTUBE_CHANNEL_ID_4 = "UC0uJKUXiU5T41Fzawy5H6mw" 
YOUTUBE_CHANNEL_ID_5 = "UCm22FAXZMw1BaWeFszZxUKw" 
YOUTUBE_CHANNEL_ID_6 = "UC_0osV_nf2b0sIbm4Wiw4RQ"  
YOUTUBE_CHANNEL_ID_7 = "UCxzXRl9vxhPhyYITOlPW9dg" 
YOUTUBE_CHANNEL_ID_8 = "UC_b1bYSup-dHfwIoIXP0zPQ" 
YOUTUBE_CHANNEL_ID_9 = "UC7AyZF0m_WV4GSXcBOg8V5Q" 
YOUTUBE_CHANNEL_ID_10 = "UCxCJ93k6uk-qarMgFpX-Otw"
YOUTUBE_CHANNEL_ID_11 = "UCqTQnJ_Wk0PAzWCOHMfefDQ"
YOUTUBE_CHANNEL_ID_12 = "UCx9yZ74cCszjui8H90cUN8A"
YOUTUBE_CHANNEL_ID_13 = "UCnNlJNSRxa3PF8XrKHOEPug"
YOUTUBE_CHANNEL_ID_14 = "UCLZxPVkEvf9XuifStuHK_gA"
YOUTUBE_CHANNEL_ID_15 = "UCdFypR5fbIFjaA5csQpgVQg"
YOUTUBE_CHANNEL_ID_16 = "UCAf6Q_sHACA__65xc37waLQ"
YOUTUBE_CHANNEL_ID_17 = "UCTKTCy5UBdCqnGcj2f4Ozug"









# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Jim Browning",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJyDVexp6fiiGzLEWkxZgS_r2YM93Gp8OpMltA=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Scammer Payback",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxLK59I5nIdm6rfSsxtNcIjSY8UkTsdTs4Rkg=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Scammer Payback Live",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxFPhs_SI1XY2znaJ_XEH8USTlmXv3wMwS86A=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ScammerRevolts",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJz4oqkoqszfVnc4Y6j4dlhNIV9aFbZ_qnCeSA=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kitboga",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJyimKCrHACbLEWlP29PnyTh9mJkRNH4M1ycBA=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="IRLrosie",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJz9ZU477gdFP6jcaVLA8Fc7N-rCjFwe1RKAkg=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Deeveeaar",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJypJVfVInV0OeM4l3LD85m17Taax2c7FFLfsw=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Malcolm Merlyn",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxEzKN2LjOHp5z96PRL3T0Th63FkQuXSO-1Qg=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )   
        
    plugintools.add_item( 
        #action="", 
        title="BobHasAVirus",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJzWZc81BXjWLKCPFXW0iZ5kUzh7OUmLOgrTUA=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )   


    plugintools.add_item( 
        #action="", 
        title="ScamBait Central",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJwubiCD9tLrJx80zGERFl7M7RItq_XN3_hKgA=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )   
    
    plugintools.add_item( 
        #action="", 
        title="NeeP",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJyYS7IMctlZw5NXnUwJ3VIePadfdlXk4wdIYw=s176-c-k-c0x00ffffff-no-rj-mo",
      folder=True )   
    

    plugintools.add_item( 
        #action="", 
        title="Thunder Dragon",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJzuB7NyKyFby-PU9pl7zc5h5HWtAONxKAq5Uw=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )   
    
    plugintools.add_item( 
        #action="", 
        title="The Hoax Hotel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJwHCzAQo_u3MTQgTnu-BZAsCDeIpN35SS9rKQ=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )   
    
    plugintools.add_item( 
        #action="", 
        title="Lewis's Tech",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJzQ0KXvcMhXxbSlD9lOciIeoJMuuELNKkszOQ=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="IRS I reck scammers",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxvwEEJpOkJBMAB-JD0O7GcitjiL9BnTfgFaw=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )   
    
    plugintools.add_item( 
        #action="", 
        title="IT Advocate",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJyHlZmfKSEkRATGSztOOSfOePum7wMjs7B3qA=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )       

    plugintools.add_item( 
        #action="", 
        title="JayBeeTV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxM71HTvvVqoQ2awSPeV-VOg6We5_s-N-VAaQ=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )   					
run()