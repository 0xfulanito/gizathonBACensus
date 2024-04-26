#!/bin/bash

for file in onnx/*.onnx; do
    filename=$(basename "$file")
    filename_without_extension="${filename%.*}"
    giza transpile "$file" --output-path "verifiable_lr/$filename_without_extension"
done