#!/bin/bash

BASE_DIR="submissions"

for dir in "$BASE_DIR"/*/; do
	dir_name=$(basename "$dir")

	find "$dir" -path "*/Accepted/*" -type f -name "Solution.*" | while read -r file; do
		extension="${file##*.}"
		new_file="$BASE_DIR/$dir_name.$extension"

		if [[ -e "$new_file" ]]; then
			i=1
			while [[ -e "$BASE_DIR/$dir_name-$i.$extension" ]]; do
				((i++))
			done
			new_file="$BASE_DIR/$dir_name-$i.$extension"
		fi

		mv "$file" "$new_file"
	done
done

rm -r "${BASE_DIR:?}"/*/

echo "Done"
