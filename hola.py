#!/usr/bin/python3
import webappmulti
import socket

class hola(webappmulti.app):

    def process(self, parsedRequest):
        httpCode = "200 Ok"
        htmlAnswer = "<!DOCTYPE html><html><body><h1>HOLA</h1></body></html>"
        return (httpCode, htmlAnswer)

class adios(webappmulti.app):

    def process(self, parsedRequest):
        httpCode = "200 Ok"
        htmlAnswer = "<!DOCTYPE html><html><body><h1> ADIOS </h1></body></html>"
        return(httpCode, htmlAnswer)
