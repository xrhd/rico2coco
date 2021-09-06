`sed '1,20000!d' rico_sca_filter.txt | sed -e 's/json/jpg/g' | sed -e 's/^/rico\/dataset\/image_cp\//' | xargs mv -t rico/dataset/images/train/`
