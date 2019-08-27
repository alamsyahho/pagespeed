class Response(object):
    """ Base Response Object

    Attributes:
        self.json (dict): JSON representation of response
        self._request (str): URL of
        self._response (`requests.models.Response` object): Response object from requests module
    """
    def __init__(self, response):
        response.raise_for_status()

        self._response = response
        self._request = response.url
        self.json = response.json()

    def __repr__(self):
        return '<Response>'


class PageSpeedResponse(Response):
    """ PageSpeed Response Object

    Attributes:
        self.url (str):
        self.title (str):
        self.locale (str):
        self.version (str):
        self.speed (int):
        self.statistics (`Statistics` object):
    """

    @property
    def url(self):
        return self.json.get('id')

    @property
    def title(self):
        return self.json.get('title')

    @property
    def locale(self):
        return self.json['lighthouseResult']['configSettings']['locale']

    @property
    def version(self):
        return self.json['lighthouseResult']['lighthouseVersion']

    @property
    def speed(self):
        return self.json['lighthouseResult']['categories']['performance']['score']

    def to_csv(self, path):
        pass

    def pretty_print(self):
        pass

    def __repr__(self):
        return '<Response(url={0})>'.format(self.url)


class DesktopPageSpeed(PageSpeedResponse):

    def __repr__(self):
        return '<DesktopPageSpeed(url={0})>'.format(self.url)


class MobilePageSpeed(PageSpeedResponse):

    @property
    def usability(self):
        return self.json.get('ruleGroups').get('USABILITY').get('score')

    def __repr__(self):
        return '<MobilePageSpeed(url={0})>'.format(self.url)