#!/usr/bin/env python3

import multiprocessing
import socket

def gen(m = socket):
    for i in dir(m):
        v = m.__dict__[i]
        if isinstance(v, int):
            # print ("    assert %s.%s == %s" % (m.__name__, i, v))
            continue
        if v == None:
            # print ("    assert %s.%s == %s" % (m.__name__, i, None))
            continue
        # print (i, type(m.__dict__[i]))
        print (type(m.__dict__[i]), i)

"""
<class 'PyCapsule'> CAPI
<class 'abc.ABCMeta'> SocketIO
<class 'enum.EnumMeta'> AddressFamily
<class 'enum.EnumMeta'> IntEnum
<class 'enum.EnumMeta'> SocketKind
<class 'function'> _intenum_converter
<class 'function'> create_connection
<class 'function'> fromfd
<class 'function'> getaddrinfo
<class 'function'> getfqdn
<class 'function'> socketpair
<class 'object'> _GLOBAL_DEFAULT_TIMEOUT
"""

def socket_00():
    assert socket.AF_APPLETALK == socket.AddressFamily.AF_APPLETALK
    assert socket.AF_ASH == socket.AddressFamily.AF_ASH
    assert socket.AF_ATMPVC == socket.AddressFamily.AF_ATMPVC
    assert socket.AF_ATMSVC == socket.AddressFamily.AF_ATMSVC
    assert socket.AF_AX25 == socket.AddressFamily.AF_AX25
    assert socket.AF_BRIDGE == socket.AddressFamily.AF_BRIDGE
    assert socket.AF_CAN == socket.AddressFamily.AF_CAN
    assert socket.AF_DECnet == 12
    assert socket.AF_ECONET == socket.AddressFamily.AF_ECONET
    assert socket.AF_INET == socket.AddressFamily.AF_INET
    assert socket.AF_INET6 == socket.AddressFamily.AF_INET6
    assert socket.AF_IPX == socket.AddressFamily.AF_IPX
    assert socket.AF_IRDA == socket.AddressFamily.AF_IRDA
    assert socket.AF_KEY == socket.AddressFamily.AF_KEY
    assert socket.AF_LLC == socket.AddressFamily.AF_LLC
    assert socket.AF_NETBEUI == socket.AddressFamily.AF_NETBEUI
    assert socket.AF_NETLINK == socket.AddressFamily.AF_ROUTE
    assert socket.AF_NETROM == socket.AddressFamily.AF_NETROM
    assert socket.AF_PACKET == socket.AddressFamily.AF_PACKET
    assert socket.AF_PPPOX == socket.AddressFamily.AF_PPPOX
    assert socket.AF_RDS == socket.AddressFamily.AF_RDS
    assert socket.AF_ROSE == socket.AddressFamily.AF_ROSE
    assert socket.AF_ROUTE == socket.AddressFamily.AF_ROUTE
    assert socket.AF_SECURITY == socket.AddressFamily.AF_SECURITY
    assert socket.AF_SNA == socket.AddressFamily.AF_SNA
    assert socket.AF_TIPC == socket.AddressFamily.AF_TIPC
    assert socket.AF_UNIX == socket.AddressFamily.AF_UNIX
    assert socket.AF_UNSPEC == socket.AddressFamily.AF_UNSPEC
    assert socket.AF_WANPIPE == socket.AddressFamily.AF_WANPIPE
    assert socket.AF_X25 == socket.AddressFamily.AF_X25
    assert socket.AI_ADDRCONFIG == 32
    assert socket.AI_ALL == 16
    assert socket.AI_CANONNAME == 2
    assert socket.AI_NUMERICHOST == 4
    assert socket.AI_NUMERICSERV == 1024
    assert socket.AI_PASSIVE == 1
    assert socket.AI_V4MAPPED == 8
    assert socket.CAN_BCM == 2
    assert socket.CAN_BCM_RX_CHANGED == 12
    assert socket.CAN_BCM_RX_DELETE == 6
    assert socket.CAN_BCM_RX_READ == 7
    assert socket.CAN_BCM_RX_SETUP == 5
    assert socket.CAN_BCM_RX_STATUS == 10
    assert socket.CAN_BCM_RX_TIMEOUT == 11
    assert socket.CAN_BCM_TX_DELETE == 2
    assert socket.CAN_BCM_TX_EXPIRED == 9
    assert socket.CAN_BCM_TX_READ == 3
    assert socket.CAN_BCM_TX_SEND == 4
    assert socket.CAN_BCM_TX_SETUP == 1
    assert socket.CAN_BCM_TX_STATUS == 8
    assert socket.CAN_EFF_FLAG == 2147483648
    assert socket.CAN_EFF_MASK == 536870911
    assert socket.CAN_ERR_FLAG == 536870912
    assert socket.CAN_ERR_MASK == 536870911
    assert socket.CAN_RAW == 1
    assert socket.CAN_RAW_ERR_FILTER == 2
    assert socket.CAN_RAW_FD_FRAMES == 5
    assert socket.CAN_RAW_FILTER == 1
    assert socket.CAN_RAW_LOOPBACK == 3
    assert socket.CAN_RAW_RECV_OWN_MSGS == 4
    assert socket.CAN_RTR_FLAG == 1073741824
    assert socket.CAN_SFF_MASK == 2047
    assert socket.EAGAIN == 11
    assert socket.EAI_ADDRFAMILY == -9
    assert socket.EAI_AGAIN == -3
    assert socket.EAI_BADFLAGS == -1
    assert socket.EAI_FAIL == -4
    assert socket.EAI_FAMILY == -6
    assert socket.EAI_MEMORY == -10
    assert socket.EAI_NODATA == -5
    assert socket.EAI_NONAME == -2
    assert socket.EAI_OVERFLOW == -12
    assert socket.EAI_SERVICE == -8
    assert socket.EAI_SOCKTYPE == -7
    assert socket.EAI_SYSTEM == -11
    assert socket.EBADF == 9
    assert socket.EWOULDBLOCK == 11
    assert socket.INADDR_ALLHOSTS_GROUP == 3758096385
    assert socket.INADDR_ANY == 0
    assert socket.INADDR_BROADCAST == 4294967295
    assert socket.INADDR_LOOPBACK == 2130706433
    assert socket.INADDR_MAX_LOCAL_GROUP == 3758096639
    assert socket.INADDR_NONE == 4294967295
    assert socket.INADDR_UNSPEC_GROUP == 3758096384
    assert socket.IPPORT_RESERVED == 1024
    assert socket.IPPORT_USERRESERVED == 5000
    assert socket.IPPROTO_AH == 51
    assert socket.IPPROTO_DSTOPTS == 60
    assert socket.IPPROTO_EGP == 8
    assert socket.IPPROTO_ESP == 50
    assert socket.IPPROTO_FRAGMENT == 44
    assert socket.IPPROTO_GRE == 47
    assert socket.IPPROTO_HOPOPTS == 0
    assert socket.IPPROTO_ICMP == 1
    assert socket.IPPROTO_ICMPV6 == 58
    assert socket.IPPROTO_IDP == 22
    assert socket.IPPROTO_IGMP == 2
    assert socket.IPPROTO_IP == 0
    assert socket.IPPROTO_IPIP == 4
    assert socket.IPPROTO_IPV6 == 41
    assert socket.IPPROTO_NONE == 59
    assert socket.IPPROTO_PIM == 103
    assert socket.IPPROTO_PUP == 12
    assert socket.IPPROTO_RAW == 255
    assert socket.IPPROTO_ROUTING == 43
    assert socket.IPPROTO_RSVP == 46
    assert socket.IPPROTO_SCTP == 132
    assert socket.IPPROTO_TCP == 6
    assert socket.IPPROTO_TP == 29
    assert socket.IPPROTO_UDP == 17
    assert socket.IPV6_CHECKSUM == 7
    assert socket.IPV6_DSTOPTS == 59
    assert socket.IPV6_HOPLIMIT == 52
    assert socket.IPV6_HOPOPTS == 54
    assert socket.IPV6_JOIN_GROUP == 20
    assert socket.IPV6_LEAVE_GROUP == 21
    assert socket.IPV6_MULTICAST_HOPS == 18
    assert socket.IPV6_MULTICAST_IF == 17
    assert socket.IPV6_MULTICAST_LOOP == 19
    assert socket.IPV6_NEXTHOP == 9
    assert socket.IPV6_PKTINFO == 50
    assert socket.IPV6_RECVDSTOPTS == 58
    assert socket.IPV6_RECVHOPLIMIT == 51
    assert socket.IPV6_RECVHOPOPTS == 53
    assert socket.IPV6_RECVPKTINFO == 49
    assert socket.IPV6_RECVRTHDR == 56
    assert socket.IPV6_RECVTCLASS == 66
    assert socket.IPV6_RTHDR == 57
    assert socket.IPV6_RTHDRDSTOPTS == 55
    assert socket.IPV6_RTHDR_TYPE_0 == 0
    assert socket.IPV6_TCLASS == 67
    assert socket.IPV6_UNICAST_HOPS == 16
    assert socket.IPV6_V6ONLY == 26
    assert socket.IP_ADD_MEMBERSHIP == 35
    assert socket.IP_DEFAULT_MULTICAST_LOOP == 1
    assert socket.IP_DEFAULT_MULTICAST_TTL == 1
    assert socket.IP_DROP_MEMBERSHIP == 36
    assert socket.IP_HDRINCL == 3
    assert socket.IP_MAX_MEMBERSHIPS == 20
    assert socket.IP_MULTICAST_IF == 32
    assert socket.IP_MULTICAST_LOOP == 34
    assert socket.IP_MULTICAST_TTL == 33
    assert socket.IP_OPTIONS == 4
    assert socket.IP_RECVOPTS == 6
    assert socket.IP_RECVRETOPTS == 7
    assert socket.IP_RETOPTS == 7
    assert socket.IP_TOS == 1
    assert socket.IP_TRANSPARENT == 19
    assert socket.IP_TTL == 2
    assert socket.MSG_CMSG_CLOEXEC == 1073741824
    assert socket.MSG_CONFIRM == 2048
    assert socket.MSG_CTRUNC == 8
    assert socket.MSG_DONTROUTE == 4
    assert socket.MSG_DONTWAIT == 64
    assert socket.MSG_EOR == 128
    assert socket.MSG_ERRQUEUE == 8192
    assert socket.MSG_FASTOPEN == 536870912
    assert socket.MSG_MORE == 32768
    assert socket.MSG_NOSIGNAL == 16384
    assert socket.MSG_OOB == 1
    assert socket.MSG_PEEK == 2
    assert socket.MSG_TRUNC == 32
    assert socket.MSG_WAITALL == 256
    assert socket.NETLINK_DNRTMSG == 14
    assert socket.NETLINK_FIREWALL == 3
    assert socket.NETLINK_IP6_FW == 13
    assert socket.NETLINK_NFLOG == 5
    assert socket.NETLINK_ROUTE == 0
    assert socket.NETLINK_USERSOCK == 2
    assert socket.NETLINK_XFRM == 6
    assert socket.NI_DGRAM == 16
    assert socket.NI_MAXHOST == 1025
    assert socket.NI_MAXSERV == 32
    assert socket.NI_NAMEREQD == 8
    assert socket.NI_NOFQDN == 4
    assert socket.NI_NUMERICHOST == 1
    assert socket.NI_NUMERICSERV == 2
    assert socket.PACKET_BROADCAST == 1
    assert socket.PACKET_FASTROUTE == 6
    assert socket.PACKET_HOST == 0
    assert socket.PACKET_LOOPBACK == 5
    assert socket.PACKET_MULTICAST == 2
    assert socket.PACKET_OTHERHOST == 3
    assert socket.PACKET_OUTGOING == 4
    assert socket.PF_CAN == 29
    assert socket.PF_PACKET == 17
    assert socket.PF_RDS == 21
    assert socket.SCM_CREDENTIALS == 2
    assert socket.SCM_RIGHTS == 1
    assert socket.SHUT_RD == 0
    assert socket.SHUT_RDWR == 2
    assert socket.SHUT_WR == 1
    assert socket.SOCK_CLOEXEC == socket.SocketKind.SOCK_CLOEXEC
    assert socket.SOCK_DGRAM == socket.SocketKind.SOCK_DGRAM
    assert socket.SOCK_NONBLOCK == socket.SocketKind.SOCK_NONBLOCK
    assert socket.SOCK_RAW == socket.SocketKind.SOCK_RAW
    assert socket.SOCK_RDM == socket.SocketKind.SOCK_RDM
    assert socket.SOCK_SEQPACKET == socket.SocketKind.SOCK_SEQPACKET
    assert socket.SOCK_STREAM == socket.SocketKind.SOCK_STREAM
    assert socket.SOL_CAN_BASE == 100
    assert socket.SOL_CAN_RAW == 101
    assert socket.SOL_IP == 0
    assert socket.SOL_SOCKET == 1
    assert socket.SOL_TCP == 6
    assert socket.SOL_TIPC == 271
    assert socket.SOL_UDP == 17
    assert socket.SOMAXCONN == 128
    assert socket.SO_ACCEPTCONN == 30
    assert socket.SO_BINDTODEVICE == 25
    assert socket.SO_BROADCAST == 6
    assert socket.SO_DEBUG == 1
    assert socket.SO_DONTROUTE == 5
    assert socket.SO_ERROR == 4
    assert socket.SO_KEEPALIVE == 9
    assert socket.SO_LINGER == 13
    assert socket.SO_MARK == 36
    assert socket.SO_OOBINLINE == 10
    assert socket.SO_PASSCRED == 16
    assert socket.SO_PEERCRED == 17
    assert socket.SO_PRIORITY == 12
    assert socket.SO_RCVBUF == 8
    assert socket.SO_RCVLOWAT == 18
    assert socket.SO_RCVTIMEO == 20
    assert socket.SO_REUSEADDR == 2
    assert socket.SO_REUSEPORT == 15
    assert socket.SO_SNDBUF == 7
    assert socket.SO_SNDLOWAT == 19
    assert socket.SO_SNDTIMEO == 21
    assert socket.SO_TYPE == 3
    assert socket.TCP_CORK == 3
    assert socket.TCP_DEFER_ACCEPT == 9
    assert socket.TCP_FASTOPEN == 23
    assert socket.TCP_INFO == 11
    assert socket.TCP_KEEPCNT == 6
    assert socket.TCP_KEEPIDLE == 4
    assert socket.TCP_KEEPINTVL == 5
    assert socket.TCP_LINGER2 == 8
    assert socket.TCP_MAXSEG == 2
    assert socket.TCP_NODELAY == 1
    assert socket.TCP_QUICKACK == 12
    assert socket.TCP_SYNCNT == 7
    assert socket.TCP_WINDOW_CLAMP == 10
    assert socket.TIPC_ADDR_ID == 3
    assert socket.TIPC_ADDR_NAME == 2
    assert socket.TIPC_ADDR_NAMESEQ == 1
    assert socket.TIPC_CFG_SRV == 0
    assert socket.TIPC_CLUSTER_SCOPE == 2
    assert socket.TIPC_CONN_TIMEOUT == 130
    assert socket.TIPC_CRITICAL_IMPORTANCE == 3
    assert socket.TIPC_DEST_DROPPABLE == 129
    assert socket.TIPC_HIGH_IMPORTANCE == 2
    assert socket.TIPC_IMPORTANCE == 127
    assert socket.TIPC_LOW_IMPORTANCE == 0
    assert socket.TIPC_MEDIUM_IMPORTANCE == 1
    assert socket.TIPC_NODE_SCOPE == 3
    assert socket.TIPC_PUBLISHED == 1
    assert socket.TIPC_SRC_DROPPABLE == 128
    assert socket.TIPC_SUBSCR_TIMEOUT == 3
    assert socket.TIPC_SUB_CANCEL == 4
    assert socket.TIPC_SUB_PORTS == 1
    assert socket.TIPC_SUB_SERVICE == 2
    assert socket.TIPC_TOP_SRV == 1
    assert socket.TIPC_WAIT_FOREVER == -1
    assert socket.TIPC_WITHDRAWN == 2
    assert socket.TIPC_ZONE_SCOPE == 1
    assert socket.has_ipv6 == True
    print ('socket_00 ok')

def socket_01():
    """
    CMSG_LEN <class 'builtin_function_or_method'>
    CMSG_SPACE <class 'builtin_function_or_method'>
    dup <class 'builtin_function_or_method'>
    getdefaulttimeout <class 'builtin_function_or_method'>
    gethostbyaddr <class 'builtin_function_or_method'>
    gethostbyname <class 'builtin_function_or_method'>
    gethostbyname_ex <class 'builtin_function_or_method'>
    gethostname <class 'builtin_function_or_method'>
    getnameinfo <class 'builtin_function_or_method'>
    getprotobyname <class 'builtin_function_or_method'>
    getservbyname <class 'builtin_function_or_method'>
    getservbyport <class 'builtin_function_or_method'>
    htonl <class 'builtin_function_or_method'>
    htons <class 'builtin_function_or_method'>
    if_indextoname <class 'builtin_function_or_method'>
    if_nameindex <class 'builtin_function_or_method'>
    if_nametoindex <class 'builtin_function_or_method'>
    inet_aton <class 'builtin_function_or_method'>
    inet_ntoa <class 'builtin_function_or_method'>
    inet_ntop <class 'builtin_function_or_method'>
    inet_pton <class 'builtin_function_or_method'>
    ntohl <class 'builtin_function_or_method'>
    ntohs <class 'builtin_function_or_method'>
    setdefaulttimeout <class 'builtin_function_or_method'>
    sethostname <class 'builtin_function_or_method'>
    """
    print ('socket_99')

def socket_01():
    """
    SocketType <class 'type'>
    error <class 'type'>
    gaierror <class 'type'>
    herror <class 'type'>
    socket <class 'type'>
    timeout <class 'type'>
    """
    print ('socket_99')

def socket_99():
    
    # Very basic IPv4 Echo
    
    def server(HOST='', PORT=50007):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        data = conn.recv(1024)
        while data:
            conn.sendall(data)
            data = conn.recv(1024)
        conn.close()
        
    def client(HOST='localhost', PORT=50007):
        send_data = b'Hello, world!'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall(send_data)
        recv_data = s.recv(1024)
        # It is possible that the recv could return only a prefix of
        # the expected string. But for this local test that is
        # very unlikely.
        assert send_data == recv_data
        s.close()

    s = multiprocessing.Process(target=server)
    s.start()
    c = multiprocessing.Process(target=client)
    c.start()
    c.join()
    s.join()
    print ('socket_99 ok')

if __name__ == '__main__':
    # gen()
    socket_99()

