import logging, logging_config

from urllib.request import urlopen
from urllib.error import URLError
from config import MAX_DOWNLOAD_TIME

def downloader(url):
    try:
        logging.info('Obtaining data from %s', url[:50] + '...' if len(url) > 50 else url)
        with urlopen(url, timeout=MAX_DOWNLOAD_TIME) as session:
            html = session.read()
            return html
    except (URLError, TimeoutError, UnicodeEncodeError):
        logging.error('Failed to obtain data from %s', url)
        return None