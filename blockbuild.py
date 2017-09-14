import datetime as date
from block import Block

def create_block_zero():
    return Block(0, date.datetime.now(), "Block Zero", "0")
