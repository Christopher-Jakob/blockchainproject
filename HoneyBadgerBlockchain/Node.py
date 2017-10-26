import requests
import json
import time
from random import randint
import datetime as date
import pickle
from uuid import uuid4

from block import Block

server_url = "http://localhost:5000"
blockchain = []
nodeID = 0

def startup():
	#get starting blockchain
	nodeID = int(requests.get(server_url + "/newNode").content)

	print('''Connection Established... 
	Node {} will start working...'''.format(nodeID))
	return nodeID
	
def work():
	while(1):
		#Make sure we work on the most current ledger...
		blocks = requests.get(server_url + "/getBlockchain").content
		
		blockchain = pickle.loads(blocks)
		
		#print("Doing work on these blocks: {}".format(blockchain))
		#save into blockchain array
		
		#Work should somehow have to do with hashing of the most recent block right?
		
		num = randint(0, 20)
		time.sleep(1)
		print("working to solve block... I will guess {}!\n".format(num))
		if num < 10:
			#you win... return new block
			print("Sending block to the guy... I am Node {}".format(nodeID))
			#instead of meaningless JSON... this needs to be a python Block object. 
			lastBlock = blockchain[-1]
			new_block = Block(int(lastBlock.index)+1, lastBlock.hash, date.datetime.now(), nodeID, num, uuid4())	#increment the index, give this NodeID, put the prev Block Hash
			
			requests.post(server_url + "/addBlock",  json = new_block.toJSON())
			return
		#else, enter while loop again

if __name__ == "__main__":
	#run code stuffs
	nodeID = startup()
	
	keep_working = True
	while(keep_working):
		
		work()