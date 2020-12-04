import argparse
import lib

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Query absolute file path.")
parser.add_argument("datasourceid", help="the query target data source if.")
parser.parse_args()

args = parser.parse_args()
filepath = args.path
data_source_id = args.datasourceid

if not filepath:
    raise Exception("filepath is required (must be absolute path)")

if not data_source_id:
    raise Exception("data_source_id is required")

if not lib.file_exist(filepath):
    raise Exception("file not found")

print(lib.get_now_str() + ": file " + filepath + " found")

print(lib.get_now_str() + ": loading the file")
f = open(filepath, "r")
content = f.read()
f.close()

print(lib.get_now_str() + ": getting hash")
query_hash = lib.gen_query_hash(content)

print(lib.get_now_str() + ": getting jobid")
job_lock_id = lib._job_lock_id(query_hash, data_source_id)

print(lib.get_now_str() + " resut:\nquery_hash: " + query_hash + "\njob_lock_id: " + job_lock_id)