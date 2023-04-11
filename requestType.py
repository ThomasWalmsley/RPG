from enum import IntEnum

class RequestType(IntEnum):
    noType = 0
    getData = 1
    setData = 2
    load = 3
    save = 4
    create = 5
    changeState = 6