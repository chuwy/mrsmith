######################################
Mr. Smith - dead simple secret manager
######################################

Disclaimer
==========
Only intention of this application - is prevent user from store chunks of text (like passowrds) in plain text format and give tool to extract them from python code.
Thus, it's a very simple and apparently non-secure way to store data and if you messing up with NSA, you probably should check other tools.

I can advice `keyring <https://bitbucket.org/kang/python-keyring-lib>`_ which is also written in python, supports system keyring services (like OS X Keychain) and actively developing. On the other hand, keyring is developed with accent on passwords. Mr. Smith developed with accent on any piece of text information.

*It's just better than plain-text. Nothing more.*


Installation
============
It's unavailable on PyPi for now, so you can install it from github:

.. code-block::

  pip install -e git+https://github.com/chuwy/mrsmith.git#egg=mrsmith

It requires python-gnupg for interacting with GPG (and of course **GPG itself**).

Also if you have installed pyperclip, you can store your secrets in OS clipboard.
Though it isn't installed by default.

It is highly recommended to install GPG2 (instead of 1)and point path to executable (gpgninary) in configuration.

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

List all your secrets: ``mrsmith list``

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
+ [X] logging for non-console access
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
