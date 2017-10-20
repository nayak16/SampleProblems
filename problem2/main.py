import logging
import os
from html_scraper import HTMLScraper


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


TARGET_LINK = 'shittylistings.com'


def construct_file_path(file, cwd):
    return cwd + '/' + file


def search_directory(root_dir, html_scraper):
    logger.info(
        "Searching the {} directory for files with link to {}..."
        .format(root_dir, TARGET_LINK)
    )
    bad_files = []
    for path, subdirs, cwd_files in os.walk(root_dir):
        for file in cwd_files:
            full_path = construct_file_path(file, path)
            if html_scraper.has_target_link(full_path):
                bad_files.append(full_path)

    return bad_files


def main():

    # Set cwd to path of script
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    scraper = HTMLScraper(TARGET_LINK)
    bad_files = search_directory('./website', scraper)

    logger.info('The following files link to {}:'.format(TARGET_LINK))
    for file in bad_files:
        logger.info(file)


if __name__ == '__main__':
    main()
