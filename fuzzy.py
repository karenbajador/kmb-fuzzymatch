import re
import sys
import collections
from fuzzywuzzy import fuzz
from postgres_interface import PostgresInterface
from helpers.ignored_words import IgnoreWords
from data_frame import PandaDataFrame
<<<<<<< HEAD
from settings import SOURCE_FOLDER
=======
>>>>>>> 1f6d2b7aa7d005689e0d650ed2fdc92db82beb88


def extract_row_generator(df):
	for index, row in df.iterrows():
		yield (index,row)

def clean(company_name):
	## Clean spaces
	company_name = re.sub(r'([^\s\+\&\w])|_+', '', company_name) 
	return re.sub(' +',' ',company_name)		

# Specify the Employee namedtuple.
Match = collections.namedtuple("Match", ["crm_company_id", "crm_company_name", "crm_group_id", "score"])

def get_fuzzy_match_generator(crm_results, excel_company_name):
	for result in crm_results:
		yield Match(crm_company_id = result[0],crm_company_name = result[1],crm_group_id = result[2], score=fuzz.ratio(excel_company_name, result[1]))



### MAIN ###

def main(argv):

	pd_file = argv[1]
	country = argv[2]
	territory = argv[3]

	ignore_words_cls = IgnoreWords()
	postgres_interface_cls = PostgresInterface()
<<<<<<< HEAD
	df_cls = PandaDataFrame(SOURCE_FOLDER + "/" + pd_file)	
=======
	df_cls = PandaDataFrame(pd_file)	
>>>>>>> 1f6d2b7aa7d005689e0d650ed2fdc92db82beb88

	for extracted_row in extract_row_generator(df_cls.df):
		index, row =  extracted_row

		## Clean company_name
		company_name = clean(row["Company Name"]).lower()
		
		## Ignore words
		company_keywords_list = ignore_words_cls.return_keyword_lists(company_name)

		## Find matches in DB using keywords , country and territory
		crm_results = postgres_interface_cls.get_record_match(company_name, company_keywords_list, country, territory)


		## Fuzzy match 
		best_match = Match(crm_company_id = "",crm_company_name = "",crm_group_id = "", score="")
		best_score = 0

		for match in get_fuzzy_match_generator(crm_results, row["Company Name"]):

			if match.score >= best_score:
				if match.score > best_score:
					best_match = {}
					best_score = match.score
				best_match = match

		
		## Test Prints
		# if best_score >= 75: 
		# 	#print ("keword_list: {} + crm_results count: {}".format(company_keywords_list,len(crm_results)))
		# 	print("{} => best_match: {} => '{}'".format(best_score, row["Company Name"], best_match))		
		print("{} => best_match: {} => '{}'".format(best_score, row["Company Name"], best_match))
		
		
		### Generate new file
		df_cls.update_df(index, best_match, best_score)



if __name__ == "__main__":
   main(sys.argv)







