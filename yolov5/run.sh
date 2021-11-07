# componenst
python -m torch.distributed.launch --nproc_per_node 2 train.py \
--save_period 1 \
--data ricoco.yaml \
--project ricoco \
--name ricoco \
--freeze 10 --batch-size 128 --adam --patience 10

python val.py \
--task test \
--save-txt \
--verbose \
--data ricoco.yaml \
--project ricoco \
--name ricoco \
--weights ricoco/ricoco/weights/best.pt

# icons
python -m torch.distributed.launch --nproc_per_node 2 train.py \
--save_period 1 \
--data ricoco_icon_legend.yaml \
--project ricoco_icon_legend \
--name ricoco_icon_legend \
--freeze 10 --batch-size 128 --adam --patience 10

python val.py \
--task test \
--save-txt \
--verbose \
--data ricoco_icon_legend.yaml \
--project ricoco_icon_legend \
--name ricoco_icon_legend \
--weights ricoco_icon_legend/ricoco_icon_legend/weights/best.pt

# click
python -m torch.distributed.launch --nproc_per_node 2 train.py \
--save_period 1 \
--data rico2coco_clickable.yaml \
--project rico2coco_clickable \
--name rico2coco_clickable \
--freeze 10 --batch-size 128 --adam --patience 10

python val.py \
--task test \
--save-txt \
--verbose \
--data rico2coco_clickable.yaml \
--project rico2coco_clickable \
--name rico2coco_clickable \
--weights rico2coco_clickable/rico2coco_clickable/weights/best.pt