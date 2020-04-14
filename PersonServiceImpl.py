# _*_ coding:utf-8 _*_
__author__ = '作者'

from com.shengsiyuan.netty.thrift.generated.py.gen import ttypes

class PersonServiceImpl:

    def getPersonByUsername(selfs, username):
        print "Got Client Param: " + username

        person = ttypes.Person()
        person.username = "lisi"
        person.age = 30
        person.married = True
        return person

    def savePerson(self, person):
        print "Got Client Param: "
        print person.username
        print person.age
        print person.married
