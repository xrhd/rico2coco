import __init__ as rico2coco
import click


@click.command()
@click.option("--labelkey", default=rico2coco.LABEL_KEY, help="Directory of images.")
def run(labelkey):
    d = rico2coco.run(labelkey)
    print(d.keys())


if __name__ == "__main__":
    run()
