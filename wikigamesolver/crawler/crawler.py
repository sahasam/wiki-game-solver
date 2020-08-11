"""
Usage: wikigamesolver crawl [options]

Options:
    -h, --help                          print this message
    -s, --start-page <url>              start page for wikipedia crawler [default: https://en.wikipedia.org/wiki/Python_(programming_language)]
    -e, --end-page <url>                end page for wikipedia crawler [default: https://en.wikipedia.org/wiki/Web_scraping]

"""
import logging
import sys
import wikipedia

from docopt import docopt

logger = logging.getLogger(__name__)

#start the indexing from the main page of Wikipedia
#list(map(lambda x:x.lower().replace(' ', '_'), wikipedia.page("Python").links))

def bfs (start_page, end_page) :
    if end_page in list(map(lambda x: x.lower().replace(' ', '_'), wikipedia.page("python_(programming_language)").links)):
        logger.debug(f"FOUND: {end_page} is in {start_page}")
    else:
        logger.debug(f"NOT FOUND: {end_page} not found in {start_page}. Moving down the tree")


def main():
    logger.debug("starting crawler")

    argv = sys.argv[1:]
    args = docopt(__doc__, argv=argv) 

    logger.debug("args: \n%s " % args)

    start_page = args['--start-page']
    end_page = args['--end-page']
    print(end_page.split('/')[-1].lower())

    bfs(start_page.split('/')[-1].lower(), end_page.split('/')[-1].lower())