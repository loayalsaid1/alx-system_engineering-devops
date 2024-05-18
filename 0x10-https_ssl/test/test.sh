#!/usr/bin/env bash
function ages() {
    array=(41 21 14 13)
    echo "${array[@]}"
}

result=$(ages)
result_array=($result)
echo ${result_array[@]}
