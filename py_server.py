# _*_ coding:utf-8 _*_
__author__ = '作者'

from com.shengsiyuan.netty.thrift.generated.py.gen import PersonService
from PersonServiceImpl import PersonServiceImpl

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

try:
    personServiceHandler = PersonServiceImpl()
    processor = PersonService.Processor(personServiceHandler)

    #   socket
    serverSocket = TSocket.TServerSocket(port=8899)

    #   transport
    transportFactory = TTransport.TFramedTransportFactory()

    #   protocol
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()

    #   Server
    server = TServer.TSimpleServer(processor, serverSocket, transportFactory, protocolFactory)

    #   启动
    server.serve()


except Thrift.TException, tx:
    print '%s ' % tx.message
