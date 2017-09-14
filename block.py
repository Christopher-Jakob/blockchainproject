import hashlib as hash



# builds a block
class Block:

    #initialize the block
    def __init__(self, index, timestamp, data, previous_hash):
            self.index = index
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.hash_block()

    # SHA256 hash block
    def hash_block(self):
        sha = hash.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf-8'))

        return sha.hexdigest()
