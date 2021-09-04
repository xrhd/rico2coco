import os
import os.path

from shutil import copyfile
from pycocotools.coco import COCO

COCO_ANNOTATIONS = "../dataset/ricoco_clickable.json"
IMAGES_PATH = "../rico2coco/rico/dataset/combined/"
OUTPUT_PATH = "datasets/"


# Truncates numbers to N decimals
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def main(coco_annotations):
    coco = COCO(coco_annotations)
    cats = coco.loadCats(coco.getCatIds())
    nms=[cat['name'] for cat in cats]
    print('COCO categories: \n{}\n'.format(' '.join(nms)))

    catIds = coco.getCatIds()
    imgIds = coco.getImgIds(catIds=catIds )
    images = coco.loadImgs(imgIds)
    print(catIds, imgIds)

    # This creates a symbolic link on python in tmp directory
    output_image_path = f"{OUTPUT_PATH}/images/"
    os.makedirs(output_image_path, exist_ok=True)

    for image in images:
        file_name = image["file_name"]
        src = f"{IMAGES_PATH}/{file_name}"
        dst = f"{output_image_path}/{file_name}"
        if not(os.path.exists(dst) or os.path.islink(dst)):
            # os.symlink(src, dst)
            copyfile(src, dst)

    # This is where the annotations will be saved in YOLO format
    output_label_path = f"{OUTPUT_PATH}/labels/"
    os.makedirs(output_label_path, exist_ok=True)
    for im in images:
        dw = 1. / im['width']
        dh = 1. / im['height']
        
        annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)
        
        filename = im['file_name'].replace(".jpg", ".txt")
        print(filename)

        with open(output_label_path + filename, "a") as myfile:
            for i in range(len(anns)):
                xmin = anns[i]["bbox"][0]
                ymin = anns[i]["bbox"][1]
                xmax = anns[i]["bbox"][2] + anns[i]["bbox"][0]
                ymax = anns[i]["bbox"][3] + anns[i]["bbox"][1]
                
                x = (xmin + xmax)/2
                y = (ymin + ymax)/2
                
                w = xmax - xmin
                h = ymax-ymin
                
                x = x * dw
                w = w * dw
                y = y * dh
                h = h * dh
                
                # Note: This assumes a single-category dataset, and thus the "0" at the beginning of each line.
                mystring = str("0 " + str(truncate(x, 7)) + " " + str(truncate(y, 7)) + " " + str(truncate(w, 7)) + " " + str(truncate(h, 7)))
                myfile.write(mystring)
                myfile.write("\n")

        myfile.close()


if __name__ == "__main__":
    main(COCO_ANNOTATIONS)
