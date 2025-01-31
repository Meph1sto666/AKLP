from io import TextIOWrapper
import json

dump = json.load(open("./utils/instruction_dump.json"))
out: TextIOWrapper = open("./utils/instructions.py", 'w')

parent = """
class Instruction:
	def __init__(self, raw_instruction:str) -> None:
		self.raw_instruction:str = raw_instruction
	def is_terminator(self) -> bool:
		assert not self.raw_instruction is None
		return re.match(r"\\[\\w+[^\\(]]", self.raw_instruction) is not None\n
"""

text_class = """
class RawText(Instruction):
	def __init__(self, line:str, text:str|None=None, name:str="narrator", **misc:dict[str, Any]) -> None:
		super().__init__(line)
		self.text:str|None = text
		self.name:str = name
		self.misc:dict[str, Any] = misc
		self.__conjected_id:set[str] = set(["narrator"])
	# def setConjectedId(self, new_id:set[str]) -> None:
	# 	self.__conjected_id = new_id
	# def getConjectedId(self) -> set[str]:
	# 	return self.__conjected_id
	# def getChar(self) -> set[str]:
	# 	# assert self.name is not None
	# 	return set([self.name])
	def get_name(self):
		return self.name
"""


imports: str = "\n".join(["from typing import Any", "import re"]) + "\n"
out.write(imports)
out.write(parent)
out.write(text_class)

for d in dump:
	if d == "RawText": continue
	class_head: str = f"class {d}(Instruction):\n"
	args: list[str] = ["raw_instruction: str"] + [f'{arg}: ' + ' | '.join(dump[d][arg] + ["None"]) + ' = None' for arg in dump[d] if arg != 'count']
	init_head: str = f"\tdef __init__(self{', ' if len(args)>0 else ''}{', '.join(args)}, **misc: dict[str, Any]) -> None:\n"
	init_body: str = "\t\tsuper().__init__(raw_instruction)\n"
	init_body += "\n".join(f"\t\tself.{arg}: " + ' | '.join(dump[d][arg] + ["None"]) + f' = {arg}' for arg in dump[d] if arg != 'count') + "\n"
	init_body += f"\t\tself.misc: dict[str, Any] = misc\n"
	# print(class_head + init_head + init_body)
	# init_body += "\t\tpass\n" if len(init_body) < 1 else "\n"
	out.write(class_head + init_head + init_body)

# for d in dump:	
# 	class_head: str = f"class {d}(Instruction):\n"
# 	args: list[str] = ["raw_instruction: str"] + [f'{arg}: ' + ' | '.join(dump[d][arg]['data_types'] + ["None"]) + ' = None' for arg in dump[d] if arg != 'count']
# 	init_head: str = f"\tdef __init__(self{', ' if len(args)>0 else ''}{', '.join(args)}, **misc: dict[str, Any]) -> None:\n"
# 	init_body: str = "\t\tsuper().__init__(raw_instruction)\n"
# 	init_body += "\n".join(f'\t\tself.{arg}: ' + ' | '.join(dump[d][arg]['data_types'] + ["None"]) + f' = {arg}' for arg in dump[d] if arg != 'count') + "\n"
# 	init_body += f"\t\tself.misc: dict[str, Any] = misc\n"
# 	# print(class_head + init_head + init_body)
# 	# init_body += "\t\tpass\n" if len(init_body) < 1 else "\n"
# 	out.write(class_head + init_head + init_body + "\n")