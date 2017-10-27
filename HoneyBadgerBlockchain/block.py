# Honey Badgers
# Block Class

#! Python3

import hashlib as hash
from uuid import uuid4


# builds a block
class Block:

	#Constructor with default values.
	def __init__(self, index, lastHash, time, verificationProcessID, proof_of_work, blockID, data="dummy data", hash=0):
		self.index = int(index)
		self.timestamp = time
		self.previous_hash = lastHash
		self.verification_process_ID = verificationProcessID
		self.proof_of_work = proof_of_work
		self.block_ID = blockID
		self.data = data
		if hash==0:
			self.hash = self.hash_block()
		else:
			self.hash = hash

	# SHA256 hash block
	def hash_block(self):
		sha = hash.sha256()
		sha.update((str(self.index) + str(self.timestamp) + str(self.verification_process_ID) + str(self.block_ID) + str(self.data) +
			str(self.previous_hash)).encode('utf-8'))
		return sha.hexdigest()
		
	def toJSON(self):
		#create and return a JSON representation of this block
		json = {"index": str(self.index),
				"time": str(self.timestamp),
				"prevHash": str(self.previous_hash),
				"nodeID" : str(self.verification_process_ID),
				"proof" : str(self.proof_of_work),
				"blockID" : str(self.block_ID),
				"hash" : str(self.hash),
				"data" : str(self.data)}
		return json
		
	def fromJSON(blockJSON):
		if "data" in blockJSON:
			data = blockJSON["data"]
		else:
			data = "dummy data"
		
		return Block(blockJSON['index'], 
			blockJSON['prevHash'], 
			blockJSON['time'], 
			blockJSON['nodeID'],
			blockJSON['proof'],
			blockJSON['blockID'],
			blockJSON['data'],
			blockJSON['hash']
			)
			
	def getData(self):
		return self.data
		
	def setData(self, data):
		self.data = data