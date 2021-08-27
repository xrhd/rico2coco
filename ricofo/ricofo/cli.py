import click
from __init__ import *


@click.command()
@click.option("--images", default=IMAGES_DIR, help="Directory of images.")
@click.option(
    "--annotation",
    default=ANNOTATION_PATH,
    help="Path to coco format image annotations.",
)
@click.option(
    "--samples",
    default=MAX_SAMPLES,
    help="Path to coco format image annotations.",
)
def run(images, annotation, samples):
    main(images, annotation, samples)


if __name__ == "__main__":
    run()
