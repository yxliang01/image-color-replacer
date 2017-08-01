#!/bin/bash

# Author: Xiao Liang Yu
# Arguments: PATH_TO_PDF PATH_TARGET ORIGIN_COLOR TARGET_COLOR
# NOTE: PATH_TO_PDF has to be absolute path

PATH_REPLACER_SCRIPT=$(realpath "../image-color-replacer.py")

cd $(mktemp -d)
pdftoppm -png "$1" png
mkdir out
for i in ./png*.png; do 
	python3 "$PATH_REPLACER_SCRIPT" "$i" "out/$i" "(0,0,0)" "(0,0,255)";
done

mv out "$2"

# rm -r .