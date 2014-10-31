"""
Mostly initialization and py3/py2-compatible functions.
"""


try:
    import configparser
except ImportError:
    import ConfigParser as configparser
from os import getenv, makedirs
from os.path import dirname, exists, expanduser, join, realpath


def get_input(prompt):
    """
    Py3k compatible way for user input.
    """
    try:
        input = raw_input   # We're in python 2
    except NameError:
        pass                # We're in python 3
    return input(prompt)


def init_config(configpath, secretsdir=None, recipient=None):
    """
    Create config file and return ConfigParser object
    """
    if not secretsdir or secretsdir.isspace():
        secretsdir = "~/.secrets"
    config = configparser.RawConfigParser()
    config.add_section('Paths')
    config.set('Paths', 'secrets', secretsdir)
    config.add_section('GPG')
    config.set('GPG', 'recipient', recipient)
    config.set('GPG', 'gnupghome', expanduser('~/.gnupg'))
    with open(configpath, 'wb') as configfile:
        config.write(configfile)
    return config


def get_config_path():
    """
    Try to get $XDG_CONFIG_HOME or fallback to ~/.config
    """
    try:
        configpath = realpath(expanduser(getenv('XDG_CONFIG_HOME')))
    except AttributeError:
        configpath = realpath(expanduser('~/.config'))
    finally:
        configfile = join(configpath, 'mrsmith', 'config')

    return configfile


def get_config(configfile=None):
    if not configfile:
        configfile = get_config_path()
    if not exists(configfile):
        print("It seems that it your first run.\n"
              "I'm creating a configfile at {}.\n"
              "Please, be sure that you gave me proper settings.".format(configfile))
        makedirs(dirname(configfile), 0o700)
        secretsdir = get_input("Specify dir, where you will be keep your secrets.\n"
                               "Directory will be created when you add your first secret "
                               "(default is ~/.secrets): ")
        recipient = get_input("Specify recipient user id. It used by GPG to get right key. "
                              "In most cases it's just your email ")
        config = init_config(configfile, str(secretsdir), str(recipient))
    else:
        config = configparser.RawConfigParser()
        config.read(configfile)
    return config
