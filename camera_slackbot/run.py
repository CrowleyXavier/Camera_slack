# coding: utf-8

import sys
import logging
from slackbot.bot import Bot

sys.path.insert(0,".")
logging.getLogger().setLevel(logging.INFO)

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
