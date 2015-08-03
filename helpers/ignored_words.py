import re

class IgnoreWords():

    def __init__(self):
        
        self.ignored_words = ["company", \
                            "of", \
                            "the", \
                            "group", \
                            "limited", \
                            "inc", \
                            "inc.", \
                            "hospital", \
                            "hospitals", \
                            "embassy", \
                            "university", \
                            "bank", \
                            "corporation", \
                            "corp", \
                            "embassy", \
                            "factory", \
                            "ltd", \
                            "co", \
                            "شركة", \
                            "مستشفى", \
                            "بنك", \
                            "مدرسة", \
                            "توظيف", \
                            "recruitment", \
                            "est", \
                            "limited", \
                            "client", \
                            "leading", \
                            "companies", \
                            "for", \
                            "star", \
                            "hotel", \
                            "services", \
                            "llc", \
                            "l.l.c.", \
                            "al", \
                            "-", \
                            "co", \
                            "in", \
                            "&", \
                            "pty", \
                            "pte", \
                            "and", \
                            "international", \
                            "consulting", \
                            "consultants", \
                            "trading", \
                            "establishment", \
                            "properties", \
                            "engineers", \
                            "technologies", \
                            "pjsc", \
                            "investment", \
                            "investments", \
                            "engineering", \
                            "insurance", \
                            "national", \
                            "psc", \
                            "contracting", \
                            "est", \
                            "securities", \
                            "holding", \
                            "holdings", \
                            "enterprises", \
                            "centre", \
                            "construction", \
                            "architects", \
                            "house", \
                            "partners", \
                            "exchange", \
                            "property", \
                            "fze", \
                            "wll", \
                            "w.l.l.", \
                            "pjsc", \
                            "psc", \
                            "p.s.c", \
                            ]
        self.ignored_phrase = ["middle east", \
                            "information technology", \
                            "sports and cultural club", \
                            "medical supplies", \
                            "real estate", \
                            "insurance brokers", \
                            "general contracting", \
                            "general services", \
                            "facility management", \
                            "facilities management", \
                            "construction company", \
                            "technology services", \
                            "hotels and resorts", \
                            "building contracting", \
                            "transport and general contracting", \
                            "building maintenance", \
                            "international technology", \
                            "abu dhabi", \
                            "development and construction", \
                            "mechanical works", \
                            "oilfield services", \
                            "information services", \
                            "management services", \
                            "petroleum services", \
                            "emirates contracting", \
                            "property management", \
                            "general trading", \
                            "building services", \
                            "business group", \
                            "development company", \
                            ]                            

    def return_keyword_lists(self,company_name):


        clean_company_name = company_name

        for phrase in self.ignored_phrase:
            clean_company_name = re.sub(r"\b%s\b" % phrase, "", clean_company_name)
            
        clean_company_name = re.sub(r"^\w\b\s|\b\w\b(\s|$)"," ",clean_company_name, flags=re.IGNORECASE)
        clean_company_name = re.sub(' +',' ',clean_company_name).strip()
        

        return set(keyword for keyword in clean_company_name.split(" ") if keyword not in self.ignored_words)