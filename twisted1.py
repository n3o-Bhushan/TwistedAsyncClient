from __future__ import print_function

from sys import argv
from pprint import pformat

from twisted.internet.task import react
from twisted.web.client import Agent, readBody
from twisted.web.http_headers import Headers
#from stringprod import StringProducer
import datetime
import operator



def cbRequest(response):
    #print('Response version:', response.version)
    #print('Response code:', response.code)
    #print('Response phrase:', response.phrase)
    #print('Response headers:')
    #print(pformat(list(response.headers.getAllRawHeaders())))
    d = readBody(response)
    d.addCallback(cbBody, response)
    return d

def cbBody(body, response):
    Present=body in dict2
    if(Present==False):
       dict2[response.request.absoluteURI]=body
       #top3= sorted(dict2.iteritems(), key=lambda x:-x[1]):[:3]
       #top3=sorted(dict2.items(),key=operator.itemgetter(1))
       #test1=top3[0][0]
       #print(test1)
    print(dict2)
    # print('Response body:')
    # print(body)

def main(reactor):
    global dict2
    dict2={}
    url=["http://localhost:8080/","http://localhost:5000/"]

    #body =StringProducer(str(datetime.datetime.now().time()))
    for a in url:
        #print(a)
        agent = Agent(reactor)
        d = agent.request(
            'GET', a,
            Headers({'User-Agent': ['Twisted Web Client Example'],'time-stamp':[str(datetime.datetime.now().time())]}),
            None)
        d.addCallback(cbRequest)
    return d

react(main)