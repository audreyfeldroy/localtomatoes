"""
localtomatoes.

Usage:
  localtomatoes [options] command <param> <another_params>
  localtomatoes [options] another-command <param>

  localtomatoes -h | --help

Options:
  --kw-arg=<kw>         Keyword option description.
  -b --boolean          Boolean option description.
  --debug               Debug.

  -h --help             Show this screen.
"""

from docopt import docopt
import logging

import localtomatoes

log = logging.getLogger(__name__)


def main():
    arguments = docopt(__doc__, version=localtomatoes.__version__)
    debug = arguments['--debug']
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    log.debug('arguments: %s', arguments)
