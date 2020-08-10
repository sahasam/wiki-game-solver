"""
wikigamesolver.

Usage:
    wikigamesolver <command> [<args>...]

Option:
    -h, --help
"""
import logging

from docopt import docopt
from wikigamesolver import __version__

def main():
    logger = logging.getLogger()
    
    args = docopt(__doc__, version=f"pyvr version {__version__}", options_first=True)

    logger.debug(f"command: {args['<command>']}")