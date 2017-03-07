#!/usr/bin/python3
import webappmulti
import socket
import hola
import suma


if __name__ == "__main__":
    holaApp = hola.hola()
    adiosApp = hola.adios()
    sumaApp = suma.suma()
    aleatApp = aleat.aleat()
    testWebApp = webappmulti.webApp(socket.gethostname(), 1231, {'/hola': holaApp,
                                                                '/adios': adiosApp,
                                                                '/suma' : sumaApp,
                                                                '/aleat': aleatApp})
