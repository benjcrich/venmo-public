import os
from venmo_api import Client
from datetime import datetime
from time import sleep

venmo = Client(access_token=os.environ['VENMO_TOKEN'])
cur_month_year = datetime.now().strftime('%B %Y')
print(cur_month_year)

username = os.environ['PAYEE']

if username != '':
    amount = os.environ['PAYMENT_AMMOUNT']
    user_id_search = venmo.user.search_for_users(username)
    user_id = None
    for i in user_id_search:
        if i.username == username:
            user_id = i.id
            break
    sleep(1)
    if user_id:
        try:
            note = f'{cur_month_year} -- {os.environ["NOTE"]}'
            venmo.payment.send_money(
                amount=float(amount),
                note=note,
                target_user_id=user_id,
                funding_source_id=os.environ['PAYMENT_ID']
            )

            print(f'Success: Paid {username} ${amount}, {note}')
        except Exception as error:
            print(f'Failed: {username}\nError: {error}')
    else:
        print(f'Failed to get user id for {username}')
