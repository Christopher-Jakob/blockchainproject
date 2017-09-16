import datetime as date
from uuid import uuid4
from block import Block

def create_block_zero():

    # Create a zero block
    return Block(0, date.datetime.now(), "VP", uuid4(), "fname", "lname", "ss", "DOB", 0)

def next_block(last_block, verification_process_ID, fname, lname, ss_num, DOB):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_verification_process_ID = verification_process_ID
    this_block_ID = uuid4()
    this_fname = fname
    this_lname = lname
    this_ss_num = ss_num
    this_DOB = DOB
    this_hash = last_block.hash
    return Block(this_index,this_timestamp, this_verification_process_ID, this_block_ID, this_fname, this_lname, this_ss_num, this_DOB, this_hash)

if __name__ == '__main__':

    # create block chain add zero block
    blockchain = [create_block_zero()]
    previous_block = blockchain[0]



    bool = True

    #add blocks to the chain
    while bool:
        verification_process_ID = input("Enter Verification Process ID: ")
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        ss_num = input ("Enter social security number: ")
        DOB = input("Enter date of birth: ")
        cont = input("Do you want to continue (y or n): ")

        bool = [True, False][cont == "n"]

        block_to_add = next_block(previous_block, verification_process_ID, fname, lname, ss_num, DOB)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        print ("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print ("Hash: {}\n".format(block_to_add.hash))