if [[ ! -d "data" ]]; then
	mkdir data
fi
cd data

# echo "audition certificates"
# file="msnotesannotator_audition_certificates_data-master(1)(2).zip"
# wget "https://www.fdr.uni-hamburg.de/record/13525/files/$file"
# unzip $file

echo "manuscript cultures"
if [[ ! -d "manuscript_cultures" ]]; then
	mkdir manuscript_cultures  
fi
cd manuscript_cultures
for ((i = 1; i <= 19; i++)); do
	echo "manuscript cultures $i"
	wget "https://www.csmc.uni-hamburg.de/publications/mc/mc$i/mc$i-full.pdf"
done
