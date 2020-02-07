""" Makes request to the site using "requests" library to get response. """
import requests


def my_get(my_url):
    """ Makes request by 'url' using 'requests' library and returns response.

    Args:
        my_url (str): URL of the site.

    Returns:
        Response: Result of request.
    """
    return requests.get(my_url)
