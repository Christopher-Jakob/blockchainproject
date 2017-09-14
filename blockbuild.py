import datetime as date
from block import Block

def create_block_zero():

    # Create a zero block
    return Block(0, date.datetime.now(), "Block Zero", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Block" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index,this_timestamp, this_data, this_hash)

if __name__ == '__main__':

    # create block chain add zero block
    blockchain = [create_block_zero()]
    previous_block = blockchain[0]


    num_of_block_to_add = 20

    #add blocks to the chain
    for i in range(0, num_of_block_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        print ("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print ("Hash: {}\n".format(block_to_add.hash))