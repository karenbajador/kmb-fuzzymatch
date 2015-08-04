import unittest
from fuzzy import *
from helpers.ignored_words import IgnoreWords

class TestFuzzy(unittest.TestCase):
    


    def test_clean_company_name(self):
        """
        Clean Company Name
        """
        self.assertEqual("Al Jaber L E G T Engineering & Contracting Alec L L C", clean("Al Jaber L E G T Engineering & Contracting (Alec) L L C"))
        self.assertEqual("G.I.T Fze", clean("G.I.T Fze"))
        self.assertEqual("United Carrier Company L L C", clean("United Carrier Company - L L C"))
        self.assertEqual("Larsen & Toubro Limited Ecc Construction Group Abu Dhabi", clean("Larsen & Toubro Limited - Ecc Construction Group - Abu Dhabi"))
        self.assertEqual("ThyssenKrupp Xervon U.A.E. L.L.C.", clean("ThyssenKrupp Xervon U.A.E. - L.L.C."))
        self.assertEqual("Autochim Systems Abu Dhabi Asad L L C", clean("Autochim Systems - Abu Dhabi - (Asad) L L C"))
        self.assertEqual("Rolf Jensen & Associates International Inc", clean("Rolf Jensen & Associates, International, Inc"))
        self.assertEqual("M+W Singapore Pte Ltd Abu Dhabi", clean("M+W Singapore Pte Ltd - Abu Dhabi"))
        self.assertEqual("Smith International Inc.", clean("Smith International Inc.,"))
        self.assertEqual("Shokri Hassan Trading Co. L.L. C.", clean("Shokri Hassan Trading Co. (L.L. C.)"))
        self.assertEqual("Dst GlobalMiddle East Limited", clean("Dst Global(Middle East Limited)"))

    def test_ignore_words(self):
        """
        Ignore words. Returned keywords list are used to query similar companies in database to narrow number of records to apply fuzzy match against.
        """
        ignore_words_cls = IgnoreWords()


        self.assertEqual(sorted(["hada", "hada general trading","tradingl.l.c"]), sorted(ignore_words_cls.return_keyword_lists("Hada General TradingL.L.C".lower())))
        self.assertEqual(sorted(["dst","globalmiddle", "east", "dst globalmiddle east"]), sorted(ignore_words_cls.return_keyword_lists("Dst GlobalMiddle East Limited".lower())))
        self.assertEqual(sorted(["jacky's","jacky's gulf"]), sorted(ignore_words_cls.return_keyword_lists("Jacky's Gulf Fze".lower())))
        self.assertEqual(sorted(["emirates trading"]), sorted(ignore_words_cls.return_keyword_lists("Emirates Trading Est.".lower())))
        self.assertEqual(sorted(["mena","mena business services"]), sorted(ignore_words_cls.return_keyword_lists("Mena Business Services Fz-Llc".lower())))
        self.assertEqual(sorted(["shokri","hassan","shokri hassan trading"]), sorted(ignore_words_cls.return_keyword_lists("Shokri Hassan Trading Co. L.L. C.".lower())))
        self.assertEqual(sorted(["danube","bulding","danube bulding materials"]), sorted(ignore_words_cls.return_keyword_lists("Danube Bulding Materials Fzco.".lower())))
        self.assertEqual(sorted(["alokozay","alokozay international"]), sorted(ignore_words_cls.return_keyword_lists("Alokozay International Ltd.".lower())))
        self.assertEqual(sorted(["malcolm","pirnie","malcolm pirnie middle east"]), sorted(ignore_words_cls.return_keyword_lists("Malcolm Pirnie Middle East FZC".lower())))
        self.assertEqual(sorted(["ojaco","ojaco engineering"]), sorted(ignore_words_cls.return_keyword_lists("Ojaco Engineering Co.".lower())))
        self.assertEqual(sorted(["jaber","alec","al jaber l e g t engineering & contracting alec"]), sorted(ignore_words_cls.return_keyword_lists("Al Jaber L E G T Engineering & Contracting Alec L L C".lower())))
        self.assertEqual(sorted(["arabtec","arabtec holding"]), sorted(ignore_words_cls.return_keyword_lists("Arabtec Holding PJSC".lower())))
        self.assertEqual(sorted(["advanced","pipes","casts","advanced pipes and casts company"]), sorted(ignore_words_cls.return_keyword_lists("Advanced Pipes and Casts Company W.L.L.".lower())))
        self.assertEqual(sorted(["smith","smith international"]), sorted(ignore_words_cls.return_keyword_lists("Smith International Inc.".lower())))
        self.assertEqual(sorted(["thyssenkrupp","xervon","thyssenkrupp xervon u.a.e."]), sorted(ignore_words_cls.return_keyword_lists("ThyssenKrupp Xervon U.A.E. L.L.C.".lower())))
        self.assertEqual(sorted(["noor","al noor hospitals group",]), sorted(ignore_words_cls.return_keyword_lists("Al Noor Hospitals Group PLC".lower())))
        self.assertEqual(sorted(["g.i.t"]), sorted(ignore_words_cls.return_keyword_lists("G.I.T Fze".lower())))
        self.assertEqual(sorted(["linde","linde engineering middle east",]), sorted(ignore_words_cls.return_keyword_lists("Linde Engineering Middle East LLC".lower())))
        self.assertEqual(sorted(["emco","maintenance","engineering maintenance company emco"]), sorted(ignore_words_cls.return_keyword_lists("Engineering Maintenance Company EMCO".lower())))
        self.assertEqual(sorted(["moherbie","thermoplast","al moherbie thermoplast"]), sorted(ignore_words_cls.return_keyword_lists("Al Moherbie Thermoplast LLC".lower())))
        self.assertEqual(sorted(["gibca","gibtek", "gibca information technology gibtek"]), sorted(ignore_words_cls.return_keyword_lists("Gibca Information Technology L L C Gibtek".lower())))
        self.assertEqual(sorted(["y&r","y&r abu dhabi"]), sorted(ignore_words_cls.return_keyword_lists("Y&R Abu Dhabi".lower())))
        self.assertEqual(sorted(["tolico","tolico trading oilfield services"]), sorted(ignore_words_cls.return_keyword_lists("Tolico Trading Oilfield Services L L C".lower())))

        
    def test_fuzzy_match(self):
        """
        Fuzzy match. Returns a generator.
        """

        best_match = Match(crm_company_id = "",crm_company_name = "",crm_group_id = "", score="")
        best_score = 0

        #Test 1
        crm_results = [
                        [3451971,"premco ready mix",1484195],
                        [45345643,  "emco (engineering maintananace company)", 1594067],
                    ]
        best_match, best_score = call_fuzzy_match_generator(best_match, best_score, "engineering maintenance company emco".lower(), crm_results)
        self.assertEqual("emco (engineering maintananace company)", best_match.crm_company_name)

        #Test 2
        best_match = Match(crm_company_id = "",crm_company_name = "",crm_group_id = "", score="")
        best_score = 0        
        crm_results = [
                        [27038,"gulf cost petroleum projects technical services",78049],
                        [3462518,"china petroleum pipeline engineering corporation (cppe)",1501536],
                        [79813,"the petroleum institute",41647],
                        [3122385,"wells petroleum services co.",1053943],
                        [3457413,"ittihad integrated petroleum and chemical iipc",1496523],
                        [29299,"national petroleum construction company (npcc)",5136],
                        [3375374,"china petroleum engineering & construction corporation (cpecc)",1342610],
                        [27103,"abu dhabi petroleum ports operating company (irshad) ex. adppoc",49198],
                    ]
        best_match, best_score = call_fuzzy_match_generator(best_match, best_score, "National Petroleum Construction Company".lower(), crm_results)
        self.assertEqual("national petroleum construction company (npcc)", best_match.crm_company_name)

        #Test 3
        best_match = Match(crm_company_id = "",crm_company_name = "",crm_group_id = "", score="")
        best_score = 0        
        crm_results = [
                        [3037284,"noor islamic finance",1004294],
                        [66055,"noor capital",288022],
                        [540314,"noorlan enviro systems",601301],
                        [54353,"al noor hospital",1031895],
                        [3503664,"the spa - rak hospitals",1679134],
                        [84726,"zulekha hospitals",1520309],
                    ]
        best_match, best_score = call_fuzzy_match_generator(best_match, best_score, "Al Noor Hospitals Group PLC".lower(), crm_results)
        self.assertEqual("al noor hospital", best_match.crm_company_name)




        
        
if __name__ == '__main__':
    unittest.main()