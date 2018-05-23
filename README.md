# pymongo-example-code
Example code showing the MongoDB Python driver (Pymongo) in action.

## Setting up the transactions code
The first example is for MongoDB 4.0 and shows the transactions code
in action. The ```transactions/setups.sh``` will setup your enviroment
including

* Downloading and installing MongoDB 4.0 RC0
* Setting up a python virtualenv
* Install the beta version of the Python MongoDB Driver (pymongo)
* Install mtools to allow easy starting of a [replica set](https://docs.mongodb.com/manual/tutorial/deploy-replica-set/)
(transactions require a replica set)
* start a replica set

All this is achieved using a single setup script. 

<pre>
<b>cd transactions</b>
<b>./setup.sh**</b>

<b>python transactions_main.py -h</b>
usage: transaction_main.py [-h] [--host HOST] [--usetxns] [--delay DELAY]
                           [--iterations ITERATIONS]

optional arguments:
  -h, --help                         show this help message and exit
  --host HOST                     MongoDB URI [default: mongodb://localhost:27017?replicaSet=txntest]
  --usetxns                         Use transactions [default: False]
  --delay DELAY                  Delay between two insertion events [default: 1.0]
  --iterations ITERATIONS   Run 3 iterations
  </pre>

## Running the examle
