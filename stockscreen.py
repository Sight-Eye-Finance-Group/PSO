import stock_scraper as ss
import pandas as pd

# Get list of symbols from the csv file with stock symbols, names and industries
def createList():
	df = pd.read_csv("sp500-constituents.csv")
	stock_list = df['Symbol'].values
	return stock_list

def main():
  	# List of companies and list of indicators
	stock_list = createList()
	interested = ['Market Cap (intraday)', 'Return on Equity', 'Revenue', 'Quarterly Revenue Growth', 
	'Operating Cash Flow', 'Total Cash', 'Total Debt', 'Current Ratio', '52-Week Change',
	'Avg Vol (3 month)', 'Avg Vol (10 day)', '% Held by Insiders']
  
  	# Create new pandas data frame to store the info
	df = pd.DataFrame(columns=interested)
  
  	# iterate through stock list and indicators, aquiring data and storing in dataframe
	for each_stock in stock_list:
		tech = ss.scrape_yahoo(each_stock)
		for ind in interested:	
			try:
				df.at[each_stock, ind] = tech[ind]
			except Exception as e:
				print('Failed, exception: ', str(e))
   		# print companies as they're scraped to keep track of progress
		print("DONE- " + each_stock)
