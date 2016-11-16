#!/bin/bash

fl=()
while IFS= read -d $'\0' -r file ; do
     fl=("${fl[@]}" "$file")
done < <(find . -maxdepth 1 -type f -print0)

for((i=0;i<${#fl[@]};i++)); do
    mv "${fl[i]}" $i.jpg
done
