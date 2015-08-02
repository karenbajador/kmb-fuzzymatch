#### CHECK IF UPLOAD FILE EXISTS (upload.txt)
echo "Opening fuzzy_list.txt..."

if [ ! -f fuzzy_list.txt ]; then
    echo -ne "\nfuzzy_list.txt does not exist! Exiting... \n"
    exit
fi

echo "Reading file..."


while read line           
do
	IFS=';' read -a params <<< "${line}"
	
	
	if [[  "$line" != "#"* ]] 
	then
		echo python fuzzy.py "${params[0]}" "${params[1]}" "${params[2]}"
		python fuzzy.py "${params[0]}" "${params[1]}" "${params[2]}"
	fi
	
	
done < fuzzy_list.txt


echo "Done"

