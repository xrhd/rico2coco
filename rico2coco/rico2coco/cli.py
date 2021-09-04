import json

import __init__ as rico2coco
import click


@click.command()
@click.option("--labelkey", default=rico2coco.LABEL_KEY, help="Directory of images.")
def run(labelkey):
    ricoco = rico2coco.run(labelkey)
    with open("ricoco.json", "w") as f:
        json.dump(ricoco, f)


if __name__ == "__main__":
    run()
