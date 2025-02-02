import os
from src.deserializer import Deserializer
from src.instructions import *
import pytest

import json # type: ignore

# o = open("out.txt", 'w', encoding="utf-8")
# # open("./ArknightsGameData_YoStar/en_US/gamedata/story/activities/act25side/level_act25side_01_beg.txt")
# d:Deserializer = Deserializer("./ArknightsGameData_YoStar/en_US/gamedata/story/activities/act25side/level_act25side_01_beg.txt")
# d.deserialize()
# dta: list[dict[str, str | None | float]] = []
# for i in d.instructions:
# 	if isinstance(i, (RawText, SpokenText, Dialog, dialog, Subtitle)):
# 		if i.text is None:
# 			continue

# 		speaker = "narrator"
# 		if isinstance(i, (Dialog, dialog)):
# 			speaker: str | None = i.head
# 		elif isinstance(i, (RawText, SpokenText)):
# 			speaker = i.name
# 		else:
# 			pass
		
# 		dta.append({
# 			"text": i.text,
# 			"speaker": speaker,
# 		})
# 	elif isinstance(i, (Delay, delay)):
# 		if i.time is None:
# 			continue
# 		dta.append({
# 			"text": None,
# 			"speaker": None,
# 			"delay": i.time
# 		})
# json.dump(dta, o)
# @pytest.Function

def test_parse() -> None:
	o = open("./tests/out.txt", 'w', encoding="utf-8")
	for root, _, files in os.walk("./ArknightsGameData_YoStar/en_US/gamedata/story"):
		for f in files:
			o.write(f+"\n")
			if not f.endswith(".txt"): continue
			d:Deserializer = Deserializer(root + "/" + f)
			d.deserialize()
			for i in d.instructions:
				o.write(i.__str__()+"\n")