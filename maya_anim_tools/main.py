import importlib
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print("MAYA_SCRIPT_PATH ENV set")

import interface
importlib.reload(interface)

def run():
    interface.main()
    print("Launching interface...")
