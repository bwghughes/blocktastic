import hashlib as hasher
import datetime as date

# Define what a Snakecoin block is
class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.nonce = 0
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(f"{self.index}{self.nonce}{self.timestamp}{self.data}{self.previous_hash}".encode("utf-8"))
    return sha.hexdigest()


  def mine(self):
    signed = False
    guesses = 0
    while signed == False:
        guesses = guesses + 1
        if self.hash.startswith("00000"):
            signed = True
        else:      
            self.nonce = self.nonce + 1
            self.hash = self.hash_block()
    else:
        return self

    def to_json(self):
        pass


# Generate genesis block
def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  block = Block(0, date.datetime.now(), "Genesis Block", "0")
  block.mine()
  return block

# Generate all later blocks in the blockchain
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  previous_hash = last_block.hash
  new_block = Block(this_index, this_timestamp, this_data, previous_hash)
  return new_block.mine()


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 1000

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
    # Tell everyone about it!
  print(f"Block added: {block_to_add.hash} after {block_to_add.nonce} attempts.")
  