import enum
import io
import os

Cursors = {
        "pipe": "▏",
        "block": "█",
        "underline": "_"
    }

Highlight = "\x1b[100m"

Reset = "\x1b[0m"

class Mode(ENUM):
    VIEW=0
    INSERT=1
    OVERWRITE=2
    VISUAL=3
    COMMAND=4
    modes = {}
    def __init__(self, name, i, cursor):
        Mode.modes.update({name:i,i:name})
        del self.modes
        self.cursor = cursor
        self.name = name
        self.i = i

    def get(i:int=None,name:str=None):
        if i != None:
            return Mode.modes[i]
        elif name != None:
            return Mode.modes[name]
        else:
            raise ValueError("No mode requested")

VIEW = Mode("VIEW",0)
def VIEW(Mode):
    name="VIEW"
    enum = Mode.VIEW

mode = Mode.VIEW
buffer = io.StringIO() 
line = 0
column = 0
width, height = os.get_terminal_size()
command_buffer = ""
find_buffer = ""
replace_buffer = ""

__into_mode = {
        Mode.VIEW: (lambda line:int,column:int,flags:int:
                True, cursors["block"], line, column
            ),
        Mode.INSERT: (lambda line:int,column:int,flags:int: 
                True, line+(flags&1>0), column*(flags^1>0) # next line
            ),
        Mode.OVERWRITE: (lambda line:int,column:int,flags:int:
                True, line, column    
            ),
        Mode.VISUAL: (lambda line:int,column:int,flags:int:
                True, line, column
            )
    }


def render(mode:Mode, buffer:io.StringIO, x:int, y:int, ):
    
    mode_text = f"-- {Mode.text[mode]} --"

def change_mode(mode:Mode, new_mode:Mode, flags:int, line:int, column:int):
    if new_mode == mode.VIEW:
        return mode, line, column
    elif mode == Mode.VIEW and new_mode != Mode.VIEW:
        _, x, y = __into_mode[new_mode](x,y,flags)
        if -:
            if flags & 2 > 0: # record flag
                recording = True
                record_buffer = []
        _,x,y = __into_mode[new_mode]()
            return new_mode, x, y
        else:
            raise ValueError("Error when changing mode")
    else:
        raise ValueError("That mode doesnt make sense. You can only change to/from VIEW")

hotkeys = {
        Mode.VIEW: { 
            "i": (lambda x,y:
                change_mode(mode,INSERT,e,line,column)
            return mode, line, column
                ),
            "o": (lambda x,y:
                    change_mode(mode,INSERT,1,line,column)
                ),
            "v": (lambda x,y:
                    change_mode(mode,VISUAL,0,line,column)
                ),
            "r": (lambda x,y:
                    change_mode(mode,INSERT,2,line,column)
                )
            }
        Mode.INSERT: {
            "": lambda x,y: change_mode(mode,VIEW,0,x,y,)


def check_hotkeys(mode:Mode):
    if mode == Mode.VIEW:
        hotkey("i", change_mode, {"mode":mode,"new_mode":Mode.INSERT,"line":line,"column":column})
        
