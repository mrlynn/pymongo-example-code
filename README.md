# pymongo-example-code
Example code showing the MongoDB Python driver (Pymongo) in action.

The first example is for MongoDB 4.0 and shows the transactions code
in action.

```
cd transactions
./setup.sh

python transactions_main.py -h
usage: transaction_main.py [-h] [--host HOST] [--usetxns] [--delay DELAY]
                           [--iterations ITERATIONS]

optional arguments:
  -h, --help                         show this help message and exit
  --host HOST                     MongoDB URI [default: mongodb://localhost:27017?replicaSet=txntest]
  --usetxns                         Use transactions [default: False]
  --delay DELAY                  Delay between two insertion events [default: 1.0]
  --iterations ITERATIONS   Run 3 iterations
```
