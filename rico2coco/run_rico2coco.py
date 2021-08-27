import json
import sys

from rico2coco import run

sys.path.append("./rico2coco")

ricoco = run(label_key="clickable")
with open("ricoco_clickable.json", "w") as f:
    json.dump(ricoco, f)
