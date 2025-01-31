from typing import Any
import re

class Instruction:
	def __init__(self, raw_instruction:str) -> None:
		self.raw_instruction:str = raw_instruction
	def is_terminator(self) -> bool:
		assert not self.raw_instruction is None
		return re.match(r"\[\w+[^\(]]", self.raw_instruction) is not None


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
class HEADER(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, is_skippable: bool | None = None, fit_mode: str | None = None, text: str | None = None, is_autoable: bool | None = None, is_tutorial: bool | None = None, is_video_only: bool | None = None, actId: str | None = None, npcId: str | None = None, char_sort_type: int | str | None = None, deny_auto_switch_scene: bool | None = None, dont_clear_gameobjectpool_onstart: bool | None = None, **misc: dict[str, Any]) -> None:
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
		self.char_sort_type: int | str | None = char_sort_type
		self.deny_auto_switch_scene: bool | None = deny_auto_switch_scene
		self.dont_clear_gameobjectpool_onstart: bool | None = dont_clear_gameobjectpool_onstart
		self.misc: dict[str, Any] = misc
class stopmusic(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | float | None = None, time: int | float | None = None, block: bool | None = None, faddetime: int | None = None, fdetime: int | None = None, crossfade: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | float | None = fadetime
		self.time: int | float | None = time
		self.block: bool | None = block
		self.faddetime: int | None = faddetime
		self.fdetime: int | None = fdetime
		self.crossfade: int | None = crossfade
		self.misc: dict[str, Any] = misc
class Dialog(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | float | None = None, block: bool | None = None, delay: int | float | None = None, style: str | None = None, text: str | None = None, time: int | float | None = None, head: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.delay: int | float | None = delay
		self.style: str | None = style
		self.text: str | None = text
		self.time: int | float | None = time
		self.head: str | None = head
		self.misc: dict[str, Any] = misc
class Delay(Instruction):
	def __init__(self, raw_instruction: str, time: int | str | float | None = None, Delay: int | float | None = None, TIME: int | float | None = None, times: float | None = None, block: bool | None = None, tinme: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | str | float | None = time
		self.Delay: int | float | None = Delay
		self.TIME: int | float | None = TIME
		self.times: float | None = times
		self.block: bool | None = block
		self.tinme: int | None = tinme
		self.misc: dict[str, Any] = misc
class Blocker(Instruction):
	def __init__(self, raw_instruction: str, a: int | float | None = None, r: int | float | None = None, g: int | float | None = None, b: int | float | None = None, fadetime: int | float | None = None, block: bool | None = None, afrom: int | float | None = None, rfrom: int | float | None = None, gfrom: int | float | None = None, bfrom: int | float | None = None, style: str | None = None, inverse: bool | None = None, initr: int | None = None, isblock: bool | None = None, text: str | None = None, ease: str | None = None, image: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.a: int | float | None = a
		self.r: int | float | None = r
		self.g: int | float | None = g
		self.b: int | float | None = b
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.afrom: int | float | None = afrom
		self.rfrom: int | float | None = rfrom
		self.gfrom: int | float | None = gfrom
		self.bfrom: int | float | None = bfrom
		self.style: str | None = style
		self.inverse: bool | None = inverse
		self.initr: int | None = initr
		self.isblock: bool | None = isblock
		self.text: str | None = text
		self.ease: str | None = ease
		self.image: str | None = image
		self.misc: dict[str, Any] = misc
class Background(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, screenadapt: str | None = None, fadetime: int | float | None = None, duration: int | float | None = None, block: bool | None = None, xScale: int | float | None = None, yScale: int | float | None = None, x: int | None = None, y: int | None = None, width: int | float | None = None, height: int | float | None = None, ypos: int | None = None, xscale: int | float | None = None, yscale: float | None = None, text: str | None = None, ysclae: int | None = None, xSclae: float | None = None, tiled: bool | None = None, isblock: bool | None = None, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.screenadapt: str | None = screenadapt
		self.fadetime: int | float | None = fadetime
		self.duration: int | float | None = duration
		self.block: bool | None = block
		self.xScale: int | float | None = xScale
		self.yScale: int | float | None = yScale
		self.x: int | None = x
		self.y: int | None = y
		self.width: int | float | None = width
		self.height: int | float | None = height
		self.ypos: int | None = ypos
		self.xscale: int | float | None = xscale
		self.yscale: float | None = yscale
		self.text: str | None = text
		self.ysclae: int | None = ysclae
		self.xSclae: float | None = xSclae
		self.tiled: bool | None = tiled
		self.isblock: bool | None = isblock
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class playMusic(Instruction):
	def __init__(self, raw_instruction: str, intro: str | None = None, key: str | None = None, volume: int | float | None = None, fadetime: int | float | None = None, delay: int | float | None = None, crossfade: int | float | None = None, crosstime: int | None = None, text: str | None = None, daley: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.intro: str | None = intro
		self.key: str | None = key
		self.volume: int | float | None = volume
		self.fadetime: int | float | None = fadetime
		self.delay: int | float | None = delay
		self.crossfade: int | float | None = crossfade
		self.crosstime: int | None = crosstime
		self.text: str | None = text
		self.daley: float | None = daley
		self.misc: dict[str, Any] = misc
class Character(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, fadetime: int | float | None = None, block: bool | None = None, name2: str | None = None, focus: int | float | None = None, blackstart: float | None = None, blackend: int | float | None = None, fadeitme: int | None = None, nameage: str | None = None, blok: bool | None = None, text: str | None = None, blackstart2: float | None = None, blackend2: float | None = None, enter2: str | None = None, enter: str | None = None, blackstart1: float | None = None, blackend1: float | None = None, fadeout: int | None = None, time: float | None = None, blockl: bool | None = None, fedetime: int | None = None, fadetiem: int | None = None, delay: int | None = None, name1: str | None = None, blo: bool | None = None, screenadapt: str | None = None, isblock: bool | None = None, slot: str | None = None, fatetime: float | None = None, fadetim: float | None = None, duration: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.name2: str | None = name2
		self.focus: int | float | None = focus
		self.blackstart: float | None = blackstart
		self.blackend: int | float | None = blackend
		self.fadeitme: int | None = fadeitme
		self.nameage: str | None = nameage
		self.blok: bool | None = blok
		self.text: str | None = text
		self.blackstart2: float | None = blackstart2
		self.blackend2: float | None = blackend2
		self.enter2: str | None = enter2
		self.enter: str | None = enter
		self.blackstart1: float | None = blackstart1
		self.blackend1: float | None = blackend1
		self.fadeout: int | None = fadeout
		self.time: float | None = time
		self.blockl: bool | None = blockl
		self.fedetime: int | None = fedetime
		self.fadetiem: int | None = fadetiem
		self.delay: int | None = delay
		self.name1: str | None = name1
		self.blo: bool | None = blo
		self.screenadapt: str | None = screenadapt
		self.isblock: bool | None = isblock
		self.slot: str | None = slot
		self.fatetime: float | None = fatetime
		self.fadetim: float | None = fadetim
		self.duration: int | None = duration
		self.misc: dict[str, Any] = misc
class SpokenText(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, text: str | None = None, avatarId: str | None = None, isAvatarRight: str | None = None, delay: float | None = None, offsetX: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.text: str | None = text
		self.avatarId: str | None = avatarId
		self.isAvatarRight: str | None = isAvatarRight
		self.delay: float | None = delay
		self.offsetX: str | None = offsetX
		self.misc: dict[str, Any] = misc
class character(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, fadetime: int | float | None = None, fadtime: int | None = None, name2: str | None = None, block: bool | None = None, focus: int | None = None, blackstart: float | None = None, blackend: int | float | None = None, blackstart2: float | None = None, blackend2: float | None = None, enter: str | None = None, fadetim: float | None = None, offsetX: str | None = None, offsetY: str | None = None, enter2: str | None = None, time: float | None = None, fpcus: int | None = None, faetime: int | None = None, foucs: int | None = None, exit2: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.fadetime: int | float | None = fadetime
		self.fadtime: int | None = fadtime
		self.name2: str | None = name2
		self.block: bool | None = block
		self.focus: int | None = focus
		self.blackstart: float | None = blackstart
		self.blackend: int | float | None = blackend
		self.blackstart2: float | None = blackstart2
		self.blackend2: float | None = blackend2
		self.enter: str | None = enter
		self.fadetim: float | None = fadetim
		self.offsetX: str | None = offsetX
		self.offsetY: str | None = offsetY
		self.enter2: str | None = enter2
		self.time: float | None = time
		self.fpcus: int | None = fpcus
		self.faetime: int | None = faetime
		self.foucs: int | None = foucs
		self.exit2: str | None = exit2
		self.misc: dict[str, Any] = misc
class PlaySound(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, volume: int | float | None = None, delay: int | float | None = None, Delay: float | None = None, loop: str | bool | None = None, channel: int | str | None = None, block: bool | None = None, fadetime: int | float | None = None, crosstime: int | None = None, crossfade: int | None = None, delai: float | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.key: str | None = key
		self.volume: int | float | None = volume
		self.delay: int | float | None = delay
		self.Delay: float | None = Delay
		self.loop: str | bool | None = loop
		self.channel: int | str | None = channel
		self.block: bool | None = block
		self.fadetime: int | float | None = fadetime
		self.crosstime: int | None = crosstime
		self.crossfade: int | None = crossfade
		self.delai: float | None = delai
		self.text: str | None = text
		self.misc: dict[str, Any] = misc
class dialog(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | None = None, block: bool | None = None, head: str | None = None, delay: int | float | None = None, style: str | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | None = fadetime
		self.block: bool | None = block
		self.head: str | None = head
		self.delay: int | float | None = delay
		self.style: str | None = style
		self.text: str | None = text
		self.misc: dict[str, Any] = misc
class CameraShake(Instruction):
	def __init__(self, raw_instruction: str, duration: int | str | float | None = None, xstrength: int | float | None = None, ystrength: int | float | None = None, vibrato: int | None = None, randomness: int | None = None, fadeout: bool | None = None, block: bool | None = None, stop: bool | None = None, delay: float | None = None, fadetime: int | float | None = None, focus: str | None = None, strength: int | None = None, isblock: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.duration: int | str | float | None = duration
		self.xstrength: int | float | None = xstrength
		self.ystrength: int | float | None = ystrength
		self.vibrato: int | None = vibrato
		self.randomness: int | None = randomness
		self.fadeout: bool | None = fadeout
		self.block: bool | None = block
		self.stop: bool | None = stop
		self.delay: float | None = delay
		self.fadetime: int | float | None = fadetime
		self.focus: str | None = focus
		self.strength: int | None = strength
		self.isblock: bool | None = isblock
		self.misc: dict[str, Any] = misc
class delay(Instruction):
	def __init__(self, raw_instruction: str, time: int | str | float | None = None, black: bool | None = None, timw: float | None = None, timr: str | None = None, title_test: float | None = None, fadetime: int | float | None = None, delay: int | float | None = None, yime: float | None = None, block: bool | None = None, text: str | None = None, t: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | str | float | None = time
		self.black: bool | None = black
		self.timw: float | None = timw
		self.timr: str | None = timr
		self.title_test: float | None = title_test
		self.fadetime: int | float | None = fadetime
		self.delay: int | float | None = delay
		self.yime: float | None = yime
		self.block: bool | None = block
		self.text: str | None = text
		self.t: float | None = t
		self.misc: dict[str, Any] = misc
class characteraction(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, type: str | None = None, xpos: int | float | None = None, ypos: int | float | None = None, fadetime: int | float | None = None, block: bool | None = None, power: int | None = None, times: int | float | None = None, delay: float | None = None, scale: int | float | None = None, isblock: bool | None = None, direction: str | None = None, y: int | None = None, time: int | None = None, duration: int | float | None = None, loop: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.type: str | None = type
		self.xpos: int | float | None = xpos
		self.ypos: int | float | None = ypos
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.power: int | None = power
		self.times: int | float | None = times
		self.delay: float | None = delay
		self.scale: int | float | None = scale
		self.isblock: bool | None = isblock
		self.direction: str | None = direction
		self.y: int | None = y
		self.time: int | None = time
		self.duration: int | float | None = duration
		self.loop: bool | None = loop
		self.misc: dict[str, Any] = misc
class Image(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, x: int | None = None, y: int | None = None, xScale: int | float | None = None, yScale: int | str | float | None = None, screenadapt: str | None = None, fadetime: int | float | None = None, block: bool | None = None, xpos: int | None = None, ypos: int | None = None, xFrom: int | None = None, yFrom: int | None = None, xTo: int | None = None, yTo: int | None = None, yScaleFrom: float | None = None, xScaleFrom: float | None = None, xScaleTo: int | float | None = None, yScaleTo: int | float | None = None, text: str | None = None, xscale: float | None = None, yScaleT: float | None = None, tiled: bool | None = None, ease: str | None = None, width: int | None = None, height: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.x: int | None = x
		self.y: int | None = y
		self.xScale: int | float | None = xScale
		self.yScale: int | str | float | None = yScale
		self.screenadapt: str | None = screenadapt
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.xpos: int | None = xpos
		self.ypos: int | None = ypos
		self.xFrom: int | None = xFrom
		self.yFrom: int | None = yFrom
		self.xTo: int | None = xTo
		self.yTo: int | None = yTo
		self.yScaleFrom: float | None = yScaleFrom
		self.xScaleFrom: float | None = xScaleFrom
		self.xScaleTo: int | float | None = xScaleTo
		self.yScaleTo: int | float | None = yScaleTo
		self.text: str | None = text
		self.xscale: float | None = xscale
		self.yScaleT: float | None = yScaleT
		self.tiled: bool | None = tiled
		self.ease: str | None = ease
		self.width: int | None = width
		self.height: int | None = height
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
class Subtitle(Instruction):
	def __init__(self, raw_instruction: str, text: str | None = None, x: int | None = None, y: int | None = None, alignment: str | None = None, size: int | None = None, delay: int | float | None = None, width: int | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.text: str | None = text
		self.x: int | None = x
		self.y: int | None = y
		self.alignment: str | None = alignment
		self.size: int | None = size
		self.delay: int | float | None = delay
		self.width: int | None = width
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc
class subtitle(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc
class playsound(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, volume: int | float | None = None, loop: str | bool | None = None, channel: int | str | None = None, delay: int | float | None = None, Delay: float | None = None, fadetime: int | float | None = None, block: bool | None = None, text: str | None = None, voluyme: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.key: str | None = key
		self.volume: int | float | None = volume
		self.loop: str | bool | None = loop
		self.channel: int | str | None = channel
		self.delay: int | float | None = delay
		self.Delay: float | None = Delay
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.text: str | None = text
		self.voluyme: float | None = voluyme
		self.misc: dict[str, Any] = misc
class ImageTween(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, x: int | None = None, y: int | None = None, xScale: int | float | None = None, yScale: int | float | None = None, xTo: int | None = None, duration: int | float | None = None, xScaleFrom: int | str | float | None = None, yScaleFrom: int | float | None = None, xScaleTo: int | float | None = None, yScaleTo: int | float | None = None, block: bool | None = None, yTo: int | None = None, xFrom: int | float | None = None, yFrom: int | float | None = None, ease: str | None = None, fadetime: int | float | None = None, tiled: bool | None = None, screenadapt: str | None = None, yTO: int | None = None, xTO: int | None = None, xfromScale: int | None = None, yfromScale: int | None = None, yto: int | None = None, xfrom: int | None = None, yfrom: int | None = None, yT: int | None = None, xto: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.x: int | None = x
		self.y: int | None = y
		self.xScale: int | float | None = xScale
		self.yScale: int | float | None = yScale
		self.xTo: int | None = xTo
		self.duration: int | float | None = duration
		self.xScaleFrom: int | str | float | None = xScaleFrom
		self.yScaleFrom: int | float | None = yScaleFrom
		self.xScaleTo: int | float | None = xScaleTo
		self.yScaleTo: int | float | None = yScaleTo
		self.block: bool | None = block
		self.yTo: int | None = yTo
		self.xFrom: int | float | None = xFrom
		self.yFrom: int | float | None = yFrom
		self.ease: str | None = ease
		self.fadetime: int | float | None = fadetime
		self.tiled: bool | None = tiled
		self.screenadapt: str | None = screenadapt
		self.yTO: int | None = yTO
		self.xTO: int | None = xTO
		self.xfromScale: int | None = xfromScale
		self.yfromScale: int | None = yfromScale
		self.yto: int | None = yto
		self.xfrom: int | None = xfrom
		self.yfrom: int | None = yfrom
		self.yT: int | None = yT
		self.xto: int | None = xto
		self.misc: dict[str, Any] = misc
class image(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, screenadapt: str | None = None, xScale: int | float | None = None, yScale: int | float | None = None, x: int | None = None, y: int | None = None, fadetime: int | float | None = None, block: bool | None = None, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.screenadapt: str | None = screenadapt
		self.xScale: int | float | None = xScale
		self.yScale: int | float | None = yScale
		self.x: int | None = x
		self.y: int | None = y
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class cameraEffect(Instruction):
	def __init__(self, raw_instruction: str, effect: str | None = None, keep: bool | None = None, amount: int | float | None = None, fadetime: int | float | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.effect: str | None = effect
		self.keep: bool | None = keep
		self.amount: int | float | None = amount
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc
class chaa(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc
class PopupDialog(Instruction):
	def __init__(self, raw_instruction: str, dialogHead: str | None = None, text: str | None = None, dialogX: int | str | None = None, dialogY: int | str | None = None, animStyle: str | None = None, black: str | None = None, protectTime: int | float | None = None, focusX: int | None = None, focusY: int | None = None, focusWidth: int | None = None, focusHeight: int | None = None, anchor: str | None = None, focusStyle: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.dialogHead: str | None = dialogHead
		self.text: str | None = text
		self.dialogX: int | str | None = dialogX
		self.dialogY: int | str | None = dialogY
		self.animStyle: str | None = animStyle
		self.black: str | None = black
		self.protectTime: int | float | None = protectTime
		self.focusX: int | None = focusX
		self.focusY: int | None = focusY
		self.focusWidth: int | None = focusWidth
		self.focusHeight: int | None = focusHeight
		self.anchor: str | None = anchor
		self.focusStyle: str | None = focusStyle
		self.misc: dict[str, Any] = misc
class charslot(Instruction):
	def __init__(self, raw_instruction: str, slot: str | None = None, name: str | None = None, focus: str | None = None, duration: int | str | float | None = None, fadetime: int | float | None = None, bstart: int | float | None = None, bend: int | float | None = None, isblock: int | bool | None = None, posfrom: str | None = None, posto: int | str | None = None, afrom: int | str | float | None = None, ato: int | str | float | None = None, action: str | None = None, random: int | bool | None = None, power: int | float | None = None, times: int | None = None, poszoom: str | None = None, scale: int | float | None = None, foucs: str | None = None, block: bool | None = None, blocker: bool | None = None, end: bool | None = None, delay: float | None = None, grad: bool | None = None, text: str | None = None, ocus: str | None = None, posTo: str | None = None, duraiton: int | None = None, Duration: int | None = None, time: int | None = None, isblocke: bool | None = None, bstrart: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.slot: str | None = slot
		self.name: str | None = name
		self.focus: str | None = focus
		self.duration: int | str | float | None = duration
		self.fadetime: int | float | None = fadetime
		self.bstart: int | float | None = bstart
		self.bend: int | float | None = bend
		self.isblock: int | bool | None = isblock
		self.posfrom: str | None = posfrom
		self.posto: int | str | None = posto
		self.afrom: int | str | float | None = afrom
		self.ato: int | str | float | None = ato
		self.action: str | None = action
		self.random: int | bool | None = random
		self.power: int | float | None = power
		self.times: int | None = times
		self.poszoom: str | None = poszoom
		self.scale: int | float | None = scale
		self.foucs: str | None = foucs
		self.block: bool | None = block
		self.blocker: bool | None = blocker
		self.end: bool | None = end
		self.delay: float | None = delay
		self.grad: bool | None = grad
		self.text: str | None = text
		self.ocus: str | None = ocus
		self.posTo: str | None = posTo
		self.duraiton: int | None = duraiton
		self.Duration: int | None = Duration
		self.time: int | None = time
		self.isblocke: bool | None = isblocke
		self.bstrart: float | None = bstrart
		self.misc: dict[str, Any] = misc
class Showitem(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, fadetime: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.fadetime: float | None = fadetime
		self.misc: dict[str, Any] = misc
class hideitem(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | float | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc
class ShowItem(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, fadetime: int | float | None = None, style: str | None = None, fadestyle: str | None = None, offsetx: int | None = None, width: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.fadetime: int | float | None = fadetime
		self.style: str | None = style
		self.fadestyle: str | None = fadestyle
		self.offsetx: int | None = offsetx
		self.width: int | None = width
		self.misc: dict[str, Any] = misc
class Battle(Instruction):
	def __init__(self, raw_instruction: str, mask: str | None = None, charId: str | None = None, sp: int | None = None, pause: bool | None = None, cost: int | None = None, time: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.mask: str | None = mask
		self.charId: str | None = charId
		self.sp: int | None = sp
		self.pause: bool | None = pause
		self.cost: int | None = cost
		self.time: int | float | None = time
		self.misc: dict[str, Any] = misc
class InputBlocker(Instruction):
	def __init__(self, raw_instruction: str, blockInput: bool | None = None, validX: int | None = None, validY: int | None = None, validWidth: int | None = None, validHeight: int | None = None, cardIndex: int | None = None, tileX: int | None = None, tileY: int | None = None, black: int | float | None = None, rightStart: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.blockInput: bool | None = blockInput
		self.validX: int | None = validX
		self.validY: int | None = validY
		self.validWidth: int | None = validWidth
		self.validHeight: int | None = validHeight
		self.cardIndex: int | None = cardIndex
		self.tileX: int | None = tileX
		self.tileY: int | None = tileY
		self.black: int | float | None = black
		self.rightStart: bool | None = rightStart
		self.misc: dict[str, Any] = misc
class Tutorial(Instruction):
	def __init__(self, raw_instruction: str, protectTime: int | float | None = None, dialogHead: str | None = None, dialogX: int | str | None = None, dialogY: int | str | None = None, text: str | None = None, target: str | None = None, searchBtnInChildren: str | bool | None = None, animStyle: str | None = None, focusStyle: str | None = None, black: float | str | None = None, startX: int | None = None, startY: int | None = None, endX: int | None = None, endY: int | None = None, focusX: int | None = None, focusY: int | None = None, focusWidth: int | None = None, focusHeight: int | None = None, anchor: str | None = None, waitForSignal: str | None = None, startAnchor: str | None = None, endAnchor: str | None = None, cardIndex: int | None = None, rightStart: bool | None = None, tileX: float | None = None, tileY: int | None = None, importantClick: bool | None = None, abortForSignal: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.protectTime: int | float | None = protectTime
		self.dialogHead: str | None = dialogHead
		self.dialogX: int | str | None = dialogX
		self.dialogY: int | str | None = dialogY
		self.text: str | None = text
		self.target: str | None = target
		self.searchBtnInChildren: str | bool | None = searchBtnInChildren
		self.animStyle: str | None = animStyle
		self.focusStyle: str | None = focusStyle
		self.black: float | str | None = black
		self.startX: int | None = startX
		self.startY: int | None = startY
		self.endX: int | None = endX
		self.endY: int | None = endY
		self.focusX: int | None = focusX
		self.focusY: int | None = focusY
		self.focusWidth: int | None = focusWidth
		self.focusHeight: int | None = focusHeight
		self.anchor: str | None = anchor
		self.waitForSignal: str | None = waitForSignal
		self.startAnchor: str | None = startAnchor
		self.endAnchor: str | None = endAnchor
		self.cardIndex: int | None = cardIndex
		self.rightStart: bool | None = rightStart
		self.tileX: float | None = tileX
		self.tileY: int | None = tileY
		self.importantClick: bool | None = importantClick
		self.abortForSignal: str | None = abortForSignal
		self.misc: dict[str, Any] = misc
class focusout(Instruction):
	def __init__(self, raw_instruction: str, type: str | None = None, id: str | None = None, to: int | float | None = None, duration: int | float | None = None, block: bool | None = None, from_: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.type: str | None = type
		self.id: str | None = id
		self.to: int | float | None = to
		self.duration: int | float | None = duration
		self.block: bool | None = block
		self.from_: int | float | None = from_
		self.misc: dict[str, Any] = misc
class StopSound(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, fadetime: int | float | None = None, isblock: bool | None = None, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.fadetime: int | float | None = fadetime
		self.isblock: bool | None = isblock
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class PlayMusic(Instruction):
	def __init__(self, raw_instruction: str, intro: str | None = None, key: str | None = None, volume: int | float | None = None, crossfade: int | float | None = None, delay: int | float | None = None, fadetime: int | float | None = None, text: str | None = None, volu7me: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.intro: str | None = intro
		self.key: str | None = key
		self.volume: int | float | None = volume
		self.crossfade: int | float | None = crossfade
		self.delay: int | float | None = delay
		self.fadetime: int | float | None = fadetime
		self.text: str | None = text
		self.volu7me: float | None = volu7me
		self.misc: dict[str, Any] = misc
class SoundVolume(Instruction):
	def __init__(self, raw_instruction: str, volume: int | float | None = None, channel: str | None = None, fadetime: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: int | float | None = volume
		self.channel: str | None = channel
		self.fadetime: int | float | None = fadetime
		self.misc: dict[str, Any] = misc
class backgroundTween(Instruction):
	def __init__(self, raw_instruction: str, xScaleFrom: int | float | None = None, yScaleFrom: int | float | None = None, xScaleTo: int | float | None = None, yScaleTo: int | float | None = None, duration: int | float | None = None, block: bool | None = None, xTo: int | None = None, yTo: int | None = None, xFrom: int | None = None, yFrom: int | None = None, fadetime: float | None = None, xScale: float | None = None, yScale: float | None = None, xfrom: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xScaleFrom: int | float | None = xScaleFrom
		self.yScaleFrom: int | float | None = yScaleFrom
		self.xScaleTo: int | float | None = xScaleTo
		self.yScaleTo: int | float | None = yScaleTo
		self.duration: int | float | None = duration
		self.block: bool | None = block
		self.xTo: int | None = xTo
		self.yTo: int | None = yTo
		self.xFrom: int | None = xFrom
		self.yFrom: int | None = yFrom
		self.fadetime: float | None = fadetime
		self.xScale: float | None = xScale
		self.yScale: float | None = yScale
		self.xfrom: int | None = xfrom
		self.misc: dict[str, Any] = misc
class CameraEffect(Instruction):
	def __init__(self, raw_instruction: str, effect: str | None = None, amount: int | float | None = None, keep: bool | None = None, fadetime: int | float | None = None, initamount: int | float | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.effect: str | None = effect
		self.amount: int | float | None = amount
		self.keep: bool | None = keep
		self.fadetime: int | float | None = fadetime
		self.initamount: int | float | None = initamount
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc
class musicvolume(Instruction):
	def __init__(self, raw_instruction: str, volume: int | float | None = None, fadetime: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: int | float | None = volume
		self.fadetime: int | float | None = fadetime
		self.misc: dict[str, Any] = misc
class stopsound(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, fadetime: int | float | None = None, duration: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.fadetime: int | float | None = fadetime
		self.duration: int | float | None = duration
		self.misc: dict[str, Any] = misc
class multiline(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, text: str | None = None, end: bool | None = None, delay: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.text: str | None = text
		self.end: bool | None = end
		self.delay: float | None = delay
		self.misc: dict[str, Any] = misc
class bgeffect(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, layer: int | None = None, fade: bool | None = None, fadetime: int | float | None = None, x: int | None = None, xto: int | None = None, yto: int | None = None, movetime: int | None = None, flip: int | None = None, delay: int | None = None, y: int | None = None, duration: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.layer: int | None = layer
		self.fade: bool | None = fade
		self.fadetime: int | float | None = fadetime
		self.x: int | None = x
		self.xto: int | None = xto
		self.yto: int | None = yto
		self.movetime: int | None = movetime
		self.flip: int | None = flip
		self.delay: int | None = delay
		self.y: int | None = y
		self.duration: int | None = duration
		self.misc: dict[str, Any] = misc
class BackgroundTween(Instruction):
	def __init__(self, raw_instruction: str, xFrom: int | None = None, yFrom: int | None = None, xTo: int | None = None, yTo: int | None = None, xScaleFrom: int | float | None = None, yScaleFrom: int | float | None = None, xScaleTo: int | float | None = None, yScaleTo: int | float | None = None, duration: int | float | None = None, block: bool | None = None, image: str | None = None, x: int | None = None, y: int | None = None, xScale: float | None = None, yScale: float | None = None, screenadapt: str | None = None, yScaleto: float | None = None, ease: str | None = None, fadetime: int | float | None = None, else_: str | None = None, xto: int | None = None, yto: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xFrom: int | None = xFrom
		self.yFrom: int | None = yFrom
		self.xTo: int | None = xTo
		self.yTo: int | None = yTo
		self.xScaleFrom: int | float | None = xScaleFrom
		self.yScaleFrom: int | float | None = yScaleFrom
		self.xScaleTo: int | float | None = xScaleTo
		self.yScaleTo: int | float | None = yScaleTo
		self.duration: int | float | None = duration
		self.block: bool | None = block
		self.image: str | None = image
		self.x: int | None = x
		self.y: int | None = y
		self.xScale: float | None = xScale
		self.yScale: float | None = yScale
		self.screenadapt: str | None = screenadapt
		self.yScaleto: float | None = yScaleto
		self.ease: str | None = ease
		self.fadetime: int | float | None = fadetime
		self.else_: str | None = else_
		self.xto: int | None = xto
		self.yto: int | None = yto
		self.misc: dict[str, Any] = misc
class StopMusic(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | float | None = None, fadeetime: int | None = None, time: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | float | None = fadetime
		self.fadeetime: int | None = fadeetime
		self.time: int | float | None = time
		self.misc: dict[str, Any] = misc
class CharacterCutin(Instruction):
	def __init__(self, raw_instruction: str, widgetID: str | None = None, name: str | None = None, style: str | None = None, fadestyle: str | None = None, fadetime: int | float | None = None, offsetx: int | None = None, width: int | None = None, block: bool | None = None, povX: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.widgetID: str | None = widgetID
		self.name: str | None = name
		self.style: str | None = style
		self.fadestyle: str | None = fadestyle
		self.fadetime: int | float | None = fadetime
		self.offsetx: int | None = offsetx
		self.width: int | None = width
		self.block: bool | None = block
		self.povX: int | None = povX
		self.misc: dict[str, Any] = misc
class background(Instruction):
	def __init__(self, raw_instruction: str, screenadapt: str | None = None, image: str | None = None, xScale: int | float | None = None, yScale: int | float | None = None, y: int | None = None, fadetime: int | float | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.screenadapt: str | None = screenadapt
		self.image: str | None = image
		self.xScale: int | float | None = xScale
		self.yScale: int | float | None = yScale
		self.y: int | None = y
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc
class curtain(Instruction):
	def __init__(self, raw_instruction: str, direction: int | None = None, fillfrom: int | float | None = None, fillto: int | float | None = None, fadetime: int | float | None = None, grad: bool | None = None, block: bool | None = None, a: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.direction: int | None = direction
		self.fillfrom: int | float | None = fillfrom
		self.fillto: int | float | None = fillto
		self.fadetime: int | float | None = fadetime
		self.grad: bool | None = grad
		self.block: bool | None = block
		self.a: int | None = a
		self.misc: dict[str, Any] = misc
class interlude(Instruction):
	def __init__(self, raw_instruction: str, maskid: str | None = None, style: int | None = None, size: str | None = None, offset: str | None = None, channel: int | None = None, type: int | None = None, name: str | None = None, afrom: int | None = None, ato: int | None = None, aduration: int | float | None = None, sfrom: str | None = None, sto: str | None = None, sduration: int | None = None, block: bool | None = None, slot: str | None = None, clear: bool | None = None, pfrom: str | None = None, pto: str | None = None, duration: int | float | None = None, tsfrom: str | None = None, tsto: str | None = None, tsduration: int | float | None = None, switch: bool | None = None, char: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.maskid: str | None = maskid
		self.style: int | None = style
		self.size: str | None = size
		self.offset: str | None = offset
		self.channel: int | None = channel
		self.type: int | None = type
		self.name: str | None = name
		self.afrom: int | None = afrom
		self.ato: int | None = ato
		self.aduration: int | float | None = aduration
		self.sfrom: str | None = sfrom
		self.sto: str | None = sto
		self.sduration: int | None = sduration
		self.block: bool | None = block
		self.slot: str | None = slot
		self.clear: bool | None = clear
		self.pfrom: str | None = pfrom
		self.pto: str | None = pto
		self.duration: int | float | None = duration
		self.tsfrom: str | None = tsfrom
		self.tsto: str | None = tsto
		self.tsduration: int | float | None = tsduration
		self.switch: bool | None = switch
		self.char: str | None = char
		self.misc: dict[str, Any] = misc
class gridbg(Instruction):
	def __init__(self, raw_instruction: str, imagegroup: str | None = None, solidwidth: str | None = None, solidheight: str | None = None, x: int | None = None, fadetime: int | float | None = None, y: int | None = None, xScale: float | None = None, yScale: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.imagegroup: str | None = imagegroup
		self.solidwidth: str | None = solidwidth
		self.solidheight: str | None = solidheight
		self.x: int | None = x
		self.fadetime: int | float | None = fadetime
		self.y: int | None = y
		self.xScale: float | None = xScale
		self.yScale: float | None = yScale
		self.misc: dict[str, Any] = misc
class largebgtween(Instruction):
	def __init__(self, raw_instruction: str, duration: int | float | None = None, yFrom: int | None = None, yTo: int | None = None, block: bool | None = None, xFrom: int | None = None, xTo: int | None = None, xScaleFrom: int | None = None, xScaleTo: float | None = None, yScaleFrom: int | None = None, yScaleTo: float | None = None, xfrom: int | None = None, ease: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.duration: int | float | None = duration
		self.yFrom: int | None = yFrom
		self.yTo: int | None = yTo
		self.block: bool | None = block
		self.xFrom: int | None = xFrom
		self.xTo: int | None = xTo
		self.xScaleFrom: int | None = xScaleFrom
		self.xScaleTo: float | None = xScaleTo
		self.yScaleFrom: int | None = yScaleFrom
		self.yScaleTo: float | None = yScaleTo
		self.xfrom: int | None = xfrom
		self.ease: str | None = ease
		self.misc: dict[str, Any] = misc
class Characteraction(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, type: str | None = None, xpos: int | None = None, fadetime: int | float | None = None, block: bool | None = None, power: int | None = None, times: int | None = None, ypos: int | None = None, isblock: bool | None = None, pwoer: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.type: str | None = type
		self.xpos: int | None = xpos
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.power: int | None = power
		self.times: int | None = times
		self.ypos: int | None = ypos
		self.isblock: bool | None = isblock
		self.pwoer: int | None = pwoer
		self.misc: dict[str, Any] = misc
class MusicVolume(Instruction):
	def __init__(self, raw_instruction: str, volume: int | float | None = None, fadetime: int | float | None = None, channel: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: int | float | None = volume
		self.fadetime: int | float | None = fadetime
		self.channel: str | None = channel
		self.misc: dict[str, Any] = misc
class hideItem(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | None = fadetime
		self.misc: dict[str, Any] = misc
class stopSound(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, fadetime: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.fadetime: int | float | None = fadetime
		self.misc: dict[str, Any] = misc
class Stopmusic(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | float | None = fadetime
		self.misc: dict[str, Any] = misc
class delat(Instruction):
	def __init__(self, raw_instruction: str, time: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: float | None = time
		self.misc: dict[str, Any] = misc
class Video(Instruction):
	def __init__(self, raw_instruction: str, res: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.res: str | None = res
		self.misc: dict[str, Any] = misc
class delayt(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class dialo(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc
class Sticker(Instruction):
	def __init__(self, raw_instruction: str, id: str | None = None, multi: bool | None = None, text: str | None = None, x: int | None = None, y: int | None = None, alignment: str | None = None, size: int | None = None, delay: int | float | None = None, width: int | None = None, block: str | bool | None = None, fadetime: int | None = None, duration: int | float | None = None, hidelog: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.id: str | None = id
		self.multi: bool | None = multi
		self.text: str | None = text
		self.x: int | None = x
		self.y: int | None = y
		self.alignment: str | None = alignment
		self.size: int | None = size
		self.delay: int | float | None = delay
		self.width: int | None = width
		self.block: str | bool | None = block
		self.fadetime: int | None = fadetime
		self.duration: int | float | None = duration
		self.hidelog: bool | None = hidelog
		self.misc: dict[str, Any] = misc
class cgitem(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, style: str | None = None, layer: int | None = None, pfrom: str | None = None, pto: str | None = None, pduration: int | float | None = None, afrom: int | None = None, ato: int | None = None, aduration: int | float | None = None, sfrom: int | float | None = None, sto: int | float | None = None, sduration: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.style: str | None = style
		self.layer: int | None = layer
		self.pfrom: str | None = pfrom
		self.pto: str | None = pto
		self.pduration: int | float | None = pduration
		self.afrom: int | None = afrom
		self.ato: int | None = ato
		self.aduration: int | float | None = aduration
		self.sfrom: int | float | None = sfrom
		self.sto: int | float | None = sto
		self.sduration: int | float | None = sduration
		self.misc: dict[str, Any] = misc
class hidecgitem(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | None = None, image: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | None = fadetime
		self.image: str | None = image
		self.misc: dict[str, Any] = misc
class Effect(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, x: int | float | None = None, y: int | float | None = None, rox: int | float | None = None, roy: int | float | None = None, roz: int | float | None = None, layer: int | None = None, delay: int | float | None = None, xTo: int | None = None, movetime: float | None = None, yScale: int | None = None, z: int | None = None, ypos: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.x: int | float | None = x
		self.y: int | float | None = y
		self.rox: int | float | None = rox
		self.roy: int | float | None = roy
		self.roz: int | float | None = roz
		self.layer: int | None = layer
		self.delay: int | float | None = delay
		self.xTo: int | None = xTo
		self.movetime: float | None = movetime
		self.yScale: int | None = yScale
		self.z: int | None = z
		self.ypos: int | None = ypos
		self.misc: dict[str, Any] = misc
class Title(Instruction):
	def __init__(self, raw_instruction: str, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.text: str | None = text
		self.misc: dict[str, Any] = misc
class Div(Instruction):
	def __init__(self, raw_instruction: str, style: str | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.style: str | None = style
		self.text: str | None = text
		self.misc: dict[str, Any] = misc
class Narration(Instruction):
	def __init__(self, raw_instruction: str, text: str | None = None, style: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.text: str | None = text
		self.style: str | None = style
		self.misc: dict[str, Any] = misc
class largebg(Instruction):
	def __init__(self, raw_instruction: str, imagegroup: str | None = None, solidwidth: str | None = None, solidheight: int | None = None, x: int | None = None, y: int | None = None, fadetime: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.imagegroup: str | None = imagegroup
		self.solidwidth: str | None = solidwidth
		self.solidheight: int | None = solidheight
		self.x: int | None = x
		self.y: int | None = y
		self.fadetime: int | float | None = fadetime
		self.misc: dict[str, Any] = misc
class Charslot(Instruction):
	def __init__(self, raw_instruction: str, duration: int | float | None = None, slot: str | None = None, posfrom: str | None = None, posto: str | None = None, name: str | None = None, afrom: int | None = None, ato: int | None = None, isblock: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.duration: int | float | None = duration
		self.slot: str | None = slot
		self.posfrom: str | None = posfrom
		self.posto: str | None = posto
		self.name: str | None = name
		self.afrom: int | None = afrom
		self.ato: int | None = ato
		self.isblock: bool | None = isblock
		self.misc: dict[str, Any] = misc
class theater(Instruction):
	def __init__(self, raw_instruction: str, mode: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.mode: bool | None = mode
		self.misc: dict[str, Any] = misc
class imageTween(Instruction):
	def __init__(self, raw_instruction: str, xScaleTo: int | float | None = None, yScaleTo: int | float | None = None, duration: int | None = None, block: bool | None = None, xFrom: int | None = None, xTo: int | None = None, yFrom: int | None = None, yTo: int | None = None, ease: str | None = None, xScaleFrom: float | None = None, yScaleFrom: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xScaleTo: int | float | None = xScaleTo
		self.yScaleTo: int | float | None = yScaleTo
		self.duration: int | None = duration
		self.block: bool | None = block
		self.xFrom: int | None = xFrom
		self.xTo: int | None = xTo
		self.yFrom: int | None = yFrom
		self.yTo: int | None = yTo
		self.ease: str | None = ease
		self.xScaleFrom: float | None = xScaleFrom
		self.yScaleFrom: float | None = yScaleFrom
		self.misc: dict[str, Any] = misc
class showitem(Instruction):
	def __init__(self, raw_instruction: str, image: str | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.image: str | None = image
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc
class HideItem(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | float | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc
class stickerclear(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc
class soundvolume(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, volume: int | float | None = None, fadetime: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.volume: int | float | None = volume
		self.fadetime: int | float | None = fadetime
		self.misc: dict[str, Any] = misc
class imagerotate(Instruction):
	def __init__(self, raw_instruction: str, angle: int | None = None, fadetime: int | float | None = None, block: bool | None = None, isblock: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.angle: int | None = angle
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
		self.isblock: bool | None = isblock
		self.misc: dict[str, Any] = misc
class warp(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.misc: dict[str, Any] = misc
class imgeffect(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, image: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.image: str | None = image
		self.misc: dict[str, Any] = misc
class header(Instruction):
	def __init__(self, raw_instruction: str, actId: str | None = None, withdrawWithoutAnim: str | None = None, key: str | None = None, is_skippable: bool | None = None, fit_mode: str | None = None, npcId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.actId: str | None = actId
		self.withdrawWithoutAnim: str | None = withdrawWithoutAnim
		self.key: str | None = key
		self.is_skippable: bool | None = is_skippable
		self.fit_mode: str | None = fit_mode
		self.npcId: str | None = npcId
		self.misc: dict[str, Any] = misc
class camerafocusto(Instruction):
	def __init__(self, raw_instruction: str, offsetX: int | str | None = None, offsetY: int | float | str | None = None, time: str | None = None, scale: str | None = None, id: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.offsetX: int | str | None = offsetX
		self.offsetY: int | float | str | None = offsetY
		self.time: str | None = time
		self.scale: str | None = scale
		self.id: str | None = id
		self.misc: dict[str, Any] = misc
class resetcamera(Instruction):
	def __init__(self, raw_instruction: str, time: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: str | None = time
		self.misc: dict[str, Any] = misc
class end(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc
class avatarId(Instruction):
	def __init__(self, raw_instruction: str, avatarId: str | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.avatarId: str | None = avatarId
		self.text: str | None = text
		self.misc: dict[str, Any] = misc
class playSound(Instruction):
	def __init__(self, raw_instruction: str, key: str | None = None, volume: int | float | None = None, delay: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.key: str | None = key
		self.volume: int | float | None = volume
		self.delay: int | float | None = delay
		self.misc: dict[str, Any] = misc
class Act38D1(Instruction):
	def __init__(self, raw_instruction: str, slotId: str | None = None, slotType: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.slotId: str | None = slotId
		self.slotType: str | None = slotType
		self.misc: dict[str, Any] = misc
class Musicvolume(Instruction):
	def __init__(self, raw_instruction: str, volume: int | float | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: int | float | None = volume
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc
class playmusic(Instruction):
	def __init__(self, raw_instruction: str, intro: str | None = None, key: str | None = None, volume: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.intro: str | None = intro
		self.key: str | None = key
		self.volume: float | None = volume
		self.misc: dict[str, Any] = misc
class delau(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class dealy(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class Activity(Instruction):
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
class Interlock(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc
class Stopsound(Instruction):
	def __init__(self, raw_instruction: str, channel: str | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.channel: str | None = channel
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc
class Backgroundtween(Instruction):
	def __init__(self, raw_instruction: str, xScaleTo: int | float | None = None, yScaleTo: int | float | None = None, xTo: int | None = None, yTo: int | None = None, duration: int | float | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xScaleTo: int | float | None = xScaleTo
		self.yScaleTo: int | float | None = yScaleTo
		self.xTo: int | None = xTo
		self.yTo: int | None = yTo
		self.duration: int | float | None = duration
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc
class bgEffect(Instruction):
	def __init__(self, raw_instruction: str, layer: int | None = None, name: str | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.layer: int | None = layer
		self.name: str | None = name
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc
class narration(Instruction):
	def __init__(self, raw_instruction: str, delay: int | float | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.delay: int | float | None = delay
		self.text: str | None = text
		self.misc: dict[str, Any] = misc
class OptionBranch(Instruction):
	def __init__(self, raw_instruction: str, option0: str | None = None, option1: str | None = None, delay: int | None = None, option2: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.option0: str | None = option0
		self.option1: str | None = option1
		self.delay: int | None = delay
		self.option2: str | None = option2
		self.misc: dict[str, Any] = misc
class Obtain(Instruction):
	def __init__(self, raw_instruction: str, id: str | None = None, delay: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.id: str | None = id
		self.delay: float | None = delay
		self.misc: dict[str, Any] = misc
class VoiceWithin(Instruction):
	def __init__(self, raw_instruction: str, head: str | None = None, delay: int | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.head: str | None = head
		self.delay: int | None = delay
		self.text: str | None = text
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
class musicvolune(Instruction):
	def __init__(self, raw_instruction: str, volume: float | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: float | None = volume
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc
class predicate(Instruction):
	def __init__(self, raw_instruction: str, references: str | None = None, selectableCondition: str | None = None, visibleCondition: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.references: str | None = references
		self.selectableCondition: str | None = selectableCondition
		self.visibleCondition: str | None = visibleCondition
		self.misc: dict[str, Any] = misc
class AddItem(Instruction):
	def __init__(self, raw_instruction: str, itemId: str | None = None, itemCount: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.itemId: str | None = itemId
		self.itemCount: str | None = itemCount
		self.misc: dict[str, Any] = misc
class SetConditionProgress(Instruction):
	def __init__(self, raw_instruction: str, conditionKey: str | None = None, itemCount: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.conditionKey: str | None = conditionKey
		self.itemCount: str | None = itemCount
		self.misc: dict[str, Any] = misc
class withdraw(Instruction):
	def __init__(self, raw_instruction: str, charId: str | None = None, id: str | None = None, withoutAnim: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.charId: str | None = charId
		self.id: str | None = id
		self.withoutAnim: str | None = withoutAnim
		self.misc: dict[str, Any] = misc
class End(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

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
class stopmucis(Instruction):
	def __init__(self, raw_instruction: str, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc
class CooperateBattle(Instruction):
	def __init__(self, raw_instruction: str, enable: bool | None = None, offsetX: int | None = None, offsetY: int | float | None = None, scale: int | float | None = None, time: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.enable: bool | None = enable
		self.offsetX: int | None = offsetX
		self.offsetY: int | float | None = offsetY
		self.scale: int | float | None = scale
		self.time: int | float | None = time
		self.misc: dict[str, Any] = misc
class UIOperation(Instruction):
	def __init__(self, raw_instruction: str, target: str | None = None, enable: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.target: str | None = target
		self.enable: str | None = enable
		self.misc: dict[str, Any] = misc
class imagetween(Instruction):
	def __init__(self, raw_instruction: str, xScaleTo: int | None = None, yScaleTo: int | None = None, duration: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.xScaleTo: int | None = xScaleTo
		self.yScaleTo: int | None = yScaleTo
		self.duration: int | None = duration
		self.misc: dict[str, Any] = misc
class ConsumeGuideOnStoryEnd(Instruction):
	def __init__(self, raw_instruction: str, target: str | None = None, subsignal: str | None = None, showAnyway: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.target: str | None = target
		self.subsignal: str | None = subsignal
		self.showAnyway: bool | None = showAnyway
		self.misc: dict[str, Any] = misc
class effect(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, layer: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.layer: int | None = layer
		self.misc: dict[str, Any] = misc
class Carving(Instruction):
	def __init__(self, raw_instruction: str, position: int | None = None, cardId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.position: int | None = position
		self.cardId: str | None = cardId
		self.misc: dict[str, Any] = misc
class soundVolume(Instruction):
	def __init__(self, raw_instruction: str, volume: float | None = None, channel: str | None = None, fadetime: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.volume: float | None = volume
		self.channel: str | None = channel
		self.fadetime: int | None = fadetime
		self.misc: dict[str, Any] = misc
class backgroundtween(Instruction):
	def __init__(self, raw_instruction: str, yFrom: int | None = None, yTo: int | None = None, duration: int | float | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.yFrom: int | None = yFrom
		self.yTo: int | None = yTo
		self.duration: int | float | None = duration
		self.block: bool | None = block
		self.misc: dict[str, Any] = misc
class charslsot(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc
class palysound(Instruction):
	def __init__(self, raw_instruction: str, name: str | None = None, volume: int | float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.name: str | None = name
		self.volume: int | float | None = volume
		self.misc: dict[str, Any] = misc
class resetCamera(Instruction):
	def __init__(self, raw_instruction: str, times: str | None = None, time: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.times: str | None = times
		self.time: str | None = time
		self.misc: dict[str, Any] = misc
class summontrap(Instruction):
	def __init__(self, raw_instruction: str, x: str | None = None, y: str | None = None, charId: str | None = None, isChar: str | None = None, dir: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.x: str | None = x
		self.y: str | None = y
		self.charId: str | None = charId
		self.isChar: str | None = isChar
		self.dir: str | None = dir
		self.misc: dict[str, Any] = misc
class executeactionarray(Instruction):
	def __init__(self, raw_instruction: str, target: str | None = None, key: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.target: str | None = target
		self.key: str | None = key
		self.misc: dict[str, Any] = misc
class summonenemy(Instruction):
	def __init__(self, raw_instruction: str, enemyId: str | None = None, y: str | None = None, x: str | None = None, endX: str | None = None, endY: str | None = None, enemyAliasId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.enemyId: str | None = enemyId
		self.y: str | None = y
		self.x: str | None = x
		self.endX: str | None = endX
		self.endY: str | None = endY
		self.enemyAliasId: str | None = enemyAliasId
		self.misc: dict[str, Any] = misc
class playanim(Instruction):
	def __init__(self, raw_instruction: str, enemyAliasId: str | None = None, anim: str | None = None, looporidle: str | None = None, dir: str | None = None, charId: str | None = None, id: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.enemyAliasId: str | None = enemyAliasId
		self.anim: str | None = anim
		self.looporidle: str | None = looporidle
		self.dir: str | None = dir
		self.charId: str | None = charId
		self.id: str | None = id
		self.misc: dict[str, Any] = misc
class createeffect(Instruction):
	def __init__(self, raw_instruction: str, enemyAliasId: str | None = None, key: str | None = None, id: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.enemyAliasId: str | None = enemyAliasId
		self.key: str | None = key
		self.id: str | None = id
		self.misc: dict[str, Any] = misc
class CharSelect(Instruction):
	def __init__(self, raw_instruction: str, sortType: str | None = None, professionFilter: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.sortType: str | None = sortType
		self.professionFilter: str | None = professionFilter
		self.misc: dict[str, Any] = misc
class GotoPage(Instruction):
	def __init__(self, raw_instruction: str, dest: str | None = None, waitForSignal: str | None = None, zoneId: str | None = None, stageId: str | None = None, initMissionPage: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.dest: str | None = dest
		self.waitForSignal: str | None = waitForSignal
		self.zoneId: str | None = zoneId
		self.stageId: str | None = stageId
		self.initMissionPage: str | None = initMissionPage
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
class Building(Instruction):
	def __init__(self, raw_instruction: str, mode: str | None = None, roomId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.mode: str | None = mode
		self.roomId: str | None = roomId
		self.misc: dict[str, Any] = misc
class SandboxV2(Instruction):
	def __init__(self, raw_instruction: str, questId: str | None = None, focusType: str | None = None, enemyRushGroupKey: str | None = None, isForceTutorial: bool | None = None, zoomType: str | None = None, focusNodeId: str | None = None, itemId: str | None = None, itemCount: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.questId: str | None = questId
		self.focusType: str | None = focusType
		self.enemyRushGroupKey: str | None = enemyRushGroupKey
		self.isForceTutorial: bool | None = isForceTutorial
		self.zoomType: str | None = zoomType
		self.focusNodeId: str | None = focusNodeId
		self.itemId: str | None = itemId
		self.itemCount: int | None = itemCount
		self.misc: dict[str, Any] = misc
class SandboxBattle(Instruction):
	def __init__(self, raw_instruction: str, offsetY: int | float | None = None, offsetX: int | None = None, time: int | float | None = None, enable: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.offsetY: int | float | None = offsetY
		self.offsetX: int | None = offsetX
		self.time: int | float | None = time
		self.enable: bool | None = enable
		self.misc: dict[str, Any] = misc
class CrisisV2(Instruction):
	def __init__(self, raw_instruction: str, mapType: str | None = None, slotType: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.mapType: str | None = mapType
		self.slotType: str | None = slotType
		self.misc: dict[str, Any] = misc
class GotoCharInfo(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

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
class dalay(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class blocker(Instruction):
	def __init__(self, raw_instruction: str, a: int | float | None = None, r: int | None = None, g: int | None = None, b: int | None = None, fadetime: int | float | None = None, block: bool | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.a: int | float | None = a
		self.r: int | None = r
		self.g: int | None = g
		self.b: int | None = b
		self.fadetime: int | float | None = fadetime
		self.block: bool | None = block
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
class fadetime(Instruction):
	def __init__(self, raw_instruction: str, fadetime: float | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.fadetime: float | None = fadetime
		self.misc: dict[str, Any] = misc
class DELAY(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class skipnode(Instruction):
	def __init__(self, raw_instruction: str, mode: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.mode: str | None = mode
		self.misc: dict[str, Any] = misc
class daley(Instruction):
	def __init__(self, raw_instruction: str, time: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.time: int | None = time
		self.misc: dict[str, Any] = misc
class duration(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc
class decision(Instruction):
	def __init__(self, raw_instruction: str, option1: str | None = None, value1: str | None = None, option2: str | None = None, value2: str | None = None, option3: str | None = None, value3: str | None = None, option4: str | None = None, value4: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.option1: str | None = option1
		self.value1: str | None = value1
		self.option2: str | None = option2
		self.value2: str | None = value2
		self.option3: str | None = option3
		self.value3: str | None = value3
		self.option4: str | None = option4
		self.value4: str | None = value4
		self.misc: dict[str, Any] = misc
class additem(Instruction):
	def __init__(self, raw_instruction: str, itemId: str | None = None, itemCount: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.itemId: str | None = itemId
		self.itemCount: str | None = itemCount
		self.misc: dict[str, Any] = misc
class save(Instruction):
	def __init__(self, raw_instruction: str, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)

		self.misc: dict[str, Any] = misc
class condition(Instruction):
	def __init__(self, raw_instruction: str, references: str | None = None, key: str | None = None, itemId: str | None = None, value: str | None = None, riftId: str | None = None, trapId: str | None = None, val: str | None = None, containsEq: int | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.references: str | None = references
		self.key: str | None = key
		self.itemId: str | None = itemId
		self.value: str | None = value
		self.riftId: str | None = riftId
		self.trapId: str | None = trapId
		self.val: str | None = val
		self.containsEq: int | None = containsEq
		self.misc: dict[str, Any] = misc
class foginview(Instruction):
	def __init__(self, raw_instruction: str, leftBottomX: int | str | None = None, leftBottomY: int | str | None = None, rightUpX: int | str | None = None, rightUpY: int | str | None = None, id: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.leftBottomX: int | str | None = leftBottomX
		self.leftBottomY: int | str | None = leftBottomY
		self.rightUpX: int | str | None = rightUpX
		self.rightUpY: int | str | None = rightUpY
		self.id: str | None = id
		self.misc: dict[str, Any] = misc
class uioperation(Instruction):
	def __init__(self, raw_instruction: str, target: str | None = None, item: str | None = None, enable: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.target: str | None = target
		self.item: str | None = item
		self.enable: str | None = enable
		self.misc: dict[str, Any] = misc
class emoji(Instruction):
	def __init__(self, raw_instruction: str, target: str | None = None, emoji: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.target: str | None = target
		self.emoji: str | None = emoji
		self.misc: dict[str, Any] = misc
class fognotinview(Instruction):
	def __init__(self, raw_instruction: str, id: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.id: str | None = id
		self.misc: dict[str, Any] = misc
class orderrift(Instruction):
	def __init__(self, raw_instruction: str, riftId: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.riftId: str | None = riftId
		self.misc: dict[str, Any] = misc
class move(Instruction):
	def __init__(self, raw_instruction: str, enemyId: str | None = None, x: str | None = None, y: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.enemyId: str | None = enemyId
		self.x: str | None = x
		self.y: str | None = y
		self.misc: dict[str, Any] = misc
class gacha(Instruction):
	def __init__(self, raw_instruction: str, gachaPool: str | None = None, cnt: str | None = None, all: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.gachaPool: str | None = gachaPool
		self.cnt: str | None = cnt
		self.all: str | None = all
		self.misc: dict[str, Any] = misc
class isAvatarRight(Instruction):
	def __init__(self, raw_instruction: str, isAvatarRight: str | None = None, text: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.isAvatarRight: str | None = isAvatarRight
		self.text: str | None = text
		self.misc: dict[str, Any] = misc
class camerascale(Instruction):
	def __init__(self, raw_instruction: str, scale: str | None = None, time: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.scale: str | None = scale
		self.time: str | None = time
		self.misc: dict[str, Any] = misc
class addfavor(Instruction):
	def __init__(self, raw_instruction: str, trapId: str | None = None, val: str | None = None, **misc: dict[str, Any]) -> None:
		super().__init__(raw_instruction)
		self.trapId: str | None = trapId
		self.val: str | None = val
		self.misc: dict[str, Any] = misc
