from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# print (" ")

# word_1 = "this is a test"
# word_2 = "this is a test!"

# print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))
# print("partial_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.partial_ratio(word_1, word_2))))

# print (" ")

# word_1 = "fuzzy wuzzy was a bear"
# word_2 = "wuzzy fuzzy was a bear"

# print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))
# print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))


# print (" ")

# word_1 = "fuzzy was a bear"
# word_2 = "fuzzy fuzzy was a bear"

# print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
# print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))

# print (" ")





# choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]

# print ("choices: {}".format(choices))

# keyword = "new york jets"
# limit = 2

# print ("process.extract *keyword={} limit {}* : {}".format(keyword, str(limit), str(process.extract(keyword, choices, limit=limit))))

# keyword = "cowboys"

# print ("process.extractOne *keyword={}* : {}".format(keyword, str(process.extractOne(keyword, choices))))




# keyword = "Al Jaber Group LLC"
# choices = ["Al Jaber Group LLC", "AL Jaber Group", "Al Jaber Brothers Hospitality / AL JABER HOLDING COMPANY (AL Jaber Group)"]
# print (" ")
# print ("choices: {}".format(choices))
# print ("process.extractOne *keyword={}* : {}".format(keyword, str(process.extractOne(keyword, choices))))
# print ("process.extract *keyword={} limit {}* : {}".format(keyword, str(limit), str(process.extract(keyword, choices, limit=limit))))
# print ("process.extract *keyword={}* : {}".format(keyword, str(process.extract(keyword, choices))))
# print (" ")

# keyword = "MAPCO L.L.C."
# choices = ["MAPCO INC", "MAPCO L L C", "MAPCO (Gravure Printing)", "MAPCO (Gravure Printing)", "Arab Fertilizers & Chemicals Industries ( KEMAPCO )","MAPCO","Mapco Fertilizer Industries FZC"]
# print (" ")
# print ("choices: {}".format(choices))
# print ("process.extractOne *keyword={}* : {}".format(keyword, str(process.extractOne(keyword, choices))))
# print ("process.extract *keyword={} limit {}* : {}".format(keyword, str(limit), str(process.extract(keyword, choices, limit=limit))))
# print ("process.extract *keyword={}* : {}".format(keyword, str(process.extract(keyword, choices))))
# print (" ")





# keyword = "Thyssenkrupp Industries And Services Qatar Doha"
# choices = ["Thyssenkrupp Elevator Doha", "Thyssenkrupp Xervon Dammam", "ThyssenKrupp Xervon Berlin", "ThyssenKrupp GfT Bautechnik Germany", \
# 	"ThyssenKrupp Bautechnik", "ThyssenKrupp Dubai","ThyssenKrupp Materials France","Thyssenkrupp Elevator Amman", \
# 	"ThyssenKrupp Elevator Shuaib Trading Co." ]

# #choices = ["x"]	
# print (" ")
# print ("choices: {}".format(choices))
# print ("process.extractOne *keyword={}* : {}".format(keyword, str(process.extractOne(keyword, choices))))
# print ("process.extract *keyword={} limit {}* : {}".format(keyword, str(limit), str(process.extract(keyword, choices, limit=limit))))
# print ("process.extract *keyword={}* : {}".format(keyword, str(process.extract(keyword, choices))))
# print (" ")


# print (" ")

# word_1 = "Thyssenkrupp Industries And Services Qatar Doha"
# word_2 = "Thyssenkrupp Elevator Doha"

# print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
# print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))
# print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))

# print (" ")

# word_2 = "Thyssenkrupp Xervon Dammam"

# print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
# print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))
# print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))

# print (" ")



# word_1 = "National Air Navigation Services (Nansc) Cairo"
# word_2 = "Nansceg Cairo"

# print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
# print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))
# print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))

# print (" ")

# word_1 = "Alexandria Electricity Distribution"
# word_2 = "nansceg cairo Egypt"

# print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
# print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))
# print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))

# print (" ")





company_names = [ 

	["",""],
	["",""],

	["",""],					

	["al ghaith holdings","al ghaith oilfield supplies"],
	["belhasa six construct company llc","abu dhabi construction company"],
	["parsons international limited","parsons corporation"],
	["abu dhabi national carpet factory","abu dhabi carpets factory"],

	["nmc special medical services ","nmc speciality hospital / nmc medical trading"],
	["parker hannifin united arab emirates","united emirates"],
	["gibca trading & contracting company - w l l","gibca crushing and quarry operations company"],
	["automatic system corporation","automatic vending services company l l c"],
	["baynunah well pipes factory limited","baynunah laboratories"],
	["al sultan cement factory (adic)","al sultan advanced medical clinics"],
	["hotel inter-continental abu dhabi","intercontinental hotel - abu dhabi"],
	["al bawardi group","al bawardi legal consultants"],
	["aldar sorouh properties pjsc.","aldar properties"],

	["national takaful co pjsc","takaful"],
	["methaq takaful insurance co","takaful"],
	["gulf ready mix","transgulf ready mix concrete company"],
	["china airlines","china machinery & electronics products exhibition centre"],
	["future pipes industrial company - w l l","future pipes industries abu dhabi"],

	["parker hannifin united arab emirates","presidential flight, united arab emirates"],
	["sybase products middle east","sybase middle east"],
	["habib bank limited","habib rafeeq limited(hrl)"],
	["al jaber transport & general contracting llc","al jaber aviation"],
	["al jaber l e g t engineering & contracting (alec) l l c","al jaber aviation"],
	["al nasser holdings","al nasser and al masri trading company"],
	["central motors & equipment llc","central perk"],
	["eastern bechtel co ltd","eastern bldg materials"],
	["credit suisse representative office","credit agricole (asset management)"],
	["gulf space petroleum equipment","gulf aerospace company"],
	["al diar gulf hotel and resort","emirates park resort - abu dhabi"],
	["lucherini association ing arch consulting","electraking fzc"],
	["al hamad general contracting est","hamad autism center"],
	["nexans france - abu dhabi","the invest in france agency -- middle east"],

	["two four 54 -fz - l l c","twofour54"],
	["transco abu dhabi transmission & despatch company","abu dhabi transmission & despatch co. ( transco)"],
	["cegelec uae","cegelec abu dhabi"],
	["al hikma development company psc","hikma medical center"],

	["al ramz securities llc","al ramz capital"],
	["belmour trading agencies establishment","medik trading agencies estb."],
	["arabtec holding pjsc","arabtec auh"],
	["wintershall middle east gmbh-abu dhabi","integraph abu dhabi"],









	



	



]


for names in company_names:
	if names[0] and names[1]:

		print("{} : {}".format(names[0], names[1]))

		#print("weighted token set ratio : {}".format(str(fuzz.weighted(names[0], names[1]))))
		#print("weighted partial ratio : {}".format(str(fuzz.weighted_2(names[0], names[1]))))
		print(">>>>> weighted 3 partial ratio 50 : {}".format(str(fuzz.weighted_3(names[0], names[1], total_weight=50))))
		print(">>>>> weighted 4 partial ratio 50 : {}".format(str(fuzz.weighted_4(names[0], names[1], total_weight=50))))


		print("token set ratio  : {}".format(str(fuzz.token_set_ratio(names[0], names[1]))))
		print("partial ratio  : {}".format(str(fuzz.partial_ratio(names[0], names[1]))))
		print(" ratio : {}".format(str(fuzz.ratio(names[0], names[1]))))
		print (" ")












































