"""Module to help students understanding their exceptions.
Just a POC, do not use.
"""

import dis
import traceback
import sys
import gettext
from pathlib import Path

__version__ = "0.0.1"

gettext.bindtextdomain('teacher', Path(__file__).resolve().parent / "locale")
gettext.textdomain('teacher')
_ = gettext.gettext

def excepthook(type, value, tb):
    t0 = traceback.StackSummary.extract(traceback.walk_tb(tb), limit=1, capture_locals=True)[0]
    errstr = traceback.format_exception_only(type, value)[0].strip()
    bytecode = dis.Bytecode.from_traceback(tb)
    instructions = list(bytecode)
    misbehaving_instruction_id = {j: i for i, j in enumerate([i.offset for i in instructions])}[bytecode.current_offset]
    misbehaving_instruction = instructions[misbehaving_instruction_id]
    print(f"{t0.filename}:{t0.lineno}:", errstr)
    if errstr == "TypeError: can't multiply sequence by non-int of type 'str'":
        right = instructions[misbehaving_instruction_id - 1]
        left = instructions[misbehaving_instruction_id - 2]
        print(f"You tried to multiply {left.argrepr} by {right.argrepr}")
        print(f"which is not allowed, the sequence {left.argrepr} can only be multiplied by an integer.")


sys.excepthook = excepthook
