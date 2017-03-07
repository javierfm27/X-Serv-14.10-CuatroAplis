#!/usr/bin/python3
import socket
import webappmulti


class aleat(webappmulti.app):

    def process(self, parsedRequest):
        import random
        numero = random.randint(0, 10000000000000)
        httpCode = "200 OK"
        htmlAnswer = "<!DOCTYPE html><html><body> Dame otra <a href='" \
                    + str(numero) + "'> mas</a></body></html>"
        return(httpCode, htmlAnswer)
