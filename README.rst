######################################
Mr. Smith - dead simple secret manager
######################################

Disclaimer
==========
Only intention of this application - is prevent user from store chunks of text (like passowrds) in plain text format and give tool to extract them from python code.
Thus, it's a very simple and apparently non-secure way to store data and if you messing up with NSA, you probably should check other tools.

*It's just better than plain-text. Nothing more.*


Installation
============
It's unavailable on PyPi for now, so you can install it from github:

.. code-block::
  pip install -e git+https://github.com/chuwy/mrsmith.git#egg=mrsmith

It requires python-gnupg for interacting with GPG (and of course **GPG itself**) and pyperclip for interacting with ClipBoard.

Objectives
==========
mrsmith create documentation after first run. It's placed inside $XDG_CONFIG_HOME/mrsmith ($XDG_CONFIG_HOME is $HOME/.config on most systems).

Command Line Interface
----------------------
Signature is
``mrsmith *action* OPTIONS``, where most of actions accept *--user* and *secret* as options.

Tell new secret (creates db, if it doesn't exists):
``mrsmith add -u MrGrey --note="Short uncrypted note" strong_secret``

Output password to terminal, after masterpass prompt:
``mrsmith show cia``

Copy password to clipboard, after masterpass prompt:
``mrsmith cp -u MrRed github.com``
If you have several usernames attached to particular service, you must specify it.

Anyway, ``-u`` and ``-n`` doesn't work for a while.

Low-level access
----------------
You can access your secrets within python code, for example:

.. code-block:: python

  from mrsmith.api import get_secret

  # If you have proper configuration and running gpg-agent, you will get password immediately
  secret = get_secret('reddit.com')


Planned features
================

+ [X] Get secret within python code
+ [X] Copy text to Mac OS X clipboard, and remove it after some period (``cp subcommand``)
+ Minimal security audit
+ Upload to PyPi, setup with copying to $PATH
+ logging for non-console access
+ raise error on special symbols
+ username option
+ note option
+ Refactoring
+ Check py3k compatibility

Tips
====
It's a good idea to use a secret keyfile, and store it on encrypted partition,
for example, `TrueCrypt <http://www.truecrypt.org/>`_.

If anyone will get access to your hard drive, he will see just two encrypted and useless piece of information:
your TrueCrypt partition and catalog with your encrypted secrets.
