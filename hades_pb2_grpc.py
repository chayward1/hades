# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hades_pb2 as hades__pb2


class ZoneInfoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_stream(
                '/hades.ZoneInfo/Read',
                request_serializer=hades__pb2.Zone.SerializeToString,
                response_deserializer=hades__pb2.Zone.FromString,
                )
        self.Write = channel.unary_unary(
                '/hades.ZoneInfo/Write',
                request_serializer=hades__pb2.Zone.SerializeToString,
                response_deserializer=hades__pb2.Zone.FromString,
                )


class ZoneInfoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ZoneInfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_stream_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=hades__pb2.Zone.FromString,
                    response_serializer=hades__pb2.Zone.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=hades__pb2.Zone.FromString,
                    response_serializer=hades__pb2.Zone.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hades.ZoneInfo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ZoneInfo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/hades.ZoneInfo/Read',
            hades__pb2.Zone.SerializeToString,
            hades__pb2.Zone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hades.ZoneInfo/Write',
            hades__pb2.Zone.SerializeToString,
            hades__pb2.Zone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
