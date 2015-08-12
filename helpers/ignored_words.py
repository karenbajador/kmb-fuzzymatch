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
                            "ltd.", \
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
                            "hotels", \
                            "services", \
                            "llc", \
                            "l.l.c.", \
                            "l.l.c", \
                            "al", \
                            "-", \
                            "co.", \
                            "in", \
                            "&", \
                            "pty", \
                            "pte", \
                            "and", \
                            "international", \
                            "consulting", \
                            "consultants", \
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
                            "fzc", \
                            "wll", \
                            "w.l.l.", \
                            "psc", \
                            "p.s.c", \
                            "p.s.c.", \
                            "plc", \
                            "dubai", \
                            "oman", \
                            "egypt", \
                            "uae", \
                            "distribution", \
                            "concrete", \
                            "emirates", \
                            "bin", \
                            "industrial", \
                            "consult", \
                            "communications", \
                            "solutions", \
                            "fzco", \
                            "fzco.", \
                            "industries", \
                            "industry", \
                            "motors", \
                            "associates", \
                            "flowers", \
                            "advertising", \
                            "u.a.e.", \
                            "branch", \
                            "gold", \
                            "gulf", \
                            "computers", \
                            "petroleum", \
                            "fz-llc", \
                            "l.l.", \
                            "c.", \
                            "est.", \
                            "materials", \
                            "electronics", \
                            "management", \
                            "restaurant", \
                            "professional", \
                            "telecommunications", \
                            "electromechanical", \
                            "technology", \
                            "systems", \
                            "jewellery", \
                            "jewels", \
                            "bakery", \
                            "healthcare", \
                            "decor", \
                            "center", \
                            "trading", \
                            "networks", \
                            "network", \
                            "f.z.e", \
                            "development", \
                            "aviation", \
                            "worldwide", \
                            "shipping", \
                            "general", \
                            "fashion", \
                            "computers", \
                            "computer", \
                            "energy", \
                            "egency", \
                            "egencies", \
                            

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
                            "technology solutions", \
                            "hotels and resorts", \
                            "building contracting", \
                            "transport and general contracting", \
                            "transport & general contracting", \
                            "building maintenance", \
                            "general maintenance", \
                            "international technology", \
                            "abu dhabi", \
                            "saudi arabia", \
                            "development and construction", \
                            "pipeline construction", \
                            "mechanical works", \
                            "oilfield services", \
                            "oil services", \
                            "oil company", \
                            "information services", \
                            "management services", \
                            "petroleum services", \
                            "business services", \
                            "media services", \
                            "security services", \
                            "technical services", \
                            "emirates contracting", \
                            "property management", \
                            "general trading", \
                            "foodstuff trading", \
                            "building services", \
                            "business group", \
                            "development company", \
                            "power company", \
                            "steel company", \
                            "ready mix", \
                            "steel industries", \
                            "paper industries", \
                            "metal industries", \
                            "cement factory", \
                            "general contracting", \
                            "marine services", \
                            "palace hotel", \
                            "future energy", \
                            "law firm", \
                            "building materials", \
                            "building material", \
                            "trading est\.", \
                            "resources group", \
                            "travel agency", \
                            "travel and tour", \
                            "shipping agency", \
                            "electro mechanical", \
                            "human resources", \
                            "animation studio", \
                            "electrical engineering", \
                            "management consultancy", \
                            "marketing consultancy", \
                            "advocate and legal consultant", \
                            "data systems", \
                            ]
        
        self.abbr_corporate_types_b = [
                            "fze", \
                            "fzco", \
                            "fzc", \
                            "wll", \
                            "pjsc", \
                            "psc", \
                            "llc", \
                            "pty", \
                            "pte", \
                            "co", \
                            "ltd", \
                            "corp", \
                            "inc", \
                            "est", \
                            "plc", \
                            "limited", \
                            ]

        self.abbr_corporate_types = [
                            "w\.l\.l\.", \
                            "p\.s\.c", \
                            "l\.l\.c\.", \
                            "inc\.", \
                            "l l c", \
                            "l t d", \
                            "l\.l\.c", \
                            "co\.", \
                            "ltd\.", \
                            "\(l\.l\.c\.\)", \
                            "fz-llc", \
                            "l\.l\. c\.", \
                            "fzco\.", \
                            "est\.", \
                            "f\.z\.e", \
                            ]                                                        

    def return_keyword_lists(self,company_name):


        clean_company_name = company_name

        #remove ignored phrases
        # for phrase in self.ignored_phrase:
        #     clean_company_name = re.sub(r"\b%s\b" % phrase, "", clean_company_name)

        rx = re.compile(r"{}".format('|'.join(["\\b{}\\b".format(phrase) for phrase in self.ignored_phrase])))
        clean_company_name = rx.sub('', clean_company_name)

        #remove ignored words
        keywords_list = set(keyword for keyword in clean_company_name.split(" ") if keyword not in self.ignored_words and len(keyword)>1)

        #strip off just the abbrevated corporate type from the original company name
        #strip without boundary
        rx = re.compile(r"{}".format('|'.join(["{}".format(abbr) for abbr in self.abbr_corporate_types])))
        stripped_original_company_name = rx.sub('', company_name).strip()        
        #strip with boundary
        rx = re.compile(r"{}".format('|'.join(["\\b{}\\b".format(abbr) for abbr in self.abbr_corporate_types_b])))
        stripped_original_company_name = rx.sub('', stripped_original_company_name).strip()   

        stripped_original_company_name = re.sub(" +", " ", stripped_original_company_name)
        
        keywords_list.add(stripped_original_company_name)
        
        return keywords_list