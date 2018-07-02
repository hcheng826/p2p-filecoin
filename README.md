# p2p-filecoin
## IPFS and Proof of Storage
### Prerequisites
1. go: https://golang.org/dl/
2. ipfs: https://ipfs.io/
3. python3 socket packge
make sure you add exacutive files "go" and "ipfs" to $PATH variable so you can execute them using command line
### Step 1: Setup a private network of IPFS
refer to: https://medium.com/@chunyu.hsiao93/ipfs-private-network-%E7%A7%81%E6%9C%89%E7%B6%B2%E8%B7%AF-8d8748cba7b2
and make sure your machines are linked on IPFS (ipfs swarm peers)
Remeber to modify the IPs in "owner.py" and ipfs_id in "miner.py" and "badminer.py"
### Step 2: IPFS File Transmission and Proof of Storage
On the machine which you want to be good miner, run
```
python3 miner.py
```
On the machine which you want to be bad miner, run
```
python3 badminer.py
```
On the machine which you want to be owner, create file to be added and modify the filename in "owner.py"
Run
```
python3 owner.py
```
And you can see the output