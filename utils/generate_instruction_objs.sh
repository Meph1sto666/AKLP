
if [ -e utils/instruction_dump.json ]; then
	read -p "A dump exists, renew? [Y/n]" -n 1 -r
	echo
	if [[ ! $REPLY =~ ^[Yy]$ ]]
	then
		./venv/bin/python utils/ris_dump.py
	fi
fi

./venv/bin/python utils/classes_generator.py #dmp_to_classes

read -p "Class definitions have been generated, overwrite old ones? [y/N]" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
	mv utils/instructions.py src/instructions.py
else
	echo "Exiting..."
fi