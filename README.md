# Runs as a github actions script. 
## Getting Venmo Token
Run the `src/venmo_get_token.py` script locally and set the username and password to get your venmo token. There's no expiration so make sure it's hella secret. 

## Running the script:
Provide the following envars in the action yml, or as regular envars to run manually:

- `VENMO_TOKEN` - Obtained via `venmo_get_token.py` sciprt
- `PAYEE` - Payee's venmo username
- `PAYMENT_AMMOUNT` - Amount you want to pay. ex) 5.00
- `NOTE` - Note to be added to the payment (the month/year will be added by the script)
- `PAYMENT_ID` - What payment method to use (can't remember where to get this. Google it 🤷‍♂️) It uses your venmo walet by default and will error out if not enough funds. 
