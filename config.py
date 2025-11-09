#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7161201979:AAH1yNFQcNFQOWgCwT2-byP_xyQLgofv4XQ")
    API_ID = int(os.environ.get("API_ID", "20937775"))
    API_HASH = os.environ.get("API_HASH", "a01276c8c21178e56c4a962b56203db7")
    AUTH_USERS = "5166775158"


