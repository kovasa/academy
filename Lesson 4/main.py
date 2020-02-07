"""
Asks the user for the address of the site that needs to be checked.
Then it uses 'website_alive' package to check whether the site is available.
"""
import website_alive.check_response

if website_alive.check_response.check(input('Enter the site address: ')):
    print("Site is available")
else:
    print("Site is unavailable")
