# LocalTimeServer
A simple local time server

## Usage:

`LocalTimeServer -h <host> -p <port> [--version] [-?]`

The server will answer queries to this host/port with the current local time in JSON format.

Enter the -? option to view command-line options.

In a browser, enter:

    http://<host>:10123/

It should return something like this:

    {"year": 2023, "month": 2, "dom": 17, "hour": 23, "min": 46, "sec": 11, "dow": 4, "doy": 48, "is_dst": 1}

## Building Python Package:

You may need to install virtual environment support for your python version:

    sudo apt install python<X.X>-venv

...where X.X is the python version on your system.
i.e. python3.10 would be python3.10-venv.
Note that LocalTimeServer requires Pyhton 3.6 or later.

From this directory:

    python3 build .

To install the built package:

    pip3 install ./dist/LocalTimeServer-<VERSION>-py3-none-any.whl --force-reinstall

...where VERSION is the version of LocalTimeServer you have just built (see version.py).
This will install LocalTimeServer just for the current user in .local/bin.
To install system-wide, use sudo.

## Building Debian package

Firstly, install pre-requisites:

    sudo apt install build-essential binutils lintian debhelper dh-make devscripts

Set the following environment variables:

    export DEBEMAIL="your@mail.com"
    export DEBFULLNAME="Name Lastname"


TBC

## Installing into OS

TBC

## Updating Version#:

    ./deb_lts/DEBIAN/control
    ./LocalTimeServer/version.py
