docker run -it -d --name yolov5 --ipc=host --gpus all -v "$(pwd)"/datasets:/usr/src/datasets/rico2coco ultralytics/yolov5:latest
