from ipfs import Miner, BadMiner

HOST = '0.0.0.0'
PORT = 12345
# change your ipfs id, it is something like '/ip4/140.112.21.80/tcp/4001/ipfs/QmT8izcWryGoN9FAPjvxckn7KtqXQxGLsW5eeXLShocqpQ'
# use command 'ipfs id' at your command line after ipfs daemon is turned on the get the ipfs id
ipfs_id = 'your ipfs id'
myMiner = BadMiner(HOST, PORT, ipfs_id)
myMiner.listen()
