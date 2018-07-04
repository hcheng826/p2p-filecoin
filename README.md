# p2p-filecoin
YouTube link: https://youtu.be/vCZUwQ8xl_s

## Part A. IPFS and Proof of Storage

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

## Part B. Blockchain_pow

### Prerequisites
1. go: (like part A)
2. boltdb: https://github.com/boltdb/bolt

To start using Bolt, install Go and run `go get`:

```sh
$ go get github.com/boltdb/bolt/...
```

### Step 1: Compile this little project

Just run `go build` to compile, and `./blockchain_pow` to generate the genesis block:

```sh
$ go build
$ ./blockchain_pow
```
### step 2: addblock or print 

There are two client cmd to use:
```sh
addblock -data BLOCK_DATA
printchain
```

## Part C. Blockchain_p2pNet

### Prerequisites
1. go: (like part A)
2. ipfs: (like part A)
3. go-spew: https://github.com/davecgh/go-spew 
4. go-ipfs-api: https://github.com/ipfs/go-ipfs-api
5. go-libp2p: https://github.com/libp2p/go-libp2p

install go-libp2p library might take more time than others,
this library couldn't just run `go get`, but need to be `make`,
there are more information in their github mentioned above.

### Step 0: running the ipfs
```sh
ipfs daemon
```

### Step 1: running the first node
To simplify this README tutorial, we just run this p2pNet in localhost:
(add `-secio` to build a safe handshake tunnel for each other)
```sh
go run main.go -l 10001 -secio
```

### Step 2: running the second node
```sh
go run main.go -l 10002 -d <given address in the instructions> -secio
```

### Step 3: running the third node
```sh
go run main.go -l 10003 -d <given address in the instructions> -secio
```

### Step n: ...
All the same, you can add multiple nodes from different IP,
but you need to modify the IP address in the < given address >

### After running up all nodes: add data(owner) or get data(miner)
There are 3 cmd:
```sh
add <your data>
get pin <data ipfs address>
get nopin <data ipfs address>
```
`pin/nopin` means a miner or just a client.

## Work Division
Please take a look at `WorkDivision.txt`