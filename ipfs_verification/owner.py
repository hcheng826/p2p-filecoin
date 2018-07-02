from ipfs import Owner

HOST1 = 'ip1'   # change to ip of one of your miners
HOST2 = 'ip2'   # change to ip of one of your miners
PORT = 12345

myOwner = Owner([(HOST1, PORT), (HOST2, PORT)])
print(myOwner.minerList)
myOwner.add_file('foo') # edit to the filename you want to add to ipfs
print(myOwner.minerList)

myOwner.miner_filecheck()
