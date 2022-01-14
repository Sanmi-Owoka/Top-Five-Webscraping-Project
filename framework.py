import requests.exceptions
from web_scrape import WebScrape
from web_processing import WebProcess
from web_word_counter import WordCounter
from bar_chart_plot import BarChart
from pie_chart_plot import PieChart


web_scrape = WebScrape()
web_process = WebProcess()
word_counter = WordCounter()
bar_chart = BarChart()
pie_chart = PieChart()


class Framework:
    """Below is where the various classes already instantiated are called """
    def call(self):
        try:
            URL = input("Enter a website to analyze: ")
            URL_scrape = web_scrape.scrape(URL)
            URL_process = web_process.text_process(URL_scrape)
            word_count = word_counter.word_counter(URL_process)
            bar_chart.plot_bar_chart(word_count)
            try:
                pie_chart.plot_pie_chart(word_count)
            except ValueError:
                return
            URL_store = open("log.csv", "a")
            URL_store.write(f"{URL}\n")
            URL_store.close()
            """EXCEPTIONS"""
        except requests.exceptions.MissingSchema:
            print(f"Invalid Web URL Format, you entered '{URL}'")
        except requests.exceptions.ConnectTimeout:
            print("Sorry Network issues")
        except requests.exceptions.InvalidSchema:
            print(f"Invalid Web URL Format, you entered '{URL}'")
        except requests.exceptions.InvalidURL:
            print(f"You entered {URL},  Enter a valid website")
        except requests.exceptions.ConnectionError:
            print(f"You entered {URL},  Enter a valid website")
            
        


