import click

import rico2coco


@click.command()
def run():
    rico2coco.run()
