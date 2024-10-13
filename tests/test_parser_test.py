import os
from src.deserializer import Deserializer

o = open("out.txt", 'w', encoding="utf-8")
for root, folder, files in os.walk("./ArknightsGameData_YoStar/en_US/gamedata/story"):
	for f in files:
		if not f.endswith(".txt"): continue
		# d:Deserializer = Deserializer("../ArknightsGameData_YoStar/en_US/gamedata/story/obt/main/level_main_00-01_beg.txt")
		d:Deserializer = Deserializer(root+"/"+f)
		d.deserialize()
		for i in d.instructions:
			o.write(i.__str__()+"\n")