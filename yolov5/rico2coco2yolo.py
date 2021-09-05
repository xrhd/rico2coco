import os
import os.path
from shutil import copyfile

from pycocotools.coco import COCO
from tqdm import tqdm

USE_SYMLINK = True
COCO_ANNOTATIONS = "../dataset/ricoco_clickable.json"
IMAGES_PATH = os.path.abspath("../rico2coco/rico/dataset/combined/")
OUTPUT_PATH = "datasets/rico2coco_clickable/"


# Truncates numbers to N decimals
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def main(coco_annotations, image_path, output_path, use_symlink=True):
    coco = COCO(coco_annotations)
    cats = coco.loadCats(coco.getCatIds())
    nms = [cat["name"] for cat in cats]
    print("COCO categories: \n{}\n".format(" ".join(nms)))

    catIds = coco.getCatIds()
    imgIds = coco.getImgIds(catIds=catIds)
    images = coco.loadImgs(imgIds)

    # # This creates a symbolic link on python in tmp directory
    # output_image_path = f"{output_path}/images/"
    # os.makedirs(output_image_path, exist_ok=True)

    # for image in tqdm(images):
    #     file_name = image["file_name"]
    #     src = f"{image_path}/{file_name}"
    #     dst = f"{output_image_path}/{file_name}"

    #     if not os.path.exists(src):
    #         raise Exception(f"do not exits: {src}")

    #     # if not (os.path.exists(dst) or os.path.islink(dst)):
    #     if use_symlink:
    #         os.symlink(src, dst)
    #     else:
    #         copyfile(src, dst)

    # This is where the annotations will be saved in YOLO format
    output_label_path = f"{output_path}/labels/"
    os.makedirs(output_label_path, exist_ok=True)
    for im in tqdm(images):
        dw = 1.0 / im["width"]
        dh = 1.0 / im["height"]

        annIds = coco.getAnnIds(imgIds=im["id"], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)

        filename = im["file_name"].replace(".jpg", ".txt")

        txt_content = []
        for i in range(len(anns)):
            category_id = anns[i]["category_id"] - 1
            
            xmin = anns[i]["bbox"][0]
            ymin = anns[i]["bbox"][1]
            xmax = anns[i]["bbox"][2] + anns[i]["bbox"][0]
            ymax = anns[i]["bbox"][3] + anns[i]["bbox"][1]

            x = (xmin + xmax) / 2
            y = (ymin + ymax) / 2

            w = xmax - xmin
            h = ymax - ymin

            x = x * dw
            w = w * dw
            y = y * dh
            h = h * dh

            mystring = str(
                f"{category_id} "
                + str(truncate(x, 7))
                + " "
                + str(truncate(y, 7))
                + " "
                + str(truncate(w, 7))
                + " "
                + str(truncate(h, 7))
            )
            txt_content.append(mystring)

        with open(output_label_path + filename, "w") as myfile:
            for line in txt_content:
                myfile.write(line+"\n")

if __name__ == "__main__":
    main(COCO_ANNOTATIONS, IMAGES_PATH, OUTPUT_PATH, USE_SYMLINK)
