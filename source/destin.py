########  ########  ######  ######## #### ##    ##    ########  ##    ##
##     ## ##       ##    ##    ##     ##  ###   ##    ##     ##  ##  ##
##     ## ##       ##          ##     ##  ####  ##    ##     ##   ####
##     ## ######    ######     ##     ##  ## ## ##    ########     ##
##     ## ##             ##    ##     ##  ##  ####    ##           ##
##     ## ##       ##    ##    ##     ##  ##   ### ## ##           ##
########  ########  ######     ##    #### ##    ## ## ##           ##

########################################################################
#                       Author: DeCoded_Void                           #
#                        Discord: Void#1337                            #
#                    E-mail: void@decodedvoid.com                      #
#                                                                      #
#                             Credit:                                  #
#                 https://github.com/Bungie-net/api                    #
#          https://github.com/DestinyDevs/BungieNetPlatform/           #
########################################################################

import asyncio
import aiohttp
import json
import os
import urllib

__version__ = '0.0'

ROOT_PATH = 'https://www.bungie.net/Platform/'
USER_PATH = ROOT_PATH + 'User/'
CONTENT_PATH = ROOT_PATH + 'Content/'
FORUM_PATH = ROOT_PATH + 'Forum/'
GROUPV2_PATH = ROOT_PATH + 'GroupV2/'
DESTINY2_PATH = ROOT_PATH + 'Destiny2/'
TRENDING_PATH = ROOT_PATH + 'Trending/'
FIRETEAM_PATH = ROOT_PATH + 'Fireteam/'

class api:
    def __init__(self, API_KEY):
        self.api_key = API_KEY
        self.CommunityContent = CommunityContent(self.api_key)
        self.Content = Content(self.api_key)
        self.Destiny2 = Destiny2(self.api_key)
        self.Fireteam = Fireteam(self.api_key)
        self.Forum = Forum(self.api_key)
        self.GroupV2 = GroupV2(self.api_key)
        self.Trending = Trending(self.api_key)
        self.User = User(self.api_key)

    async def process(self, url):
        """To process the api request, GET only."""
        headers = {'X-API-KEY':self.api_key}
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=headers) as resp:
                    if resp.status == 200:
                        response = await resp.json()
                        return response
                    else:
                        raise Exception(f'Unable to connect to Bungie.net\nError code: {resp.status}')
            except Exception as error:
                raise Exception('Unable to connect to Bungie.net')
            await session.close()

class CommunityContent:
    def __init__(self, key):
        self.key = key

class Content:
    def __init__(self, key):
        self.key = key

class Destiny2:
    def __init__(self, key):
        self.key = key

    async def GetPublicMilestones(self):
        """Gets public information about currently available Milestones

        Arguments:
            None

        Returns:
            The current version of the manifest as a json object.
        """
        url = DESTINY2_PATH + 'Milestones/'
        resp = await api(self.key).process(url)
        if resp['ErrorCode'] == 1:
            return resp
        else:
            raise Exception(f'Failed GetPublicMilestones with error code {url["ErrorCode"]}')

class Fireteam:
    def __init__(self, key):
        self.key = key

class Forum:
    def __init__(self, key):
        self.key = key

class GroupV2:
    def __init__(self, key):
        self.key = key

class Trending:
    def __init__(self, key):
        self.key = key

class User:
    def __init__(self, key):
        self.key = key
