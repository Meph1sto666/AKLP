import json
import os
import re
import typing
from json import loads

data: dict[str, dict[str, set[str]]] = {}

class SetEncoder(json.JSONEncoder):
    def default(self, o: set[typing.Any]) -> list[typing.Any] | typing.Any:
        if isinstance(o, set): # type: ignore
            return list(o)
        return json.JSONEncoder.default(self, o)

class LineParser():
	def __init__(self, raw: str) -> None:
		self.__raw:str = raw		
		self.line:str = raw.strip()
		self.instruction_type:str|None = None
		self.args:dict[str, typing.Any]|None = None
		self.parse()
		# print(self.instruction_type, self.args)

	def parse(self) -> None:
		found_meta:re.Match[str]|None = re.search(r"(?<=\[).*(?=\])", self.__raw)
		meta: str = found_meta.group() if found_meta else ""
		text: str = self.line.replace(meta, "", 1).strip(' []\n')
		args_list: typing.Iterator[re.Match[str]] = re.finditer(r"\w+(\s*)?=(\s*)?((\".+?\")|[^(,(\s*)?|(\s*)?,)\)\n\]]+)", meta)
		try:
			args:dict[str,float|int|str|None] = dict([[self.convert(c) for c in re.split(r"\s*=\s*", a.group(), 1)] for a in args_list]) # type: ignore
			e:float|int|str|None = args.pop('else', None)
			if not e is None:
				args["else_"] = e
			e:float|int|str|None = args.pop('from', None)
			if not e is None:
				args["from_"] = e
			
		except:
			print(re.finditer(r"\w+(\s*)?=(\s*)?((\".+?\")|[^(,(\s*)?|(\s*)?,)\)\n\]]+)", meta))
			raise ValueError
		found_type:re.Match[str]|None = re.search(r"\w+(?=\(?)", meta)
		self.instruction_type:str|None = found_type.group() if found_type else ""
		if text:
			args['text'] = text
		self.args = args
		if self.instruction_type == "name":
			self.instruction_type = "SpokenText"
		if self.instruction_type == "":
			self.instruction_type = "RawText"

		if data.get(self.instruction_type, None) is None:
			data[self.instruction_type] = dict([
					# (a[0], {"data_types":[type(a[1]).__name__]})
					(a[0], set([type(a[1]).__name__]))
					for a in args.items()
				])
		else:
			for a in args.items():
				try:
					data[self.instruction_type][a[0]].add(type(a[1]).__name__)
				except:
					data[self.instruction_type][a[0]] = set([type(a[1]).__name__])

	def convert(self, val:str) -> float | int | str | bool | None:
		try:
			return loads(val)
		except:
			return val

o = open("./utils/instruction_dump.json", 'w', encoding="utf-8")
for root, folder, files in os.walk("./ArknightsGameData_YoStar/en_US/gamedata/story"):
	for f in files:
		print(f)
		if not f.endswith(".txt"): continue
		with open(root+"/"+f, "r", encoding="utf-8") as file:
			for line in file:
				lp = LineParser(line)

json.dump(data, o, cls=SetEncoder)