import asyncio
import asyncpg
import json


def connect(username:str, password:str):
    con = asyncio.run(asyncpg.connect(host="localhost"))
    return con