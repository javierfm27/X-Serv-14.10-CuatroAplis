#!/usr/bin/python3
import webappmulti
import socket

class hola(webappmulti.app):

    def process(self, parsedRequest):
        httpCode = "200 Ok"
        htmlAnswer = "<!DOCTYPE html><html><body><h1>¡HOLA!</h1></body></html>"
        return (httpCode, htmlAnswer)

class adios(webappmulti.app):

    def process(self, parsedRequest):
        httpCode = "200 Ok"
        htmlAnswer = "<!DOCTYPE html><html><body><h5> ADIÓS </h5></body></html>"

if __name__ == "__main__":
    holaApp = hola()
    adiosApp = adios()
    testWebApp = webappmulti.webApp(socket.gethostname(), 1231, {'/hola': holaApp,
                                                                '/adios': adiosApp})
