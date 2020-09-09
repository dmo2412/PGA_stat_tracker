import pandas as pd

class ImportExcelToCSV:
    def __init__(self):
        self.import_masters()
        self.import_usopen()
        self.import_pga()
        self.import_open_championship()

    def import_masters(self):
        self.data_xls = pd.read_excel('masters_stats_2010_to_2019.xlsx', 'Sheet1', index_col=None) #Change file name to match file name in Scraping/masters_scrape.py
        self.data_xls.to_csv('masters.csv', encoding='utf-8')

    def import_usopen(self):
        self.data_xls = pd.read_excel('us_open_stats_2010_to_2019.xlsx', 'Sheet1', index_col=None) #Change file name to match file name in Scraping/us_open_scrape.py
        self.data_xls.to_csv('usopen.csv', encoding='utf-8')

    def import_pga(self):
        self.data_xls = pd.read_excel('pga_stats_2010_to_2019.xlsx', 'Sheet1', index_col=None) #Change file name to match file name in Scraping/pga_scrape.py
        self.data_xls.to_csv('pga.csv', encoding='utf-8')

    def import_open_championship(self):
        self.data_xls = pd.read_excel('open_championship_stats_2010_to_2019.xlsx', 'Sheet1', index_col=None) #Change file name to match file name in Scraping/open_championship_scrape.py
        self.data_xls.to_csv('openchampionship.csv', encoding='utf-8')

if __name__ == '__main__':
    imp = ImportExcelToCSV()
