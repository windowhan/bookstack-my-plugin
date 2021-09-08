from common.datastruct import *
from common.lib import *

from history.lib import *

from util import *

config = readConfig("./config.json")
token = BookStackToken(tid=config["token_id"], secret=config["token_secret"], name=config["bot_name"], host=config["host_url"])
reqManager = RequestManager(token)

historyManager = HistoryManager(reqManager)
historyManager.updateCompleteHistory()
