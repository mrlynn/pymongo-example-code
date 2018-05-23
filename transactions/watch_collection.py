
import pymongo
from argparse import ArgumentParser
from datetime import datetime

if __name__ == "__main__" :

    parser = ArgumentParser()

    parser.add_argument( "--host", default="mongodb://localhost:27017", help="mongodb URI for connecting to server [default: %(default)s]")
    parser.add_argument( "--watch", default="test.test", help="Watch <database.colection> [default: %(default)s]")

    args = parser.parse_args()

    client = pymongo.MongoClient( host=args.host)

    ( database_name, dot, collection_name ) = args.watch.partition( ".")

    database = client[database_name]
    collection = database[collection_name]

    watch_cursor = collection.watch()
    output = database["watcher"]
    try:
        print( "Watching: {}".format(args.watch))
        for d in watch_cursor:
            print( "time now:{}".format(datetime.utcnow()))
            print("cluster time : {}".format(d["clusterTime"].as_datetime()))
            print("collection   : {}".format(d["ns"]))
            print("seat         : {}".format(d["fullDocument"]["seat"]) )
            #print(d)
            output.insert_one(d)
    except KeyboardInterrupt:
        print("Closing watch cursor")
        watch_cursor.close()
        print("exiting...")

