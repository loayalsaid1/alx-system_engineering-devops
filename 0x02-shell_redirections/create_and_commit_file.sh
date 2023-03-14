#!/bin/bash

# check if filename and message are provided
if [ -z "$1" ] || [ -z "$2" ]
then
  echo "Usage: create_and_commit_file.sh <filename> <text>"
  exit 1
fi

# create file and open it with vi
touch "$1"
vi "$1"

# add shebang and blank line
sed -i '1i#!/bin/bash\n' "$1"
sed -i '2i' "$1"

# add file name to commit message and commit changes
commit_message="Add $1"
echo "$1: $2" >> "README.md"
git add "$1" "README.md"
git commit -m "$commit_message"
git push

# remove the file name from the text and append it to the README.md file
text=${2/$1/}
echo "$1: $text" >> "README.md"
git add "README.md"
git commit --amend -m "$commit_message"
git push -f

