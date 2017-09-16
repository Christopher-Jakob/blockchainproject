# Honey Badgers
# Block Builder

#! Python3

import datetime as date
from uuid import uuid4
from block import Block

from xml.etree.ElementTree import ElementTree, Element
import xml.etree.ElementTree as ET
import sys

# creates zero block with arbitrary data
def create_block_zero():

    return Block(0, date.datetime.now(), "VP", uuid4(), "fname", "lname", "ss", "DOB", 0)

def next_block(last_block, verification_process_ID, fname, lname, ss_num, DOB):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_verification_process_ID = verification_process_ID
    this_block_ID = uuid4()
    # print(this_block_ID)
    this_fname = fname
    this_lname = lname
    this_ss_num = ss_num
    this_DOB = DOB
    this_hash = last_block.hash
    return Block(this_index,this_timestamp, this_verification_process_ID, this_block_ID, this_fname, this_lname, this_ss_num, this_DOB, this_hash)

#iterates through block chain list and then writes to an XML file.
def build_xml(blockchain):

    op = ''

    for i in range(1, len(blockchain)):

        block = blockchain[i]

        root = Element('Block')
        tree = ElementTree(root)
        root.set('ID', str(block.block_ID))


        index = Element('index')
        root.append(index)
        index.text = str(block.index)

        timestamp = Element('timestamp')
        root.append(timestamp)
        timestamp.text = str(block.timestamp)

        verification_process_ID = Element('verification_process_ID')
        root.append(verification_process_ID)
        verification_process_ID.text = str(block.verification_process_ID)

        # block_ID = Element('block_ID')
        # block_ID.text = block.block_ID

        fname = Element('fname')
        root.append(fname)
        fname.text = str(block.fname)

        lname = Element('lname')
        root.append(lname)
        lname.text = str(block.lname)

        ss_num = Element('ss_num')
        root.append(ss_num)
        ss_num.text = str(block.ss_num)

        DOB = Element('DOB')
        root.append(DOB)
        DOB.text = str(block.DOB)

        # tree.write(open('blocks.xml', 'w'), encoding="unicode")
        u = str(ET.tostring(root), "utf-8")
        op = op + u

    with open('blocks.xml', 'w') as f:
        f.write(op)



if __name__ == '__main__':

    # create block chain add zero block
    blockchain = [create_block_zero()]
    previous_block = blockchain[0]


    bool = True

    # while user still typing, add blocks to the chain
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


    build_xml(blockchain)