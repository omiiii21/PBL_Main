echo "Enter file name:" 	 #Create new file
read fn
touch $fn
echo "$fn Created!!" 	#Message for successful file creation to user
echo -e "\n Enter content in $fn file:"	#Ask user to enter content into the file
cat>$fn
echo "Content in sorted manner is as follows:" 
sort $fn
echo "Content in reverse order is as follows:"
tac $fn 
echo "Content in Uppercase is as follows:"
cat $fn | tr 'a-z' 'A-Z' <$fn
echo "Enter the keyword to be searched"
read s
echo "The lines are:"
grep $s $fn
echo "Enter the position from where content is to be cut:"
read x
echo "The $x character is:"
cut -c$x $fn
echo "Enter the no. of lines to be printed form head:"
read n
echo "The content of line from head ts as follows:"
head -$n $fn
echo "The word count of $fn is:"
wc $fn
echo "enter a new file name:"
read newname
ls
mv $fn $newname
echo "Enter the file name to be deleted:"
read delfile
rm $delfile
ls
echo "$delfile Deleted"