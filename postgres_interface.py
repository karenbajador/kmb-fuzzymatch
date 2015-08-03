

from pg_auth_config import POSTGRESS_HOST, \
    POSTGRESS_PORT, POSTGRESS_USERNAME, \
    POSTGRESS_PASSWORD, POSTGRESS_DB

import psycopg2    


class PostgresInterface():

    def __init__(self):
    	self.host = POSTGRESS_HOST
    	self.port = POSTGRESS_PORT
    	self.user_name = POSTGRESS_USERNAME
    	self.password = POSTGRESS_PASSWORD
    	self.db_name = POSTGRESS_DB
    	self.conn = psycopg2.connect(database=self.db_name, 
    		user=self.user_name, 
    		password=self.password, 
    		host=self.host, 
    		port=self.port)


    def get_record_match(self, company_name, company_keywords_list, country, territory=""):
    	cur = self.conn.cursor()
    	
    	company_name_like = ' or '.join(("lower(company_name) like %s" for keyword in company_keywords_list if len(keyword) > 2))

    	sql = "select company_id, lower(company_name), group_id from crm.company_denorm_info where country = '{}'".format(country)

    	if len(territory) > 0:
    		sql += " and territory = '{}'".format(territory)

    	if len(company_name_like) > 0:
    		sql += " and (({}) OR lower(company_name) like %s)".format(company_name_like)
    	else:	
    		sql += " and lower(company_name) like %s".format(company_name)


    	# print(sql)
    	# print(list('%{}%'.format(keyword) for keyword in company_keywords_list) + ['%{}%'.format(company_name)])
    	

    	cur.execute(sql,list('%{}%'.format(keyword) for keyword in company_keywords_list if len(keyword) > 2) + ['%{}%'.format(company_name)])

    	rows = cur.fetchall()

    	return rows
    	

    	


