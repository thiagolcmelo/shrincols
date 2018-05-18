shrincols
=========

CLI for making a text to fit in a max number of columns. It is possible to
especify the max number of columns as well as to juntify it.

It is possible to write output to a file and to pipe a text for the script's 
standard input.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``https://github.com/thiagolcmelo/desafio-idwall``
3. Fetch development dependencies: ``make install``

Usage
-----

The input might be a filename:

::

    $ shrincols filename.txt -c 80

or a string:

::

    $ shrincols "some text goes here ..." -c 80

The option ``-j`` forces the text to be justified:

::

    $ shrincols filename.txt -c 80 -j

Altough the result will always be printed on the standard output, the option
``-o`` might be used for writing the result to a file.

::

    $ shrincols filename.txt -c 40 -o output.txt

It is also possible to pipe standard output into the script's standard input:

::

    $ cat filename.txt | shrincols -c 40

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use

::

    $ pipenv run make



