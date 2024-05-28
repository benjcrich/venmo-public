from venmo_api import Client

access_token = Client.get_access_token(username = '<venmo_username>',
                                       password = '<venmo_password>')

print("My token:", access_token)
