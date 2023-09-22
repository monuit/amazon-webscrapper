import time
import argparse
from amazon_scraper.scraper import Scraper

class AmazonScraperApp:
    def __init__(self):
        self.scraper = Scraper()
        print("Scraper initialized.")

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Extracts links contained in a URL')
        parser.add_argument(
            '-w', '--word',
            nargs='*',
            default='smart phone',
            help='Enter the word you want to search'
        )
        self.args = parser.parse_args()
        self.args.word = ' '.join(self.args.word)
        print("Arguments parsed.")

    def execute_scraper(self):
        self.scraper.search(self.args.word)
        print("Scraping complete.")

def main():
    app = AmazonScraperApp()
    app.parse_arguments()
    app.execute_scraper()

if __name__ == "__main__":
    print("Extracting...")
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print("Finished Extracting...")
    print(f"The extraction took {end_time - start_time:.2f} seconds.")
