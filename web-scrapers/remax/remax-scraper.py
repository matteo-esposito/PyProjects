import requests
from bs4 import BeautifulSoup
from csv import writer
import re
import time


def timedRun(func, *args):
    """ 
    Return the output of the provided function and the amount of time elapsed
    from the call of the function to the end of execution.

    Arguments:
        func {function} -- A method that needs to be timed.
        *args: argument(s) for the function provided
    """
    start = time.clock()
    func(*args)
    end = time.clock()
    print('Time elapsed: ({0:.{1}f}s)'.format((end-start), 4))


def parser(maxPage=50):
    """
    Function that scrapes housing data from remax.

    Keyword Arguments:
        maxPage {int} -- Limit of number of pages to scrape (default: {50})
    """

    # "Open" csv to write header
    with open('remax-scraped.csv', "w") as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(["Price", "Description", "Address",
                             "# Bath", "# Bed", "# Water Room", "Note", "ULS", "Link"])

    for pgnum in range(0, maxPage-1):
        url = "https://www.remax-quebec.com/fr/recherche/residentielle/resultats.rmx?offset=" + \
            str(10*pgnum) + "#listing"

        # Initial site access
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Main envelope
        posting_elements = soup.find(
            class_="listing-mosaik listing-properties")

        # Individual ads
        ads = posting_elements.find_all(class_="property-entry")

        # Start appending to csv
        with open("remax-scraped.csv", "a") as csv_file:
            csv_writer = writer(csv_file)

            # Scrape desired variables from individual ads on search page "search-results-listings-list__item"
            for posting in ads:

                # Description
                desc_elem = posting.find(class_="property-type")
                if desc_elem is not None:
                    desc_val = re.sub(r'[\t\r\n]', '', desc_elem.text).replace(
                        "             à", " à").rstrip()

                # Prices
                posting_price_elem = posting.find(class_="property-price")
                if posting_price_elem is not None:
                    price_val = posting_price_elem.text.replace(
                        "$", "").strip().replace("  ", " ")

                # Address
                address_elem = posting.find(class_="property-address")
                if address_elem is not None:
                    add_val = address_elem.find("h2").text.strip().replace(
                        '"', "").replace(",", " ")

                # Room counters
                bb_elem = posting.find(class_="property-options")
                if bb_elem is not None:
                    bb_val = bb_elem.find_all("span")

                    if len(bb_val) < 1:
                        bb_val1 = 0
                    else:
                        bb_val1 = re.sub("[^0-9]", "", str(bb_val[0]))

                    if len(bb_val) < 2:
                        bb_val2 = 0
                    else:
                        bb_val2 = re.sub("[^0-9]", "", str(bb_val[1]))

                    if len(bb_val) < 3:
                        bb_val3 = 0
                    else:
                        bb_val3 = re.sub("[^0-9]", "", str(bb_val[2]))

                # Note
                note_elem = posting.find(
                    class_="property-special-infos property-special-infos-new")
                if note_elem is not None:
                    note_val = re.sub(r'[\t\r\n]', '', note_elem.text).strip()

                # ULS
                uls_elem = posting.find(class_="property-uls")
                if uls_elem is not None:
                    uls_val = uls_elem.text.replace("ULS: ", "").strip()

                # Url
                url_elem = posting.find("a", class_="property-thumbnail")
                if url_elem is not None:
                    url_val = "https://www.remax-quebec.com/" + \
                        url_elem["href"]

                # Write to csv file
                csv_writer.writerow(
                    [price_val, desc_val, add_val, bb_val1, bb_val2, bb_val3, note_val, uls_val, url_val])


if __name__ == "__main__":
    timedRun(parser(50))
