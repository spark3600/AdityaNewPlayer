import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("14789064"))
API_HASH = getenv("0532c65daeaa8bed31350cb48eb5d78e")
BOT_TOKEN = getenv("5769782973:AAESB3geugmN2Q4u6Nqq0Syp2o_kmDc4bZU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("1BVtsOHcBu7B7_dGmf1TcRFuiKaROhm2biCcWg08Cnus5Z0pM-9AoNgEvrwApNJoF0YQMufQK9kL62bVOx3LaYENoNRvAe7hX0g0OJ7_cO7A2h35Oo0pudiPwY7FWBPbG_gIejsZZR4wHceIy1h4KzEFMXIkLSUijdUrYfWfm4SYPp1J15mq3WPyFvb9TvLxTtoOy-TVPDstLeYire4pHh0SX3VtB_brw6Rmal_4qCNYlzpOy7EVIp39qW1On0fIURWZYyP7ty-PS0U_0mYwxWkEE86vtgFeq9Yb5E7liXsukk-c7EBvK_ZUaprx1pSJc02rqS-0VGhd5FtmHf3vVkmmSvxreN8E=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "910606632").split()))
aiohttpsession = aiohttp.ClientSession()
