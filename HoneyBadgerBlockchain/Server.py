'''
Blockchain internal server by HoneyBadgerMedSolution
11_06_2017 
'''
from flask import Flask, request, jsonify
import datetime as date
from block import Block
import pickle
from collections import deque
import json
from uuid import uuid4

nodes = []
blockchain = []
unverifiedBlocks = deque()

unverifiedBlocks.append({
							"firstname" : "Joe",
							"lastname" : "Smith",
							"dob" : "1/2/90",
							"ssn" : "123456789",
							"allergies" : ["doggos", "advil"],
							"symptoms" : ["itchy elbow", "stuffy nose"]
							})

app = Flask(__name__)

def CreateFirstBlock():
	return Block(-1, 0, date.datetime.now(), -1, 0, uuid4())	
	
@app.route("/newNode", methods=["GET"])
def NewNode():
	node_url = request.remote_addr
	nodes.append(node_url)
	if len(blockchain) == 0:
		blockchain.append(CreateFirstBlock())
	
	nodeID = len(nodes)
	print("[NewNode ] A new Node has joined! nodeID = {}".format(nodeID))
	return str(nodeID)	#Return a unique ID to represent the new Node.
	
@app.route("/addBlock", methods=["POST"])
def AddBlock():
	
	blockJSON = request.get_json()
	new_block = Block.fromJSON(blockJSON)
	
	#check for duplicate by comparing hash
	last_block = blockchain[-1]
	if last_block.hash == new_block.hash:
		#don't add, return blockchain
		print("[AddBlock] Duplicate found! No Block added.")
		return(pickle.dumps(blockchain))
	
	#check proof of work field of the block to verify
	if int(new_block.proof_of_work) < 0:
		return "stop cheating"
	if not int(new_block.proof_of_work) < 10:		#set the requirement for work here.
		return "stop cheating"
		
	
	if unverifiedBlocks:
		new_block.setData(unverifiedBlocks.popleft())
	else:
		print("[AddBlock] There is no data to add")
		return ""
		
	
	
	blockchain.append(new_block)
	print("[AddBlock] Block added to the chain: {}".format(new_block.toJSON()))
	print(new_block)
	
	WriteBlockchainToFile()
	
	return ""	#return empty string
	
	
@app.route("/getBlockchain", methods=["GET"])
def GetBlockchain():
	#simply send the current blockchain ledger to a Node. 
	return pickle._dumps(blockchain)

	
def ToJSON():
	jsonChain = []
	for b in blockchain:
		jsonChain.append(b.toJSON())
	return jsonChain
	
def WriteBlockchainToFile():
	with open('Blockchain.json', 'w') as outfile:
		json.dump(ToJSON(), outfile)


def ReadFromJSON():
	blockchain = []
	data = []
	try:
		with open('Blockchain.json') as infile:
			data = json.load(infile)
			for i in data:
				blockchain.append(Block.fromJSON(i))
			return blockchain
	except:
		print("[Startup ] No File Blockchain.json found")
		return blockchain

'''
Begin Code for Front end requests
'''

@app.route("/getAllRecords", methods=["GET"])
def GetAllRecords():
	#convert blockchain list to JSON
	jsonChain = []
	for b in blockchain:
		jsonChain.append(b.toJSON())
	return str(jsonChain).replace("'", '"')

@app.route("/getByName", methods=["GET"])
def GetByName():
	last_name = request.args.get('lastname')
	first_name = request.args.get('firstname')

	#find blocks with data containing patient name
	jsonChain = []
	for block in blockchain:
		data = block.data
		if 'lastname' in data and 'firstname' in data:
			try:
				data = json.loads(block.data.replace("'", '"'))		#JSON likes " but not '
			except:
				pass
			if data['lastname'] == last_name:
				if data['firstname'] == first_name:
					jsonChain.append(block.toJSON())
	return str(jsonChain).replace("'", '"')
	
@app.route("/getBySSN", methods=["GET"])
def GetBySSN():
	ssn = request.args.get('SSN')

	#find blocks with data containing patient SSN
	jsonChain = []
	for block in blockchain:
		data = block.data
		if 'ssn' in data:
			try:
				data = json.loads(block.data.replace("'", '"'))		#JSON likes " not '
			except:
				pass
			if data['ssn'] == ssn:
				jsonChain.append(block.toJSON())
	return str(jsonChain).replace("'", '"')
	
@app.route("/addRecord", methods=["POST"])
def AddRecord():
	#do some check to make sure the record is formatted a certain way or has proper credentials. 
	data = request.get_json(force=True)		#force interpretation as a JSON input
	unverifiedBlocks.append(data)
	print("[PostReq ] Data added to Queue: {}".format(data))
	
	return "Data Added to Queue"
	
#@app.route("/editRecord", methods=["POST"])
#def EditRecord():
#	#search to find data record, copy that data and edit it... add to the queue	
#	return "Not yet implemented"
	
	
if __name__ == "__main__":
	blockchain = ReadFromJSON()
	app.run(threaded = True)