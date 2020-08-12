"""
Usage: wikigamesolver crawl [options]

Options:
    -h, --help                          print this message
    -s, --start-page <url>              start page for wikipedia crawler [default: https://en.wikipedia.org/wiki/Python_(programming_language)]
    -e, --end-page <url>                end page for wikipedia crawler [default: https://en.wikipedia.org/wiki/London_Stock_Exchange]

"""
import logging
import sys
import wikipedia

from docopt import docopt

logger = logging.getLogger(__name__)


def bfs (start_page, end_page, depth=0, trace=[]) :
    link_list = list(map(lambda x: x.lower().replace(' ', '_'), wikipedia.page(start_page).links))
    if end_page in link_list:
        logger.debug(f"FOUND: {end_page} is in {start_page}")
        return True
    else:
        logger.debug(f"NOT FOUND: {end_page} not found in {start_page}. Moving down the tree")
        if depth >= 5:
            return False
        for link in link_list :
            if bfs(link, end_page, depth + 1, trace) :
                return True
        return False

def main():
    logger.debug("starting crawler")

    argv = sys.argv[1:]
    args = docopt(__doc__, argv=argv) 

    logger.debug("args: \n%s " % args)

    start_page = args['--start-page']
    end_page = args['--end-page']

    bfs(start_page.split('/')[-1].lower(), end_page.split('/')[-1].lower())