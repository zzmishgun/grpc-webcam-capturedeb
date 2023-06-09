# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import image_pb2 as image__pb2


class ImageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SaveImage = channel.unary_unary(
                '/ImageService/SaveImage',
                request_serializer=image__pb2.ImageRequest.SerializeToString,
                response_deserializer=image__pb2.ImageResponse.FromString,
                )


class ImageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SaveImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SaveImage': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveImage,
                    request_deserializer=image__pb2.ImageRequest.FromString,
                    response_serializer=image__pb2.ImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SaveImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageService/SaveImage',
            image__pb2.ImageRequest.SerializeToString,
            image__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
