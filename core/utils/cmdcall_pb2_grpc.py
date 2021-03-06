# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
try:
    from utils import cmdcall_pb2 as cmdcall__pb2
except:
    import cmdcall_pb2 as cmdcall__pb2


class CmdCallStub(object):

    def __init__(self, channel):
        """Constructor.
    
        Args:
          channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
            '/cmdcall.CmdCall/Call',
            request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
            response_deserializer=cmdcall__pb2.CallResponse.FromString,
            )
        self.CallWithResult = channel.unary_unary(
            '/cmdcall.CmdCall/CallWithResult',
            request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
            response_deserializer=cmdcall__pb2.CallResponse.FromString,
            )
        self.CallAndTransferXmlToJson = channel.unary_unary(
            '/cmdcall.CmdCall/CallAndTransferXmlToJson',
            request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
            response_deserializer=cmdcall__pb2.CallResponse.FromString,
            )
        self.CallAndSplitKVToJson = channel.unary_unary(
            '/cmdcall.CmdCall/CallAndSplitKVToJson',
            request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
            response_deserializer=cmdcall__pb2.CallResponse.FromString,
            )


class CmdCallServicer(object):

    def Call(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    
    def CallWithResult(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    
    def CallAndTransferXmlToJson(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
    
    def CallAndSplitKVToJson(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CmdCallServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Call': grpc.unary_unary_rpc_method_handler(
            servicer.Call,
            request_deserializer=cmdcall__pb2.CallRequest.FromString,
            response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
        ),
        'CallWithResult': grpc.unary_unary_rpc_method_handler(
            servicer.CallWithResult,
            request_deserializer=cmdcall__pb2.CallRequest.FromString,
            response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
        ),
        'CallAndTransferXmlToJson': grpc.unary_unary_rpc_method_handler(
            servicer.CallAndTransferXmlToJson,
            request_deserializer=cmdcall__pb2.CallRequest.FromString,
            response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
        ),
        'CallAndSplitKVToJson': grpc.unary_unary_rpc_method_handler(
            servicer.CallAndSplitKVToJson,
            request_deserializer=cmdcall__pb2.CallRequest.FromString,
            response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'cmdcall.CmdCall', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
