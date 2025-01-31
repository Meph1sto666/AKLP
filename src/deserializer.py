import re
import typing
from json import loads
from .instructions import *
from . import instructions as instructions

class Deserializer():
	def __init__(self, file_path: str):
		"""
		"""
		self.file_path:str = file_path
		self.instructions: typing.List[Instruction] = []
		self.__is_deserialized: bool = False
	
	def deserialize(self) -> list[Instruction]:
		"""
		"""
		print(self.file_path)
		with open(self.file_path, "r", encoding="utf-8") as file:
			for line in file:
				lp = LineParser(line)
				self.instructions.append(lp.parse())
		self.__is_deserialized = True
		return self.instructions
	
	def is_deserialized(self) -> bool:
		return self.__is_deserialized

class LineParser():
	def __init__(self, raw: str) -> None:
		self.__raw:str = raw		
		self.line:str = raw.strip()
		self.instruction_type:str|None = None
		self.args:dict[str, typing.Any]|None = None
		# print(self.instruction_type, self.args)

	def parse(self) -> Instruction:
		found_meta:re.Match[str]|None = re.search(r"(?<=\[).*(?=\])", self.__raw)
		meta: str = found_meta.group() if found_meta else ""
		text: str = self.line.replace(meta, "", 1).strip(' []\n')
		args_list: typing.Iterator[re.Match[str]] = re.finditer(r"\w+(\s*)?=(\s*)?((\".+?\")|[^(,(\s*)?|(\s*)?,)\)\n\]]+)", meta)
		try:
			args:dict[str,float|int|str|None] = dict([[self.convert(c) for c in re.split(r"\s*=\s*", a.group(), 1)] for a in args_list]) # type: ignore
			e:float|int|str|None = args.pop('else', None)
			if not e is None:
				args["elseRename"] = e
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
		_class: typing.Any|None = getattr(instructions, self.instruction_type, None)
		if _class is None:
			print(self.__raw)
			raise RuntimeError
		else:
			return _class(self.__raw, **self.args)


	def convert(self, val:str) -> float | int | str | bool | None:
		try:
			return loads(val)
		except:
			return val