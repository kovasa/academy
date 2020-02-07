""" Accepts URL as a string (for example, 'http://google.ru/') and
uses 'my_get' function to make request.
"""
import website_alive.make_request


def check(my_url):
    """ Calls 'my_get' to get site response and checks it.

    Args:
        my_url (str): URL of the site.

    Returns:
        bool: State of the site. True if site is available and False otherwise.
    """
    return website_alive.make_request.my_get(my_url).status_code == 200
