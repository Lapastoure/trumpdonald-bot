# Automate TrumpDonald.org

Simple selenium script that forever blows Donald's strange hair.

![](screenshot.gif)


## Set-up

Install dependencies in a Python virtualenv:

    $ pip install -r requirements.txt

Run it:

    # Example:
    # python trump.py [num_processes]

    $ python trump.py 1

If you must, quit it:

    $ ctrl-C

Or just close the browser.

## Multi-processing

By default, that argument passed into the script is the number of processes to
run. Increase the number to run multiple brosers in parallel. Passing no
argument will default to the number of CPUs available on your computer.
