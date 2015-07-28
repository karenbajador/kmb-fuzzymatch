from fuzzywuzzy import fuzz
from fuzzywuzzy import process


print (" ")

word_1 = "this is a test"
word_2 = "this is a test!"

print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))
print("partial_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.partial_ratio(word_1, word_2))))

print (" ")

word_1 = "fuzzy wuzzy was a bear"
word_2 = "wuzzy fuzzy was a bear"

print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))
print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))


print (" ")

word_1 = "fuzzy was a bear"
word_2 = "fuzzy fuzzy was a bear"

print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))

print (" ")





choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]

print ("choices: {}".format(choices))

keyword = "new york jets"
limit = 2

print ("process.extract *keyword={} limit {}* : {}".format(keyword, str(limit), str(process.extract(keyword, choices, limit=limit))))

keyword = "cowboys"

print ("process.extractOne *keyword={}* : {}".format(keyword, str(process.extractOne(keyword, choices))))




keyword = "Al Jaber Group LLC"
choices = ["Al Jaber Group LLC", "AL Jaber Group", "Al Jaber Brothers Hospitality / AL JABER HOLDING COMPANY (AL Jaber Group)"]
print (" ")
print ("choices: {}".format(choices))
print ("process.extractOne *keyword={}* : {}".format(keyword, str(process.extractOne(keyword, choices))))
print ("process.extract *keyword={} limit {}* : {}".format(keyword, str(limit), str(process.extract(keyword, choices, limit=limit))))
print ("process.extract *keyword={}* : {}".format(keyword, str(process.extract(keyword, choices))))
print (" ")

keyword = "MAPCO L.L.C."
choices = ["MAPCO INC", "MAPCO L L C", "MAPCO (Gravure Printing)", "MAPCO (Gravure Printing)", "Arab Fertilizers & Chemicals Industries ( KEMAPCO )","MAPCO","Mapco Fertilizer Industries FZC"]
print (" ")
print ("choices: {}".format(choices))
print ("process.extractOne *keyword={}* : {}".format(keyword, str(process.extractOne(keyword, choices))))
print ("process.extract *keyword={} limit {}* : {}".format(keyword, str(limit), str(process.extract(keyword, choices, limit=limit))))
print ("process.extract *keyword={}* : {}".format(keyword, str(process.extract(keyword, choices))))
print (" ")





keyword = "Thyssenkrupp Industries And Services Qatar Doha"
choices = ["Thyssenkrupp Elevator Doha", "Thyssenkrupp Xervon Dammam", "ThyssenKrupp Xervon Berlin", "ThyssenKrupp GfT Bautechnik Germany", \
	"ThyssenKrupp Bautechnik", "ThyssenKrupp Dubai","ThyssenKrupp Materials France","Thyssenkrupp Elevator Amman", \
	"ThyssenKrupp Elevator Shuaib Trading Co." ]

#choices = ["x"]	
print (" ")
print ("choices: {}".format(choices))
print ("process.extractOne *keyword={}* : {}".format(keyword, str(process.extractOne(keyword, choices))))
print ("process.extract *keyword={} limit {}* : {}".format(keyword, str(limit), str(process.extract(keyword, choices, limit=limit))))
print ("process.extract *keyword={}* : {}".format(keyword, str(process.extract(keyword, choices))))
print (" ")


print (" ")

word_1 = "Thyssenkrupp Industries And Services Qatar Doha"
word_2 = "Thyssenkrupp Elevator Doha"

print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))
print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))

print (" ")

word_2 = "Thyssenkrupp Xervon Dammam"

print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))
print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))

print (" ")



word_1 = "National Air Navigation Services (Nansc) Cairo"
word_2 = "Nansceg Cairo"

print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))
print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))

print (" ")

word_1 = "Alexandria Electricity Distribution"
word_2 = "nansceg cairo Egypt"

print("token_sort_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_sort_ratio(word_1, word_2))))
print("token_set_ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.token_set_ratio(word_1, word_2))))
print("ratio 1 *{}* : {}".format(word_1 + " & " + word_2, str(fuzz.ratio(word_1, word_2))))

print (" ")
