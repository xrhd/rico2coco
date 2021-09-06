# notes

```
richard@gpu12:~/_rico2coco/rico2coco$ sed '20001,22500!d' rico_sca_filter.txt | sed -e 's/json/jpg/g' | sed -e 's/^/rico\/dataset\/images_cp\//' | xargs mv -t rico/dataset/images/val
richard@gpu12:~/_rico2coco/rico2coco$ sed '22501,25000!d' rico_sca_filter.txt | sed -e 's/json/jpg/g' | sed -e 's/^/rico\/dataset\/images_cp\//' | xargs mv -t rico/dataset/images/test

```
`sed '1,20000!d' rico_sca_filter.txt | sed -e 's/json/jpg/g' | sed -e 's/^/rico\/dataset\/image_cp\//' | xargs mv -t rico/dataset/images/train/`

`ils images/val/ | sed -e 's/jpg/txt/g' | sed -e 's/^/labels\//' | xargs mv -t labels/val`
