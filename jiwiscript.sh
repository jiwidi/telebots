#!/bin/bash
# may also run on /bin/bash/elconsersh
#

fl=()
while IFS= read -d $'\0' -r file ; do
     fl=("${fl[@]}" "$file")
done < <(find . -maxdepth 1 -type f -print0)

for((i=0;i<${#fl[@]};i++)); do
    mv "${fl[i]}" $i.$(echo ${fl[i]} | rev | cut -d'.' -f 1 | rev)
done
