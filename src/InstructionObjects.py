from typing import Any
import re

class Instruction:
	def __init__(self, raw_instruction:str) -> None:
		self.raw_instruction:str = raw_instruction
	def is_terminator(self) -> bool:
		assert not self.raw_instruction is None
		return re.match(r"\[\w+[^\(]]", self.raw_instruction) is not None


class Text(Instruction):
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

	def __str__(self) -> str:
		return f"<{self.__class__.__name__} name={self.name} / conjID={self.__conjected_id}>{' '+self.text if self.text else ''}" if not self.is_terminator() else f"<{self.__class__.__name__}>"

class HEADER(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, is_skippable: bool | None = None, fit_mode: str | None = None, text: str | None = None, is_autoable: bool | None = None, is_tutorial: bool | None = None, is_video_only: bool | None = None, actId: str | None = None, npcId: str | None = None, deny_auto_switch_scene: bool | None = None, char_sort_type: str | None = None, dont_clear_gameobjectpool_onstart: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.key: str | None = key
		self.is_skippable: bool | None = is_skippable
		self.fit_mode: str | None = fit_mode
		self.text: str | None = text
		self.is_autoable: bool | None = is_autoable
		self.is_tutorial: bool | None = is_tutorial
		self.is_video_only: bool | None = is_video_only
		self.actId: str | None = actId
		self.npcId: str | None = npcId
		self.deny_auto_switch_scene: bool | None = deny_auto_switch_scene
		self.char_sort_type: str | None = char_sort_type
		self.dont_clear_gameobjectpool_onstart: bool | None = dont_clear_gameobjectpool_onstart
		self.misc: dict[str, Any] = misc

class Dialog(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, time: float | int | None = None, block: bool | None = None, head: str | None = None, delay: float | int | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.time: float | int | None = time
		self.block: bool | None = block
		self.head: str | None = head
		self.delay: float | int | None = delay
		self.text: str | None = text
		self.misc: dict[str, Any] = misc

class PlayMusic(Instruction):
	def __init__(self, raw_instruction: str, intro: str | None = None, key: str | None = None, volume: float | int | None = None, crossfade: float | int | None = None, delay: float | int | None = None, text: str | None = None, fadetime: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.intro: str | None = intro
		self.key: str | None = key
		self.volume: float | int | None = volume
		self.crossfade: float | int | None = crossfade
		self.delay: float | int | None = delay
		self.text: str | None = text
		self.fadetime: float | int | None = fadetime
		self.misc: dict[str, Any] = misc

class Delay(Instruction):
	def __init__(self, raw_instruction: str, time: float | str | int | None = None, Delay: float | int | None = None, TIME: float | int | None = None, text: str | None = None, block: bool | None = None, times: float | None = None, tinme: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: float | str | int | None = time
		self.Delay: float | int | None = Delay
		self.TIME: float | int | None = TIME
		self.text: str | None = text
		self.block: bool | None = block
		self.times: float | None = times
		self.tinme: int | None = tinme
		self.misc: dict[str, Any] = misc

class name(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, text: str | None = None, delay: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.text: str | None = text
		self.delay: float | None = delay
		self.misc: dict[str, Any] = misc

class Blocker(Instruction):
	def __init__(self, raw_instruction: str, a: float | int | None = None, r: float | int | None = None, g: float | int | None = None, b: float | int | None = None, fadetime: float | int | None = None, block: bool | None = None, afrom: float | int | None = None, rfrom: float | int | None = None, gfrom: float | int | None = None, bfrom: float | int | None = None, text: str | None = None, isblock: bool | None = None, initr: int | None = None, ease: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.a: float | int | None = a
		self.r: float | int | None = r
		self.g: float | int | None = g
		self.b: float | int | None = b
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.afrom: float | int | None = afrom
		self.rfrom: float | int | None = rfrom
		self.gfrom: float | int | None = gfrom
		self.bfrom: float | int | None = bfrom
		self.text: str | None = text
		self.isblock: bool | None = isblock
		self.initr: int | None = initr
		self.ease: str | None = ease
		self.misc: dict[str, Any] = misc

class Character(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, name: str | None = None, name2: str | None = None, focus: float | int | None = None, fedetime: int | None = None, block: bool | None = None, blackstart: float | None = None, blackend: float | int | None = None, fadeitme: int | None = None, enter: str | None = None, enter2: str | None = None, blo: bool | None = None, blackstart2: float | None = None, blackend2: float | None = None, name1: str | None = None, time: float | None = None, blackstart1: float | None = None, blackend1: float | None = None, text: str | None = None, fadeout: int | None = None, delay: int | None = None, blockl: bool | None = None, blok: bool | None = None, isblock: bool | None = None, fadetiem: int | None = None, screenadapt: str | None = None, nameage: str | None = None, fatetime: float | None = None, duration: int | None = None, slot: str | None = None, fadetim: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.name: str | None = name
		self.name2: str | None = name2
		self.focus: float | int | None = focus
		self.fedetime: int | None = fedetime
		self.block: bool | None = block
		self.blackstart: float | None = blackstart
		self.blackend: float | int | None = blackend
		self.fadeitme: int | None = fadeitme
		self.enter: str | None = enter
		self.enter2: str | None = enter2
		self.blo: bool | None = blo
		self.blackstart2: float | None = blackstart2
		self.blackend2: float | None = blackend2
		self.name1: str | None = name1
		self.time: float | None = time
		self.blackstart1: float | None = blackstart1
		self.blackend1: float | None = blackend1
		self.text: str | None = text
		self.fadeout: int | None = fadeout
		self.delay: int | None = delay
		self.blockl: bool | None = blockl
		self.blok: bool | None = blok
		self.isblock: bool | None = isblock
		self.fadetiem: int | None = fadetiem
		self.screenadapt: str | None = screenadapt
		self.nameage: str | None = nameage
		self.fatetime: float | None = fatetime
		self.duration: int | None = duration
		self.slot: str | None = slot
		self.fadetim: float | None = fadetim
		self.misc: dict[str, Any] = misc

class Image(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, x: int | None = None, y: int | None = None, xScale: float | int | None = None, yScale: float | str | int | None = None, fadetime: float | int | None = None, screenadapt: str | None = None, block: bool | None = None, xTo: int | None = None, yTo: int | None = None, xScaleFrom: float | None = None, yScaleFrom: float | None = None, xScaleTo: float | int | None = None, yScaleTo: float | int | None = None, xpos: int | None = None, ypos: int | None = None, xscale: float | None = None, xFrom: int | None = None, yFrom: int | None = None, yScaleT: float | None = None, text: str | None = None, tiled: bool | None = None, ease: str | None = None, width: int | None = None, height: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.x: int | None = x
		self.y: int | None = y
		self.xScale: float | int | None = xScale
		self.yScale: float | str | int | None = yScale
		self.fadetime: float | int | None = fadetime
		self.screenadapt: str | None = screenadapt
		self.block: bool | None = block
		self.xTo: int | None = xTo
		self.yTo: int | None = yTo
		self.xScaleFrom: float | None = xScaleFrom
		self.yScaleFrom: float | None = yScaleFrom
		self.xScaleTo: float | int | None = xScaleTo
		self.yScaleTo: float | int | None = yScaleTo
		self.xpos: int | None = xpos
		self.ypos: int | None = ypos
		self.xscale: float | None = xscale
		self.xFrom: int | None = xFrom
		self.yFrom: int | None = yFrom
		self.yScaleT: float | None = yScaleT
		self.text: str | None = text
		self.tiled: bool | None = tiled
		self.ease: str | None = ease
		self.width: int | None = width
		self.height: int | None = height
		self.misc: dict[str, Any] = misc

class ImageTween(Instruction):
	def __init__(self, raw_instruction: str, xFrom: float | int | None = None, yFrom: float | int | None = None, xTo: int | None = None, yTo: int | None = None, xScaleFrom: float | str | int | None = None, yScaleFrom: float | int | None = None, xScaleTo: float | int | None = None, yScaleTo: float | int | None = None, duration: float | int | None = None, block: bool | None = None, xScale: float | int | None = None, yScale: float | int | None = None, ease: str | None = None, image: str | None = None, x: int | None = None, y: int | None = None, tiled: bool | None = None, fadetime: float | int | None = None, screenadapt: str | None = None, yTO: int | None = None, yto: int | None = None, yT: int | None = None, xTO: int | None = None, xfromScale: int | None = None, yfromScale: int | None = None, xto: int | None = None, xfrom: int | None = None, yfrom: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xFrom: float | int | None = xFrom
		self.yFrom: float | int | None = yFrom
		self.xTo: int | None = xTo
		self.yTo: int | None = yTo
		self.xScaleFrom: float | str | int | None = xScaleFrom
		self.yScaleFrom: float | int | None = yScaleFrom
		self.xScaleTo: float | int | None = xScaleTo
		self.yScaleTo: float | int | None = yScaleTo
		self.duration: float | int | None = duration
		self.block: bool | None = block
		self.xScale: float | int | None = xScale
		self.yScale: float | int | None = yScale
		self.ease: str | None = ease
		self.image: str | None = image
		self.x: int | None = x
		self.y: int | None = y
		self.tiled: bool | None = tiled
		self.fadetime: float | int | None = fadetime
		self.screenadapt: str | None = screenadapt
		self.yTO: int | None = yTO
		self.yto: int | None = yto
		self.yT: int | None = yT
		self.xTO: int | None = xTO
		self.xfromScale: int | None = xfromScale
		self.yfromScale: int | None = yfromScale
		self.xto: int | None = xto
		self.xfrom: int | None = xfrom
		self.yfrom: int | None = yfrom
		self.misc: dict[str, Any] = misc

class Background(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, fadetime: float | int | None = None, block: bool | None = None, screenadapt: str | None = None, x: int | None = None, y: int | None = None, xScale: float | int | None = None, yScale: float | int | None = None, text: str | None = None, xscale: float | int | None = None, yscale: float | None = None, xSclae: float | None = None, ysclae: int | None = None, width: float | int | None = None, height: float | int | None = None, ypos: int | None = None, time: int | None = None, tiled: bool | None = None, isblock: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.screenadapt: str | None = screenadapt
		self.x: int | None = x
		self.y: int | None = y
		self.xScale: float | int | None = xScale
		self.yScale: float | int | None = yScale
		self.text: str | None = text
		self.xscale: float | int | None = xscale
		self.yscale: float | None = yscale
		self.xSclae: float | None = xSclae
		self.ysclae: int | None = ysclae
		self.width: float | int | None = width
		self.height: float | int | None = height
		self.ypos: int | None = ypos
		self.time: int | None = time
		self.tiled: bool | None = tiled
		self.isblock: bool | None = isblock
		self.misc: dict[str, Any] = misc

class stopmusic(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, time: float | int | None = None, block: bool | None = None, faddetime: int | None = None, fdetime: int | None = None, crossfade: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.time: float | int | None = time
		self.block: bool | None = block
		self.faddetime: int | None = faddetime
		self.fdetime: int | None = fdetime
		self.crossfade: int | None = crossfade
		self.misc: dict[str, Any] = misc

class PlaySound(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, volume: float | int | None = None, block: bool | None = None, delay: float | int | None = None, loop: bool | str | None = None, channel: str | int | None = None, Delay: float | None = None, fadetime: float | int | None = None, crosstime: int | None = None, text: str | None = None, delai: float | None = None, crossfade: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.key: str | None = key
		self.volume: float | int | None = volume
		self.block: bool | None = block
		self.delay: float | int | None = delay
		self.loop: bool | str | None = loop
		self.channel: str | int | None = channel
		self.Delay: float | None = Delay
		self.fadetime: float | int | None = fadetime
		self.crosstime: int | None = crosstime
		self.text: str | None = text
		self.delai: float | None = delai
		self.crossfade: int | None = crossfade
		self.misc: dict[str, Any] = misc

class CameraShake(Instruction):
	def __init__(self, raw_instruction: str, duration: float | str | int | None = None, xstrength: float | int | None = None, ystrength: float | int | None = None, vibrato: int | None = None, randomness: int | None = None, block: bool | None = None, fadeout: bool | None = None, fadetime: float | int | None = None, stop: bool | None = None, delay: float | None = None, focus: str | None = None, isblock: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.duration: float | str | int | None = duration
		self.xstrength: float | int | None = xstrength
		self.ystrength: float | int | None = ystrength
		self.vibrato: int | None = vibrato
		self.randomness: int | None = randomness
		self.block: bool | None = block
		self.fadeout: bool | None = fadeout
		self.fadetime: float | int | None = fadetime
		self.stop: bool | None = stop
		self.delay: float | None = delay
		self.focus: str | None = focus
		self.isblock: bool | None = isblock
		self.misc: dict[str, Any] = misc

class showitem(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class hideitem(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc

class character(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, fadetime: float | int | None = None, focus: int | None = None, name2: str | None = None, blackstart: float | None = None, blackend: float | int | None = None, block: bool | None = None, enter: str | None = None, fadetim: float | None = None, enter2: str | None = None, blackstart2: float | None = None, blackend2: float | None = None, fadtime: int | None = None, time: float | None = None, offsetX: str | None = None, offsetY: str | None = None, exit2: str | None = None, faetime: int | None = None, foucs: int | None = None, fpcus: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.fadetime: float | int | None = fadetime
		self.focus: int | None = focus
		self.name2: str | None = name2
		self.blackstart: float | None = blackstart
		self.blackend: float | int | None = blackend
		self.block: bool | None = block
		self.enter: str | None = enter
		self.fadetim: float | None = fadetim
		self.enter2: str | None = enter2
		self.blackstart2: float | None = blackstart2
		self.blackend2: float | None = blackend2
		self.fadtime: int | None = fadtime
		self.time: float | None = time
		self.offsetX: str | None = offsetX
		self.offsetY: str | None = offsetY
		self.exit2: str | None = exit2
		self.faetime: int | None = faetime
		self.foucs: int | None = foucs
		self.fpcus: int | None = fpcus
		self.misc: dict[str, Any] = misc

class playsound(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, volume: float | int | None = None, channel: str | None = None, loop: bool | str | None = None, delay: float | int | None = None, block: bool | None = None, Delay: float | None = None, fadetime: int | None = None, text: str | None = None, voluyme: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.key: str | None = key
		self.volume: float | int | None = volume
		self.channel: str | None = channel
		self.loop: bool | str | None = loop
		self.delay: float | int | None = delay
		self.block: bool | None = block
		self.Delay: float | None = Delay
		self.fadetime: int | None = fadetime
		self.text: str | None = text
		self.voluyme: float | None = voluyme
		self.misc: dict[str, Any] = misc

class image(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, block: bool | None = None, image: str | None = None, screenadapt: str | None = None, xScale: float | int | None = None, yScale: float | int | None = None, x: int | None = None, y: int | None = None, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.image: str | None = image
		self.screenadapt: str | None = screenadapt
		self.xScale: float | int | None = xScale
		self.yScale: float | int | None = yScale
		self.x: int | None = x
		self.y: int | None = y
		self.time: int | None = time
		self.misc: dict[str, Any] = misc

class CameraEffect(Instruction):
	def __init__(self, raw_instruction: str, effect: str | None = None, amount: float | int | None = None, keep: bool | None = None, fadetime: float | int | None = None, block: bool | None = None, initamount: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.effect: str | None = effect
		self.amount: float | int | None = amount
		self.keep: bool | None = keep
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.initamount: float | int | None = initamount
		self.misc: dict[str, Any] = misc

class StopMusic(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, time: float | int | None = None, fadeetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.time: float | int | None = time
		self.fadeetime: int | None = fadeetime
		self.misc: dict[str, Any] = misc

class PopupDialog(Instruction):
	def __init__(self, raw_instruction: str, dialogHead: str | None = None, text: str | None = None, dialogX: str | int | None = None, dialogY: str | int | None = None, animStyle: str | None = None, protectTime: float | int | None = None, focusX: int | None = None, focusY: int | None = None, focusWidth: int | None = None, focusHeight: int | None = None, anchor: str | None = None, focusStyle: str | None = None, black: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.dialogHead: str | None = dialogHead
		self.text: str | None = text
		self.dialogX: str | int | None = dialogX
		self.dialogY: str | int | None = dialogY
		self.animStyle: str | None = animStyle
		self.protectTime: float | int | None = protectTime
		self.focusX: int | None = focusX
		self.focusY: int | None = focusY
		self.focusWidth: int | None = focusWidth
		self.focusHeight: int | None = focusHeight
		self.anchor: str | None = anchor
		self.focusStyle: str | None = focusStyle
		self.black: str | None = black
		self.misc: dict[str, Any] = misc

class playMusic(Instruction):
	def __init__(self, raw_instruction: str, intro: str | None = None, key: str | None = None, volume: float | int | None = None, crossfade: float | int | None = None, fadetime: float | int | None = None, delay: float | int | None = None, text: str | None = None, crosstime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.intro: str | None = intro
		self.key: str | None = key
		self.volume: float | int | None = volume
		self.crossfade: float | int | None = crossfade
		self.fadetime: float | int | None = fadetime
		self.delay: float | int | None = delay
		self.text: str | None = text
		self.crosstime: int | None = crosstime
		self.misc: dict[str, Any] = misc

class delay(Instruction):
	def __init__(self, raw_instruction: str, time: float | int | None = None, timw: float | None = None, delay: float | int | None = None, title_test: float | None = None, black: bool | None = None, fadetime: float | int | None = None, timr: str | None = None, block: bool | None = None, text: str | None = None, t: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: float | int | None = time
		self.timw: float | None = timw
		self.delay: float | int | None = delay
		self.title_test: float | None = title_test
		self.black: bool | None = black
		self.fadetime: float | int | None = fadetime
		self.timr: str | None = timr
		self.block: bool | None = block
		self.text: str | None = text
		self.t: float | None = t
		self.misc: dict[str, Any] = misc

class cameraEffect(Instruction):
	def __init__(self, raw_instruction: str, effect: str | None = None, keep: bool | None = None, amount: float | int | None = None, fadetime: float | int | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.effect: str | None = effect
		self.keep: bool | None = keep
		self.amount: float | int | None = amount
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc

class dialog(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | None = None, block: bool | None = None, head: str | None = None, delay: float | int | None = None, style: str | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | None = fadetime
		self.block: bool | None = block
		self.head: str | None = head
		self.delay: float | int | None = delay
		self.style: str | None = style
		self.text: str | None = text
		self.misc: dict[str, Any] = misc

class Decision(Instruction):
	def __init__(self, raw_instruction: str, options: str | None = None, values: str | None = None, option1: str | None = None, value1: str | None = None, option2: str | None = None, value2: str | None = None, option3: str | None = None, value3: str | None = None, option4: str | None = None, value4: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.options: str | None = options
		self.values: str | None = values
		self.option1: str | None = option1
		self.value1: str | None = value1
		self.option2: str | None = option2
		self.value2: str | None = value2
		self.option3: str | None = option3
		self.value3: str | None = value3
		self.option4: str | None = option4
		self.value4: str | None = value4
		self.misc: dict[str, Any] = misc

class Predicate(Instruction):
	def __init__(self, raw_instruction: str, references: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.references: str | None = references
		self.misc: dict[str, Any] = misc

class playmusic(Instruction):
	def __init__(self, raw_instruction: str, intro: str | None = None, key: str | None = None, volume: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.intro: str | None = intro
		self.key: str | None = key
		self.volume: float | None = volume
		self.misc: dict[str, Any] = misc

class Subtitle(Instruction):
	def __init__(self, raw_instruction: str, text: str | None = None, x: int | None = None, y: int | None = None, alignment: str | None = None, size: int | None = None, delay: float | int | None = None, width: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.text: str | None = text
		self.x: int | None = x
		self.y: int | None = y
		self.alignment: str | None = alignment
		self.size: int | None = size
		self.delay: float | int | None = delay
		self.width: int | None = width
		self.misc: dict[str, Any] = misc

class subtitle(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class characteraction(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, type: str | None = None, xpos: float | int | None = None, fadetime: float | int | None = None, block: bool | None = None, power: int | None = None, times: float | int | None = None, ypos: float | int | None = None, isblock: bool | None = None, delay: float | None = None, scale: float | int | None = None, direction: str | None = None, y: int | None = None, time: int | None = None, duration: float | int | None = None, loop: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.type: str | None = type
		self.xpos: float | int | None = xpos
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.power: int | None = power
		self.times: float | int | None = times
		self.ypos: float | int | None = ypos
		self.isblock: bool | None = isblock
		self.delay: float | None = delay
		self.scale: float | int | None = scale
		self.direction: str | None = direction
		self.y: int | None = y
		self.time: int | None = time
		self.duration: float | int | None = duration
		self.loop: bool | None = loop
		self.misc: dict[str, Any] = misc

class StopSound(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, fadetime: float | int | None = None, isblock: bool | None = None, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.fadetime: float | int | None = fadetime
		self.isblock: bool | None = isblock
		self.time: int | None = time
		self.misc: dict[str, Any] = misc

class musicvolume(Instruction):
	def __init__(self, raw_instruction: str, volume: float | int | None = None, fadetime: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: float | int | None = volume
		self.fadetime: float | int | None = fadetime
		self.misc: dict[str, Any] = misc

class multiline(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, text: str | None = None, delay: float | None = None, end: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.text: str | None = text
		self.delay: float | None = delay
		self.end: bool | None = end
		self.misc: dict[str, Any] = misc

class stopsound(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, fadetime: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.fadetime: float | int | None = fadetime
		self.misc: dict[str, Any] = misc

class CharacterCutin(Instruction):
	def __init__(self, raw_instruction: str, widgetID: str | None = None, name: str | None = None, style: str | None = None, fadetime: float | int | None = None, offsetx: int | None = None, width: int | None = None, block: bool | None = None, fadestyle: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.widgetID: str | None = widgetID
		self.name: str | None = name
		self.style: str | None = style
		self.fadetime: float | int | None = fadetime
		self.offsetx: int | None = offsetx
		self.width: int | None = width
		self.block: bool | None = block
		self.fadestyle: str | None = fadestyle
		self.misc: dict[str, Any] = misc

class stopSound(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, fadetime: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.fadetime: float | int | None = fadetime
		self.misc: dict[str, Any] = misc

class dealy(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc

class largebg(Instruction):
	def __init__(self, raw_instruction: str, imagegroup: str | None = None, solidwidth: str | None = None, solidheight: int | None = None, x: int | None = None, fadetime: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.imagegroup: str | None = imagegroup
		self.solidwidth: str | None = solidwidth
		self.solidheight: int | None = solidheight
		self.x: int | None = x
		self.fadetime: float | int | None = fadetime
		self.misc: dict[str, Any] = misc

class soundvolume(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, volume: float | int | None = None, fadetime: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.volume: float | int | None = volume
		self.fadetime: float | int | None = fadetime
		self.misc: dict[str, Any] = misc

class Characteraction(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, type: str | None = None, power: int | None = None, times: int | None = None, fadetime: float | int | None = None, block: bool | None = None, xpos: int | None = None, ypos: int | None = None, isblock: bool | None = None, pwoer: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.type: str | None = type
		self.power: int | None = power
		self.times: int | None = times
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.xpos: int | None = xpos
		self.ypos: int | None = ypos
		self.isblock: bool | None = isblock
		self.pwoer: int | None = pwoer
		self.misc: dict[str, Any] = misc

class MusicVolume(Instruction):
	def __init__(self, raw_instruction: str, volume: float | int | None = None, fadetime: float | int | None = None, channel: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: float | int | None = volume
		self.fadetime: float | int | None = fadetime
		self.channel: str | None = channel
		self.misc: dict[str, Any] = misc

class playSound(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, volume: float | int | None = None, delay: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.key: str | None = key
		self.volume: float | int | None = volume
		self.delay: float | int | None = delay
		self.misc: dict[str, Any] = misc

class Stopmusic(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.misc: dict[str, Any] = misc

class Sticker(Instruction):
	def __init__(self, raw_instruction: str, id: str | None = None, text: str | None = None, x: int | None = None, y: int | None = None, alignment: str | None = None, size: int | None = None, delay: float | int | None = None, width: int | None = None, duration: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.id: str | None = id
		self.text: str | None = text
		self.x: int | None = x
		self.y: int | None = y
		self.alignment: str | None = alignment
		self.size: int | None = size
		self.delay: float | int | None = delay
		self.width: int | None = width
		self.duration: float | int | None = duration
		self.misc: dict[str, Any] = misc

class stickerclear(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class ShowItem(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, fadetime: float | int | None = None, fadestyle: str | None = None, offsetx: int | None = None, width: int | None = None, style: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.fadetime: float | int | None = fadetime
		self.fadestyle: str | None = fadestyle
		self.offsetx: int | None = offsetx
		self.width: int | None = width
		self.style: str | None = style
		self.misc: dict[str, Any] = misc

class HideItem(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc

class largebgtween(Instruction):
	def __init__(self, raw_instruction: str, xFrom: int | None = None, xTo: int | None = None, duration: float | int | None = None, ease: str | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xFrom: int | None = xFrom
		self.xTo: int | None = xTo
		self.duration: float | int | None = duration
		self.ease: str | None = ease
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc

class BackgroundTween(Instruction):
	def __init__(self, raw_instruction: str, xFrom: int | None = None, xTo: int | None = None, duration: float | int | None = None, ease: str | None = None, block: bool | None = None, yFrom: int | None = None, yTo: int | None = None, elseRename: str | None = None, xScaleFrom: float | int | None = None, yScaleFrom: float | int | None = None, xScaleTo: float | int | None = None, yScaleTo: float | int | None = None, image: str | None = None, screenadapt: str | None = None, yScaleto: float | None = None, fadetime: float | None = None, xto: int | None = None, yto: int | None = None, x: int | None = None, y: int | None = None, xScale: float | None = None, yScale: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xFrom: int | None = xFrom
		self.xTo: int | None = xTo
		self.duration: float | int | None = duration
		self.ease: str | None = ease
		self.block: bool | None = block
		self.yFrom: int | None = yFrom
		self.yTo: int | None = yTo
		self.elseRename: str | None = elseRename
		self.xScaleFrom: float | int | None = xScaleFrom
		self.yScaleFrom: float | int | None = yScaleFrom
		self.xScaleTo: float | int | None = xScaleTo
		self.yScaleTo: float | int | None = yScaleTo
		self.image: str | None = image
		self.screenadapt: str | None = screenadapt
		self.yScaleto: float | None = yScaleto
		self.fadetime: float | None = fadetime
		self.xto: int | None = xto
		self.yto: int | None = yto
		self.x: int | None = x
		self.y: int | None = y
		self.xScale: float | None = xScale
		self.yScale: float | None = yScale
		self.misc: dict[str, Any] = misc

class Musicvolume(Instruction):
	def __init__(self, raw_instruction: str, volume: float | int | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: float | int | None = volume
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class Tutorial(Instruction):
	def __init__(self, raw_instruction: str, target: str | None = None, searchBtnInChildren: bool | str | None = None, waitForSignal: str | None = None, animStyle: str | None = None, focusStyle: str | None = None, black: float | str | None = None, protectTime: float | int | None = None, dialogHead: str | None = None, text: str | None = None, dialogX: str | int | None = None, dialogY: str | int | None = None, focusX: int | None = None, focusY: int | None = None, focusWidth: int | None = None, focusHeight: int | None = None, anchor: str | None = None, startX: int | None = None, startY: int | None = None, endX: int | None = None, endY: int | None = None, startAnchor: str | None = None, endAnchor: str | None = None, importantClick: bool | None = None, abortForSignal: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.target: str | None = target
		self.searchBtnInChildren: bool | str | None = searchBtnInChildren
		self.waitForSignal: str | None = waitForSignal
		self.animStyle: str | None = animStyle
		self.focusStyle: str | None = focusStyle
		self.black: float | str | None = black
		self.protectTime: float | int | None = protectTime
		self.dialogHead: str | None = dialogHead
		self.text: str | None = text
		self.dialogX: str | int | None = dialogX
		self.dialogY: str | int | None = dialogY
		self.focusX: int | None = focusX
		self.focusY: int | None = focusY
		self.focusWidth: int | None = focusWidth
		self.focusHeight: int | None = focusHeight
		self.anchor: str | None = anchor
		self.startX: int | None = startX
		self.startY: int | None = startY
		self.endX: int | None = endX
		self.endY: int | None = endY
		self.startAnchor: str | None = startAnchor
		self.endAnchor: str | None = endAnchor
		self.importantClick: bool | None = importantClick
		self.abortForSignal: str | None = abortForSignal
		self.misc: dict[str, Any] = misc

class stopmucis(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class backgroundTween(Instruction):
	def __init__(self, raw_instruction: str, xTo: int | None = None, duration: float | int | None = None, block: bool | None = None, xScaleFrom: float | int | None = None, yScaleFrom: float | int | None = None, xScaleTo: float | int | None = None, yScaleTo: float | int | None = None, xFrom: int | None = None, yFrom: int | None = None, yTo: int | None = None, xScale: float | None = None, yScale: float | None = None, fadetime: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xTo: int | None = xTo
		self.duration: float | int | None = duration
		self.block: bool | None = block
		self.xScaleFrom: float | int | None = xScaleFrom
		self.yScaleFrom: float | int | None = yScaleFrom
		self.xScaleTo: float | int | None = xScaleTo
		self.yScaleTo: float | int | None = yScaleTo
		self.xFrom: int | None = xFrom
		self.yFrom: int | None = yFrom
		self.yTo: int | None = yTo
		self.xScale: float | None = xScale
		self.yScale: float | None = yScale
		self.fadetime: float | None = fadetime
		self.misc: dict[str, Any] = misc

class Activity(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class charslot(Instruction):
	def __init__(self, raw_instruction: str, slot: str | None = None, name: str | None = None, posfrom: str | None = None, posto: str | None = None, afrom: float | str | int | None = None, ato: float | int | None = None, duration: float | int | None = None, isblock: bool | int | None = None, focus: str | None = None, action: str | None = None, random: bool | int | None = None, power: float | int | None = None, times: int | None = None, block: bool | None = None, bstart: float | int | None = None, bend: float | int | None = None, scale: float | int | None = None, poszoom: str | None = None, end: bool | None = None, delay: float | None = None, posTo: str | None = None, fadetime: float | int | None = None, blocker: bool | None = None, text: str | None = None, ocus: str | None = None, isblocke: bool | None = None, time: int | None = None, Duration: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.slot: str | None = slot
		self.name: str | None = name
		self.posfrom: str | None = posfrom
		self.posto: str | None = posto
		self.afrom: float | str | int | None = afrom
		self.ato: float | int | None = ato
		self.duration: float | int | None = duration
		self.isblock: bool | int | None = isblock
		self.focus: str | None = focus
		self.action: str | None = action
		self.random: bool | int | None = random
		self.power: float | int | None = power
		self.times: int | None = times
		self.block: bool | None = block
		self.bstart: float | int | None = bstart
		self.bend: float | int | None = bend
		self.scale: float | int | None = scale
		self.poszoom: str | None = poszoom
		self.end: bool | None = end
		self.delay: float | None = delay
		self.posTo: str | None = posTo
		self.fadetime: float | int | None = fadetime
		self.blocker: bool | None = blocker
		self.text: str | None = text
		self.ocus: str | None = ocus
		self.isblocke: bool | None = isblocke
		self.time: int | None = time
		self.Duration: int | None = Duration
		self.misc: dict[str, Any] = misc

class Effect(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, y: int | None = None, rox: int | None = None, roy: int | None = None, roz: float | int | None = None, delay: float | int | None = None, ypos: int | None = None, x: int | None = None, layer: int | None = None, yScale: int | None = None, z: int | None = None, xTo: int | None = None, movetime: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.y: int | None = y
		self.rox: int | None = rox
		self.roy: int | None = roy
		self.roz: float | int | None = roz
		self.delay: float | int | None = delay
		self.ypos: int | None = ypos
		self.x: int | None = x
		self.layer: int | None = layer
		self.yScale: int | None = yScale
		self.z: int | None = z
		self.xTo: int | None = xTo
		self.movetime: float | None = movetime
		self.misc: dict[str, Any] = misc

class SoundVolume(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, volume: float | int | None = None, fadetime: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.volume: float | int | None = volume
		self.fadetime: float | int | None = fadetime
		self.misc: dict[str, Any] = misc

class bgeffect(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, layer: int | None = None, x: int | None = None, delay: int | None = None, xto: int | None = None, yto: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.layer: int | None = layer
		self.x: int | None = x
		self.delay: int | None = delay
		self.xto: int | None = xto
		self.yto: int | None = yto
		self.misc: dict[str, Any] = misc

class curtain(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | int | None = None, grad: bool | None = None, block: bool | None = None, a: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | int | None = fadetime
		self.grad: bool | None = grad
		self.block: bool | None = block
		self.a: int | None = a
		self.misc: dict[str, Any] = misc

class theater(Instruction):
	def __init__(self, raw_instruction: str, mode: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.mode: bool | None = mode
		self.misc: dict[str, Any] = misc

class background(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, xScale: float | int | None = None, yScale: float | int | None = None, fadetime: float | int | None = None, screenadapt: str | None = None, y: int | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.xScale: float | int | None = xScale
		self.yScale: float | int | None = yScale
		self.fadetime: float | int | None = fadetime
		self.screenadapt: str | None = screenadapt
		self.y: int | None = y
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc

class Stopsound(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class imageTween(Instruction):
	def __init__(self, raw_instruction: str, xFrom: int | None = None, xTo: int | None = None, duration: int | None = None, yFrom: int | None = None, block: bool | None = None, yTo: int | None = None, ease: str | None = None, xScaleFrom: float | None = None, yScaleFrom: float | None = None, xScaleTo: float | int | None = None, yScaleTo: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xFrom: int | None = xFrom
		self.xTo: int | None = xTo
		self.duration: int | None = duration
		self.yFrom: int | None = yFrom
		self.block: bool | None = block
		self.yTo: int | None = yTo
		self.ease: str | None = ease
		self.xScaleFrom: float | None = xScaleFrom
		self.yScaleFrom: float | None = yScaleFrom
		self.xScaleTo: float | int | None = xScaleTo
		self.yScaleTo: float | int | None = yScaleTo
		self.misc: dict[str, Any] = misc

class delau(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc

class Video(Instruction):
	def __init__(self, raw_instruction: str, res: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.res: str | None = res
		self.misc: dict[str, Any] = misc

class musicvolune(Instruction):
	def __init__(self, raw_instruction: str, volume: float | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: float | None = volume
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class ConsumeGuideOnStoryEnd(Instruction):
	def __init__(self, raw_instruction: str, target: str | None = None, subsignal: str | None = None, showAnyway: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.target: str | None = target
		self.subsignal: str | None = subsignal
		self.showAnyway: bool | None = showAnyway
		self.misc: dict[str, Any] = misc

class hideItem(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | None = fadetime
		self.misc: dict[str, Any] = misc

class dialo(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class delat(Instruction):
	def __init__(self, raw_instruction: str, time: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: float | None = time
		self.misc: dict[str, Any] = misc

class delayt(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc

class chaa(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class palysound(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, volume: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.volume: float | int | None = volume
		self.misc: dict[str, Any] = misc

class Interlock(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class End(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class predicate(Instruction):
	def __init__(self, raw_instruction: str, references: str | None = None, selectableCondition: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.references: str | None = references
		self.selectableCondition: str | None = selectableCondition
		self.misc: dict[str, Any] = misc

class SetConditionProgress(Instruction):
	def __init__(self, raw_instruction: str, conditionKey: str | None = None, itemCount: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.conditionKey: str | None = conditionKey
		self.itemCount: str | None = itemCount
		self.misc: dict[str, Any] = misc

class withdraw(Instruction):
	def __init__(self, raw_instruction: str, charId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.charId: str | None = charId
		self.misc: dict[str, Any] = misc

class AddItem(Instruction):
	def __init__(self, raw_instruction: str, itemId: str | None = None, itemCount: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.itemId: str | None = itemId
		self.itemCount: str | None = itemCount
		self.misc: dict[str, Any] = misc

class Condition(Instruction):
	def __init__(self, raw_instruction: str, references: str | None = None, key: str | None = None, itemId: str | None = None, value: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.references: str | None = references
		self.key: str | None = key
		self.itemId: str | None = itemId
		self.value: str | None = value
		self.misc: dict[str, Any] = misc

class Sandbox(Instruction):
	def __init__(self, raw_instruction: str, focusType: str | None = None, module: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.focusType: str | None = focusType
		self.module: str | None = module
		self.misc: dict[str, Any] = misc

class Battle(Instruction):
	def __init__(self, raw_instruction: str, pause: bool | None = None, mask: str | None = None, cost: int | None = None, charId: str | None = None, sp: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.pause: bool | None = pause
		self.mask: str | None = mask
		self.cost: int | None = cost
		self.charId: str | None = charId
		self.sp: int | None = sp
		self.misc: dict[str, Any] = misc

class InputBlocker(Instruction):
	def __init__(self, raw_instruction: str, blockInput: bool | None = None, validX: int | None = None, validY: int | None = None, validWidth: int | None = None, validHeight: int | None = None, black: float | int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.blockInput: bool | None = blockInput
		self.validX: int | None = validX
		self.validY: int | None = validY
		self.validWidth: int | None = validWidth
		self.validHeight: int | None = validHeight
		self.black: float | int | None = black
		self.misc: dict[str, Any] = misc

class imagerotate(Instruction):
	def __init__(self, raw_instruction: str, angle: int | None = None, fadetime: float | int | None = None, isblock: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.angle: int | None = angle
		self.fadetime: float | int | None = fadetime
		self.isblock: bool | None = isblock
		self.misc: dict[str, Any] = misc

class bgEffect(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class Backgroundtween(Instruction):
	def __init__(self, raw_instruction: str, xScaleTo: float | int | None = None, yScaleTo: float | int | None = None, xTo: int | None = None, yTo: int | None = None, duration: float | int | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xScaleTo: float | int | None = xScaleTo
		self.yScaleTo: float | int | None = yScaleTo
		self.xTo: int | None = xTo
		self.yTo: int | None = yTo
		self.duration: float | int | None = duration
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc

class narration(Instruction):
	def __init__(self, raw_instruction: str, delay: float | int | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.delay: float | int | None = delay
		self.text: str | None = text
		self.misc: dict[str, Any] = misc

class OptionBranch(Instruction):
	def __init__(self, raw_instruction: str, option0: str | None = None, option1: str | None = None, option2: str | None = None, delay: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.option0: str | None = option0
		self.option1: str | None = option1
		self.option2: str | None = option2
		self.delay: int | None = delay
		self.misc: dict[str, Any] = misc

class VoiceWithin(Instruction):
	def __init__(self, raw_instruction: str, head: str | None = None, delay: int | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.head: str | None = head
		self.delay: int | None = delay
		self.text: str | None = text
		self.misc: dict[str, Any] = misc

class Obtain(Instruction):
	def __init__(self, raw_instruction: str, id: str | None = None, delay: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.id: str | None = id
		self.delay: float | None = delay
		self.misc: dict[str, Any] = misc

class Charslot(Instruction):
	def __init__(self, raw_instruction: str, duration: float | int | None = None, slot: str | None = None, posfrom: str | None = None, posto: str | None = None, name: str | None = None, afrom: int | None = None, ato: int | None = None, isblock: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.duration: float | int | None = duration
		self.slot: str | None = slot
		self.posfrom: str | None = posfrom
		self.posto: str | None = posto
		self.name: str | None = name
		self.afrom: int | None = afrom
		self.ato: int | None = ato
		self.isblock: bool | None = isblock
		self.misc: dict[str, Any] = misc

class gridbg(Instruction):
	def __init__(self, raw_instruction: str, imagegroup: str | None = None, solidwidth: str | None = None, solidheight: str | None = None, x: int | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.imagegroup: str | None = imagegroup
		self.solidwidth: str | None = solidwidth
		self.solidheight: str | None = solidheight
		self.x: int | None = x
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class soundVolume(Instruction):
	def __init__(self, raw_instruction: str, volume: float | None = None, channel: str | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: float | None = volume
		self.channel: str | None = channel
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc

class backgroundtween(Instruction):
	def __init__(self, raw_instruction: str, yFrom: int | None = None, yTo: int | None = None, duration: float | int | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.yFrom: int | None = yFrom
		self.yTo: int | None = yTo
		self.duration: float | int | None = duration
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc

class charslsot(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class verticalbg(Instruction):
	def __init__(self, raw_instruction: str, imagegroup: str | None = None, solidwidth: int | None = None, solidheight: str | None = None, x: int | None = None, y: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.imagegroup: str | None = imagegroup
		self.solidwidth: int | None = solidwidth
		self.solidheight: str | None = solidheight
		self.x: int | None = x
		self.y: int | None = y
		self.misc: dict[str, Any] = misc

class timersticker(Instruction):
	def __init__(self, raw_instruction: str, x: int | None = None, y: int | None = None, width: int | None = None, size: int | None = None, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.x: int | None = x
		self.y: int | None = y
		self.width: int | None = width
		self.size: int | None = size
		self.time: int | None = time
		self.misc: dict[str, Any] = misc

class timerclear(Instruction):
	def __init__(self, raw_instruction: str, afrom: int | None = None, ato: int | None = None, duration: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.afrom: int | None = afrom
		self.ato: int | None = ato
		self.duration: int | None = duration
		self.misc: dict[str, Any] = misc

class warp(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.misc: dict[str, Any] = misc

class cgitem(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, style: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.style: str | None = style
		self.misc: dict[str, Any] = misc

class hidecgitem(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class Act38D1(Instruction):
	def __init__(self, raw_instruction: str, slotId: str | None = None, slotType: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.slotId: str | None = slotId
		self.slotType: str | None = slotType
		self.misc: dict[str, Any] = misc

class Showitem(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, fadetime: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.fadetime: float | None = fadetime
		self.misc: dict[str, Any] = misc

class SkipToThis(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class StartBattle(Instruction):
	def __init__(self, raw_instruction: str, stageId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.stageId: str | None = stageId
		self.misc: dict[str, Any] = misc

class GotoPage(Instruction):
	def __init__(self, raw_instruction: str, dest: str | None = None, waitForSignal: str | None = None, initMissionPage: str | None = None, zoneId: str | None = None, stageId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.dest: str | None = dest
		self.waitForSignal: str | None = waitForSignal
		self.initMissionPage: str | None = initMissionPage
		self.zoneId: str | None = zoneId
		self.stageId: str | None = stageId
		self.misc: dict[str, Any] = misc

class GotoCharInfo(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc

class Building(Instruction):
	def __init__(self, raw_instruction: str, mode: str | None = None, roomId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.mode: str | None = mode
		self.roomId: str | None = roomId
		self.misc: dict[str, Any] = misc

class Campaign(Instruction):
	def __init__(self, raw_instruction: str, zoneId: str | None = None, waitForSignal: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.zoneId: str | None = zoneId
		self.waitForSignal: str | None = waitForSignal
		self.misc: dict[str, Any] = misc

class Shop(Instruction):
	def __init__(self, raw_instruction: str, shopType: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.shopType: str | None = shopType
		self.misc: dict[str, Any] = misc

class CharSelect(Instruction):
	def __init__(self, raw_instruction: str, sortType: str | None = None, professionFilter: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.sortType: str | None = sortType
		self.professionFilter: str | None = professionFilter
		self.misc: dict[str, Any] = misc

class blocker(Instruction):
	def __init__(self, raw_instruction: str, a: float | int | None = None, block: bool | None = None, fadetime: float | int | None = None, r: int | None = None, g: int | None = None, b: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.a: float | int | None = a
		self.block: bool | None = block
		self.fadetime: float | int | None = fadetime
		self.r: int | None = r
		self.g: int | None = g
		self.b: int | None = b
		self.misc: dict[str, Any] = misc

class daley(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc

class skipnode(Instruction):
	def __init__(self, raw_instruction: str, mode: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.mode: str | None = mode
		self.misc: dict[str, Any] = misc

class effect(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, layer: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.layer: int | None = layer
		self.misc: dict[str, Any] = misc

class fadetime(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | None = fadetime
		self.misc: dict[str, Any] = misc

class header(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, is_skippable: bool | None = None, fit_mode: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.key: str | None = key
		self.is_skippable: bool | None = is_skippable
		self.fit_mode: str | None = fit_mode
		self.misc: dict[str, Any] = misc

class camerashake(Instruction):
	def __init__(self, raw_instruction: str, duration: float | None = None, xstrength: int | None = None, ystrength: int | None = None, vibrato: int | None = None, randomness: int | None = None, fadeout: bool | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.duration: float | None = duration
		self.xstrength: int | None = xstrength
		self.ystrength: int | None = ystrength
		self.vibrato: int | None = vibrato
		self.randomness: int | None = randomness
		self.fadeout: bool | None = fadeout
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc

class delay9ti(Instruction):
	def __init__(self, raw_instruction: str, delay9ti: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.delay9ti: int | None = delay9ti
		self.misc: dict[str, Any] = misc

class dalay(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc

class Title(Instruction):
	def __init__(self, raw_instruction: str, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.text: str | None = text
		self.misc: dict[str, Any] = misc

class Div(Instruction):
	def __init__(self, raw_instruction: str, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.text: str | None = text
		self.misc: dict[str, Any] = misc

class focusout(Instruction):
	def __init__(self, raw_instruction: str, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.text: str | None = text
		self.misc: dict[str, Any] = misc