import json


class Request(object):
    """Client request class."""

    def __init__(self, action, service=None, params=None, content=None):
        self.action = action
        self.service = service
        self.params = params
        self.content = content


class Response(object):
    """Server response class."""

    def __init__(self, content, status="S0"):
        self.content = content
        self.status = status

    def serialize(self):
        """Serializes the response to JSON.

        Returns:
            str: JSON serialized string.
        """

        serialized_response = json.dumps(
            {"status": self.status, "content": self.content}
        )
        return serialized_response


class Parser(object):
    """Protocol parser class."""

    def __init__(self, services):
        self.actions = ["catalog", "services"]
        self.services = services

    def parse_request(self, request):
        """Request parser method.

        Args:
            request (Request): Request object instance.

        Returns:
            Response: Response object instance.
        """

        if request.service is None:
            if request.action == "catalog":
                return Response(self.actions, "S0")
            elif request.action == "services":
                res = list(self.services.keys())
                return Response(res, "S0")
            else:
                return Response(None, "CE2")
        else:
            try:
                service = self.services[request.service]
                if request.action == "catalog":
                    res = list(service.keys())
                    return Response(res, "S0")
                handler = service[request.action]
                return handler(request)
            except KeyError:
                return Response(None, "CE2")
