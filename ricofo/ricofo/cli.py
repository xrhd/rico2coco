import click
from __init__ import *


@click.command()
@click.option("--images", default=IMAGES_DIR, help="Directory of images.")
@click.option(
    "--annotation",
    default=ANNOTATION_PATH,
    help="Path to coco format image annotations.",
)
def run(images, annotation):
    main(images, annotation)


if __name__ == "__main__":
    run()
