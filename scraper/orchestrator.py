# region imports

import numpy as np
import pandas as pd
import requests
import re
import sqlite3
import time
import openai
import redis
import datetime
import json
import yaml

# endregion imports

# region init

config_path = "config.yaml"

with open(config_path, "w") as f:
    yaml.dump({
        "redis": {
            "host": "localhost",
            "port": 5211
        },
        "sqlite": {
            "path": "scraping.db"
        }
    }, f)

# config = yaml.load(config_path)
# print(config)

# r = redis.Redis("localhost")

# endregion init


# 1. Date sequence generator




# 2. Article info storer

# 3. Content scraping assigner