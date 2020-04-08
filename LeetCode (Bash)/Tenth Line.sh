# Read from the file file.txt and output the tenth line to stdout.
# $t = "0"
# echo "$VAR1"
# cat file.txt
t="${t:-1}"
while IFS= read line; do
if [ $t = 10 ]; then
echo "$line"
fi
t=$((t + 1))
done < file.txt
if [ $t = 10 ]; then
echo "$line"
fi