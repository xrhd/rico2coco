docker run -it -d --name yolov5 --ipc=host --gpus all -v "$(pwd)"/../rico2coco/rico/yolov5:/usr/src/rico2coco ultralytics/yolov5:latest
