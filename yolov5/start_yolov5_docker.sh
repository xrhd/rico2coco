docker build -t yolov5_wandb . &&
docker run -it -d --name yolov5 --ipc=host --gpus all -v "$(pwd)"/datasets:/usr/src/datasets yolov5_wandb
