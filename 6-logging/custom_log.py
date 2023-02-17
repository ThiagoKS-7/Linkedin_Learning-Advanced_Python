# Demonstrate how to customize logging output

import logging
import socket
from requests import get
ip = get('https://api.ipify.org').text


def get_data():
    response = get(f'https://ipapi.co/{ip}/json/').json()
    myData = {
        "hostname": f"{socket.gethostname()} ({response.get('version')}) -\
{response.get('country')}, {response.get('timezone')}",
    }
    return myData


myData = get_data()


def another_func():
    logging.debug("Debugging another function", extra=myData)


def main():
    # set the output file and debug level, and
    datestr = "%d/%m/%Y %I:%M:%S %p"
    fmtstr = "User: %(hostname)s %(asctime)s - %(levelname)s: %(funcName)s() \
Line: %(lineno)d %(message)s"

    # TODO: use a custom formatting specification
    logging.basicConfig(
        filename="output.log",
        level=logging.DEBUG,
        filemode="w",
        format=fmtstr,
        datefmt=datestr
    )

    logging.info("This is an info-level log message", extra=myData)
    logging.warning("This is a warning-level message", extra=myData)
    another_func()


if __name__ == "__main__":
    main()
