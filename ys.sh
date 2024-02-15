#!/bin/bash
for file in path/*; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")  # 获取文件名部分
    extension="${filename##*.}"  # 获取文件扩展名
    filename="${filename%.*}"  # 去掉文件的扩展名部分
    if [[ $file == *.exe ]]; then
      zip -FSr "path/${filename}.zip" "$file"
      rm "$file"
    elif [[ $file == *.zip ]] || [[ $file == *.gz ]]; then
      continue  # 如果是已经压缩的文件则跳过
    else
      gzip -c "$file" > "path/${filename}.gz"  # 使用-gc选项将压缩输出到新文件中
      rm "$file"
    fi
  fi
done
