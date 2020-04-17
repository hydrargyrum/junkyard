#!/usr/bin/env python3

import requests


# boilerplate
def setup_session_for_returning_addr(session):
    def set_ip(response, *args, **kwargs):
        # depending on the requests/urllib3/python version, the attribute
        # may be in a different place
        try:
            func = response.raw._connection.sock.getpeername
        except AttributeError:
            try:
                func = response.raw._connection.sock.socket.getpeername
            except AttributeError:
                func = None

        if func is not None:
            response.remote_addr = func()

    # insert it before others because as soon as content is read, as the
    # "_connection" attr doesn't exist anymore after reading body
    session.hooks['response'].insert(0, set_ip)
# end of boilerplate


# demo
session = requests.Session()
setup_session_for_returning_addr(session)
response = session.get('https://httpbin.org/get')
print(response.remote_addr)
