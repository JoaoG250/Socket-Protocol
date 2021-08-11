from core import Parser
from calculator import handlers

services = {
    "add": {"send": handlers.add},
    "subtract": {"send": handlers.subtract},
    "multiply": {"send": handlers.multiply},
    "divide": {"send": handlers.divide},
}

parser = Parser(services)
