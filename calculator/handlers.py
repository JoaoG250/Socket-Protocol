from core import Response


def add(request):
    """Add service handler.

    Args:
        request (Request): Request object instance.

    Returns:
        Response: Response object instance.
    """

    content = request.content
    if content and isinstance(content, list):
        try:
            res = sum(content)
            return Response(res, "S0")
        except TypeError:
            return Response("List items have to be integer or float", "CE0")
    return Response('"content" needs to be a non empty list.', "CE0")


def subtract(request):
    """Subtract service handler.

    Args:
        request (Request): Request object instance.

    Returns:
        Response: Response object instance.
    """

    content = request.content
    if content and isinstance(content, list):
        try:
            res = content[0]
            for i in range(1, len(content)):
                res -= content[i]
            return Response(res, "S0")
        except TypeError:
            return Response("List items have to be integer or float", "CE0")
    return Response('"content" needs to be a non empty list.', "CE0")


def multiply(request):
    """Multiply service handler.

    Args:
        request (Request): Request object instance.

    Returns:
        Response: Response object instance.
    """

    content = request.content
    if content and isinstance(content, list):
        try:
            res = content[0]
            for i in range(1, len(content)):
                res *= content[i]
            return Response(res, "S0")
        except TypeError:
            return Response("List items have to be integer or float", "CE0")

    return Response('"content" needs to be a non empty list.', "CE0")


def divide(request):
    """Divide service handler.

    Args:
        request (Request): Request object instance.

    Returns:
        Response: Response object instance.
    """

    content = request.content
    if content and isinstance(content, list):
        try:
            res = content[0]
            for i in range(1, len(content)):
                res /= content[i]
            return Response(res, "S0")
        except TypeError:
            return Response("List items have to be integer or float", "CE0")
    return Response('"content" needs to be a non empty list.', "CE0")
