import time
import grpc
import uuid
import board
import argparse
import adafruit_dht

import hades_pb2
import hades_pb2_grpc

# TODO Declare options.
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default='localhost:50051')
parser.add_argument('-n', '--name', default=uuid.uuid4())
parser.add_argument('-s', '--sensor', default=11)
parser.add_argument('-d', '--delay', default=1)

# TODO Parse arguments.
args = parser.parse_args()

# TODO Connect to GPIO headers.
dht = None
if args.sensor == '11':
    dht = adafruit_dht.DHT22(board.D2)
else:
    dht = adafruit_dht.DHT11(board.D6)

# TODO Connect to service.
with grpc.insecure_channel(args.addr) as channel:
    stub = hades_pb2_grpc.ZoneInfoStub(channel)
    running = True

    # TODO Run the application.
    while running:
        try:
            # TODO Read the temperature and humidity.
            t = dht.temperature
            h = dht.humidity

            # TODO Write the data to the server.
            response = stub.Write(hades_pb2.Zone(name=args.name,
                                                 temperature=int(t),
                                                 humidity=int(h)))
        except RuntimeError:
            # TODO Client side error handling.
            pass

        finally:
            # TODO Sleep until next cycle.
            time.sleep(args.delay)
