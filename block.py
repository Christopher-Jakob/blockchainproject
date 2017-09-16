# Honey Badgers
# Block Class

#! Python3

import hashlib as hash


# builds a block
class Block:

    #initialize the block
    def __init__(self, index, timestamp, verification_process_ID, block_ID, fname, lname, ss_num, DOB, previous_hash):
            self.index = index
            self.timestamp = timestamp
            self.verification_process_ID = verification_process_ID
            self.block_ID = block_ID
            self.fname = fname
            self.lname = lname
            self.ss_num = ss_num
            self.DOB = DOB

            self.previous_hash = previous_hash
            self.hash = self.hash_block()



    # SHA256 hash block
    def hash_block(self):
        sha = hash.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.verification_process_ID) +
                    str(self.block_ID) +
                    str(self.fname) +
                    str(self.lname) +
                    str(self.ss_num) +
                    str(self.DOB) +
                    str(self.previous_hash)).encode('utf-8'))

        return sha.hexdigest()


