# Teste lojaintegrada

## Problem to solve
    - editor_grafico.py.txt
## Set Up

    $ cd lojaintegrada
    $ virtualenv  -p /usr/bin/python3.4 env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python app/graphic_editor.py
    
## Tests
    $ cd lojaintegrada
    $ source env/bin/activate
    $ nosetests test/test_graphic_editor.py
