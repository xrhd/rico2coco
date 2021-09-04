docker run -it -d --name yolov5 --ipc=host --gpus all -v "$(pwd)"/coco:/usr/src/coco ultralytics/yolov5:latest
