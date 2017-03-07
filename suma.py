#!/usr/bin/python3
import webappmulti
import socket

class suma(webappmulti.app):

    def parse(self, request, rest):
        parsedRequest = rest[1:]
        print(parsedRequest)
        return parsedRequest

    def process(self, parsedRequest):
        if parsedRequest == 'favicon.ico':
            return("404 Not Found","<!DOCTYPE html><html><body><h1>Not Found</h1></body></html>")
        operando1, operando2 = parsedRequest.split('+')
        print(operando1, " ", operando2)
        resultado = int(operando1) + int(operando2)
        htmlAnswer = "<!DOCTYPE html><html><body><p> El resultado de sumar " \
                    + operando1 + " + " + operando2 + " = " + str(resultado) \
                    + "</p></body></html>"
        return("200 OK",htmlAnswer)
