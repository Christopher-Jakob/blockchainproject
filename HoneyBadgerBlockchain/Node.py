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
		
		num = randint(0, 20)
		time.sleep(1)
		print("[Work ] Working to solve block... I will guess {}!\n".format(num))
		if num < 10:
			#you win... return new block
			print("I win? Sending block to the server")
			lastBlock = blockchain[-1]
			new_block = Block(int(lastBlock.index)+1, lastBlock.hash, date.datetime.now(), nodeID, num, uuid4())
			
			requests.post(server_url + "/addBlock",  json = new_block.toJSON())
			return
		#else, enter while loop again

if __name__ == "__main__":
	nodeID = startup()
	
	keep_working = True
	while(keep_working):
		work()