"""
wikigamesolver crawler. Contains the search algorithms used to find the route
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
    """
    breadth first search.
    Recursively searches every link to a depth of 5. Does not account for link loops
    and is very slow and inconsistent.

    Try 1: 3 minutes 51 seconds
    Try 2: 11 minutes 5 seconds
    Try 3: 30 minutes 21 seconds
    """
    try:
        link_list = list(map(lambda x: x.lower().replace(' ', '_'), wikipedia.page(start_page).links))
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) :
        print(f"skipping {start_page}")
        return False

    trace.append(start_page)
    if end_page in link_list:
        logger.debug(f"FOUND: {end_page} is in {start_page}")
        logger.info(trace)
        return True
    else:
        logger.debug(f"NOT FOUND: {end_page} not found in {start_page}. Currently at depth {depth}")
        if depth >= 5:
            return False
        for link in link_list :
            if bfs(link, end_page, depth + 1, trace) :
                return True
        return False

def bfs_threaded (start_page, end_page, depth=0, trace=[]):
    import threading
    import threading.Lock
    import queue
    """
    a multithreaded breadth first search
    Recursively searches every link to a depth of 5, but has three worker threads to speed up the process
    """
    pageQueue = queue.Queue()
    t1 = threading.Thread(target=bfs_worker_thread)
    t2 = threading.Thread(target=bfs_worker_thread)
    t3 = threading.Thread(target=bfs_worker_thread)
    t1.start()
    t2.start()
    t3.start()

def main():
    logger.debug("starting crawler")

    argv = sys.argv[1:]
    args = docopt(__doc__, argv=argv)

    logger.debug("args: \n%s " % args)

    start_page = args['--start-page']
    end_page = args['--end-page']

    bfs(start_page.split('/')[-1].lower(), end_page.split('/')[-1].lower())
