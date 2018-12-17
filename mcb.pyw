#! python3
# mcb.pyw - saves and loads text fragments to the clipboard
# Usage: mcb save <keyword> - saves clipboard to a keyword value
#        mcb <keyword> - loads the keyword value to clipboard
#        mcb list - loads a list of keywords to clipboards
#        mcb delete - deletes all data
#        mcb delete <keyword> - deletes the keyword

import sys, shelve, pyperclip

mcb_shelf = shelve.open('mcb')
if len(sys.argv) == 3:
    # Save clipboard content.
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2].lower()] = pyperclip.paste()
    
    # Delete the keyword from the shelf.
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2].lower() in mcb_shelf:
            del mcb_shelf[sys.argv[2].lower()]
        else:
            pyperclip.copy('No such keyword <' + sys.argv[2].lower() + '>.')
    
    # Bad imput.
    else:
       pyperclip.copy('Wrong input. Try again.') 

elif len(sys.argv) == 2:
    # List of keywords.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    
    # Delete all.
    elif sys.argv[1].lower() == 'delete':
        for key in list(mcb_shelf.keys()):
            del mcb_shelf[key]
    
    # Load content.
    elif sys.argv[1].lower() in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1].lower()])
    else:
        pyperclip.copy('No such keyword <' + sys.argv[1].lower() + '>.')

# Bad imput.
else:
    pyperclip.copy('Wrong input. Try again.')
mcb_shelf.close()
