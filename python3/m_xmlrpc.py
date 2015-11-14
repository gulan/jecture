#!/usr/bin/env python3

import xmlrpc.server
import xmlrpc.client
import local_stack
import multiprocessing

def gen(m = xmlrpc.client):
    for i in dir(m):
        v = m.__dict__[i]
        if isinstance(v, int):
            print ("    assert %s.%s == %s" % (m.__name__, i, v))
            continue
        if v == None:
            print ("    assert %s.%s == %s" % (m.__name__, i, None))
            continue
        # print (i, type(m.__dict__[i]))

""" server module
class BaseHTTPRequestHandler
class CGIXMLRPCRequestHandler
class DocCGIXMLRPCRequestHandler
class DocXMLRPCRequestHandler
class DocXMLRPCServer
class Fault
class MultiPathXMLRPCServer
class ServerHTMLDoc
class SimpleXMLRPCDispatcher
class SimpleXMLRPCRequestHandler
class SimpleXMLRPCServer
class XMLRPCDocGenerator
function dumps
function gzip_decode
function gzip_encode
function list_public_methods
function loads
function resolve_dotted_attribute
"""

"""
WRAPPERS <class 'tuple'>
GzipDecodedResponse <class 'abc.ABCMeta'>

class Binary
class Boolean
class BytesIO
class DateTime
class Error
class ExpatParser
class Fault
class Marshaller
class MultiCall
class MultiCallIterator
class ProtocolError
class ResponseError
class SafeTransport
class Server
class ServerProxy
class Transport
class Unmarshaller
class boolean
class datetime

function dumps
function escape
function getparser
function gzip_decode
function gzip_encode
function loads
"""

def xmlrpc_00():
    assert xmlrpc.client.APPLICATION_ERROR == -32500
    assert xmlrpc.client.FastMarshaller == None
    assert xmlrpc.client.FastParser == None
    assert xmlrpc.client.FastUnmarshaller == None
    assert xmlrpc.client.INTERNAL_ERROR == -32603
    assert xmlrpc.client.INVALID_ENCODING_CHAR == -32702
    assert xmlrpc.client.INVALID_METHOD_PARAMS == -32602
    assert xmlrpc.client.INVALID_XMLRPC == -32600
    assert xmlrpc.client.MAXINT == 2147483647
    assert xmlrpc.client.METHOD_NOT_FOUND == -32601
    assert xmlrpc.client.MININT == -2147483648
    assert xmlrpc.client.NOT_WELLFORMED_ERROR == -32700
    assert xmlrpc.client.PARSE_ERROR == -32700
    assert xmlrpc.client.SERVER_ERROR == -32600
    assert xmlrpc.client.SYSTEM_ERROR == -32400
    assert xmlrpc.client.TRANSPORT_ERROR == -32300
    assert xmlrpc.client.UNSUPPORTED_ENCODING == -32701
    print ('xmlrpc_client_00')

def xmlrpc_03():
    # No docs on SimpleXMLRPCRequestHandler implementation. We do not
    # even know how to instanciate this class.
    rh = xmlrpc.server.SimpleXMLRPCRequestHandler
    """
    accept_encodings
    address_string
    aepattern
    date_time_string
    decode_request_content
    default_request_version
    disable_nagle_algorithm
    do_POST
    encode_threshold
    end_headers
    error_content_type
    error_message_format
    finish
    flush_headers
    handle
    handle_expect_100
    handle_one_request
    is_rpc_path_valid
    log_date_time_string
    log_error
    log_message
    log_request
    monthname
    parse_request
    protocol_version
    rbufsize
    report_404
    responses
    rpc_paths
    send_error
    send_header
    send_response
    send_response_only
    server_version
    setup
    sys_version
    timeout
    version_string
    wbufsize
    weekdayname
    """
    print ('xmlrpc_client_03')


def xmlrpc_04():
    
    class RH(xmlrpc.server.SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC2',)
        
    def server(port=8000):
        addr = ('localhost', port)
        ss = xmlrpc.server.SimpleXMLRPCServer(
            addr,
            # requestHandler = SimpleXMLRPCRequestHandler,   # Default
            requestHandler = RH, # Recomended
            # logRequests = True,
            logRequests = False,
            # allow_none = False,  # Default
            allow_none = True,
            encoding = None,
            bind_and_activate = True,
            use_builtin_types = False)
        
        ss.register_instance(local_stack.forth_stack())
        ss.serve_forever()
        
    def client(uri='http://localhost:8000'):
        sp = xmlrpc.client.ServerProxy(
            uri,
            transport=None,
            encoding=None,
            verbose=False,
            # allow_none=False,  # Default
            allow_none=True,
            use_datetime=False,
            use_builtin_types=False,
            # *, ?
            context=None)
        local_stack.test(sp)
        
    s = multiprocessing.Process(target=server)
    s.start()
    c = multiprocessing.Process(target=client)
    c.start()
    c.join()
    s.terminate()
    s.join()
    print ('xmlrpc_client_04')

def xmlrpc_01(): print ('xmlrpc_client_05')
def xmlrpc_02(): print ('xmlrpc_client_05')
def xmlrpc_05(): print ('xmlrpc_client_05')
def xmlrpc_06(): print ('xmlrpc_client_06')
def xmlrpc_07(): print ('xmlrpc_client_07')
def xmlrpc_08(): print ('xmlrpc_client_08')
def xmlrpc_09(): print ('xmlrpc_client_09')

if __name__ == '__main__':
    xmlrpc_00()
    # xmlrpc_03()
    xmlrpc_04()

