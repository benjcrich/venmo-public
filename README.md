# Runs as a github actions script. 
## Getting Venmo Token
Run the `src/venmo_get_token.py` script and set the envars to get your venmo token. There's no expiration so make sure it's hella secret. 

## Running the script:
Provide the following envars in the action yml, or as regular envars to run manually:

- `VENMO_TOKEN` - Obtained via `venmo_get_token.py` sciprt
- `PAYEE` - Payee's venmo username
- `PAYMENT_AMMOUNT`
- `NOTE` - Note to be added to the payment
- `PAYMENT_ID` - What payment method to use
