import sys
import json
from rico2coco import run


sys.path.append("./rico2coco")

ricoco = run()
with open("ricoco.json", "w") as f:
    json.dump(ricoco, f)
