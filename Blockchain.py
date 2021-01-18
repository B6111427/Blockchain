import hashlib
class Block:
    def __init__(self,PrevBlockHash,BlockIndex,Tx):
        self.PrevBlockHash = PrevBlockHash
        self.BlockIndex = BlockIndex
        self.Tx = Tx
    def getHash(self):
        MerkleRoot = hashlib.sha256(self.Tx.encode())
        hashvalue = hashlib.sha256((self.PrevBlockHash + MerkleRoot.hexdigest()).encode())
        return hashvalue.hexdigest()

#Create Genesis Block
TxGenesis = [
    
]
GenesisBlock = Block("0",0,TxGenesis)
blockchain = []
blockchain.append(GenesisBlock)

def CreateBlock(PrevBlockHash,Tx):
    BlockIndex = len(blockchain)
    NewBlock = Block(PrevBlockHash,BlockIndex,Tx)
    
    blockchain.append(NewBlock)
    return NewBlock.getHash()

CreateBlock(blockchain[0].getHash(),"KUY")
print(blockchain[0].getHash())
print(blockchain[1].getHash())


