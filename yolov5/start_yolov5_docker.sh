docker run -it -d --name yolov5 --ipc=host --gpus all -v "$(pwd)"/../ric2coco/rico/coco:/usr/src/coco ultralytics/yolov5:latest
