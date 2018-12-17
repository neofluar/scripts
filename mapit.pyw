#! python3
# mapit.pyw - launches GoogleMap in the browser using an address 
#             from the command line or clipboard.

import sys
import webbrowser, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# Else get address from clipboard.
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
