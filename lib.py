import hashlib
import re
from os import path
from datetime import datetime

COMMENTS_REGEX = re.compile("/\*.*?\*/")

def file_exist(filepath):
    return path.exists(filepath)

def get_now_str():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def gen_query_hash(sql):
    """Return hash of the given query after stripping all comments, line breaks
    and multiple spaces, and lower casing all text.

    TODO: possible issue - the following queries will get the same id:
        1. SELECT 1 FROM table WHERE column='Value';
        2. SELECT 1 FROM table where column='value';
    """
    sql = COMMENTS_REGEX.sub("", sql)
    sql = "".join(sql.split()).lower()
    return hashlib.md5(sql.encode('utf-8')).hexdigest()

def _job_lock_id(query_hash, data_source_id):
    return "query_hash_job:%s:%s" % (data_source_id, query_hash)