import pandas as pd
from helpers.decorator import CreateDirectory
<<<<<<< HEAD
from settings import DESTINATION_FOLDER, COLUMNS, SOURCE_FOLDER
=======
from settings import DESTINATION_FOLDER, SOURCE_FOLDER, COLUMNS
>>>>>>> 1f6d2b7aa7d005689e0d650ed2fdc92db82beb88

class PandaDataFrame():

    def __init__(self, pd_file):
        
        class myIOError(Exception): pass
        print ("Loading Data...")

        

        try:
            #xls = pd.ExcelFile('files/' + pd_file)
<<<<<<< HEAD
            data = pd.read_csv(SOURCE_FOLDER+"/"+pd_file)
=======
            data = pd.read_csv(SOURCE_FOLDER + "/" + pd_file)
>>>>>>> 1f6d2b7aa7d005689e0d650ed2fdc92db82beb88
        except IOError as e:
                raise myIOError('Caching error: %s' % e)  

        #data = xls.parse(xls.sheet_names[0])
        self._pd_file = pd_file
        
        print ("Loaded Data!")

        #Generate DataFrame including relevant columns
        df = pd.DataFrame(data, columns=COLUMNS)

        self._new_df = df

        self._new_df["Match Status"] = ""
        self._new_df["CRM Company Name"] = ""
        self._new_df["CRM Group ID"] = ""
        self._new_df["CRM Company ID"] = ""



    @property
    def df(self):
    	return self._new_df


    def update_df(self,index, best_match, best_score):
        if best_score >= 75:
            match_status = 'high'
            ## Add best match columns
        elif best_score >= 70:
            match_status = 'medium'
            ## Add best match columns            
        elif best_score > 0:
            match_status = 'low'
            ## Add best match columns                        
        else:
            match_status = 'not matched'

        self._new_df['Match Status'][int(index)]=match_status+"="+str(best_score)
        self._new_df['CRM Company Name'][int(index)]=best_match.crm_company_name
        self._new_df['CRM Group ID'][int(index)]=best_match.crm_group_id
        self._new_df['CRM Company ID'][int(index)]=best_match.crm_company_id

        self.save()


    
    @CreateDirectory(DESTINATION_FOLDER)
    def save(self):
        # writer_orig = pd.ExcelWriter('processed_files/'+self._pd_file, engine='xlsxwriter')
        # self._new_df.to_excel(writer_orig, index=False, sheet_name='report')
        #writer_orig = pd.ExcelWriter('processed_files/'+self._pd_file, engine='xlsxwriter')
        self._new_df.to_csv(DESTINATION_FOLDER+"/"+self._pd_file, index=False)
        #writer_orig.save()




 


    
