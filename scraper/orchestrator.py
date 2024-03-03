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

config = yaml.load(config_path)

db_options = {
    "sqlite": lambda config: sqlite3.connect(**config["sqlite"])
}

cache_options = {
    "redis": lambda config: redis.Redis(**config["redis"])
}


def create_article_table_sqlite(
        db: sqlite3.Connection,
        config: dict
):
    """Creates tables to store the articles in for all sites

    Args:
        db (sqlite3.Connection): sqlite connection to the database.
        config (dict): configuration dictionary with `sites` key and
        dict value where each key is a site and each value is a dict
        of column names and their properties.
    """

    # db.execute("drop table if exists article")
    db.commit()

    # for each news website
    for site, pairs in config["sites"].items():
        sql_command = "create table if not exists article_"
        sql_command += site + " (\n"

        cols = []
        # for each table column
        for key, value in pairs.items():
            col = "\t" + key + " " + value
            col += ",\n" if len(cols) - 1 < len(pairs) else ");"

    db.commit()

# endregion init


# 1. Date sequence generator

# newsam
    
initial_date = datetime.datetime(2009, 6, 25)
on_date = initial_date

while on_date <= datetime.datetime.now():
    print(on_date.year, end="\r")
    r.lpush("to_fetch_list_newsam", f"{on_date.year}/{on_date.month}/{on_date.day}/")
    on_date += datetime.timedelta(1)


# tertam
    
initial_date = datetime.datetime(2010, 3, 2)
on_date = initial_date

while on_date <= datetime.datetime.now():
    print(on_date.year, end="\r")
    r.lpush("to_fetch_list_tertam", on_date.strftime("%Y/%m/%d"))
    on_date += datetime.timedelta(1)


# armenpress
    
lastid = 3279

while True:
    article_ids, timestamps = get_article_list(lastid)

    if len(article_ids) == 0:
        break
    lastid += 1

    [insert_article(article_ids[i], None, timestamps[i], None, None, False) for i in range(len(article_ids))]
    db.commit()
    # time.sleep(0.15)
    print(lastid, end="\r")

# 2. Article info storer

# 3. Content scraping assigner