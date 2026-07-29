# Linux Commands
Display the message "Hello, World!"
```bash
$ echo Hello, World!
```
Print Working Directory
```bash
$ pwd
```
Current Directory
```bash
$ cd .
```
Parent Directory
```bash
$ cd .. 
```
Change Directory
```bash
$ cd Directory/
```
Change directory (out current directory and in another directory)
```bash
$ cd ../dir_name
```
List all the contents within a directory
```bash
$ ls
```
List all the contents with additional information
```bash
$ ls -l
```
List all the contents with additional information in chronological order 
```bash
$ ls -lt
```
List all the contents with additional information in reverse chronological order 
```bash
$ ls -ltr
```
List all the files with a prefix (file)
```bash
$ ls file*
```
List all the files with a suffix (.txt)
```bash
$ ls *.txt
```
List all the files with prefix (file, ecoli, lacz) and suffix (.txt)
```bash
$ ls {file,ecoli,lacz}*.txt
```
List all the files with (a to z) initial letters and suffix (.txt)
```bash
$ ls [a-z]*.txt
```
List all the files with (a) initial letters and suffix (.txt)
```bash
$ ls a*.txt
```
File copying
```bash
$ cp file.txt dir_name
$ cp file1.txt file2.txt dir_name
$ cp file.txt path/to/dir
```
File moving
```bash
$ mv file.txt dir_name
$ mv file.txt path/to/dir
```
File creation
```bash
$ touch file.txt
$ touch file1.txt file2.txt file3.txt
```
Removing a file
```bash
$ rm file.txt
```
Removing a file while asking for confirmation y/n
```bash
$ rm -i file.txt
```
Creating a directory
```bash
$ mkdir dir_name
```
Removing an empty directory
```bash
$ rmdir dir_name
```
Removing a directory
```bash
$ rm -r dir_name
```
File viewing; more(unidirectional viewing) less(bidirectional viewing)
```bash
$ more file.txt
$ less file.txt
```
View top 10 lines of a file
```bash
$ head file.txt
```
View top 50 lines of a file
```bash
$ head -50 file.txt
```
View bottom 10 lines of a file
```bash
$ tail file.txt
```
View bottom 50 lines of a file
```bash
$ tail -50 file.txt
```
File reading and concatenation (cat: concatenate)

Reading the file content
```bash
$ cat file.txt
```
Concatenate two files
```bash
$ cat file1.txt file2.txt
```
Concatenate two files and create a new file having the content of both the files
```bash
$ cat file1.txt file2.txt > file3.txt
```
Writing a file by creating it (if the file is already present and not empty, then it will be overwritten)
```bash
$ cat > file.txt
```
Appending a file
```bash
$ cat >> file.txt
```
Count no_lines, no_words, no_characters and file_name
```bash
$ wc file.txt
```
Count no_lines
```bash
$ wc -l file.txt
```
Count no_of_items in a directory
```bash
$ ls | wc -l
```
Sorting file content alphabetically
```bash
$ sort file.txt
```
Sorting file content reverse alphabetically
```bash
$ sort -r file.txt
```
Sorting file content numerically
```bash
$ sort -n file.txt
```
Sorting file content reverse numerically
```bash
$ sort -rn file.txt
```
Sort column 2 alphabetically
```bash
$ sort -k2 file.txt
```
Sort column 2 numerically
```bash
$ sort -k 2n file.txt
```
Sort column 2 in reverse numerical order
```bash
$ sort -k 2rn file.txt
```
View column 2 & 3 of a file
```bash
$ cut -f2,3 file.txt
```
View column 2 & 3 of a space seperated file
```bash
$ cut -d " " -f2,3 file.txt
           or
$ cut -d " " -f2-3 file.txt
```
Sorting unique content of the file
```bash
$ sort -u file.txt
```
Unique contents of each cluster as per the data in a file
```bash
$ uniq file.txt
```
Remove everything from the current directory
```bash
$ rm * 
```
Compress file (file.txt)
```bash
$ gzip file.txt
```
Uncompress the gzip file
```bash
$ gunzip file.txt.gz
```
Archieve all the files in Folder.tar
```bash
$ tar -cvf Folder.tar file1 file2 file3
```
Compress the archieve
```bash
$ gzip Folder.tar
```
Listing all the files and folder in archieve without extracting it
```bash
$ tar -xvf Folder.tar
```
Add extension to all the files in a folder
```
$ rename "s/$/.txt/g" *
```

Add file_name to the first column of a file (file_name.txt)

>Before

1	3          
4	8          
8	0          
10	77         

>After

file_name	1	3          
file_name	4	8          
file_name	8	0          
file_name	10	77         

```
$ awk '{print FILENAME"\t"$0}' file_name.txt | sed "s/.txt//g"
```

Replace two columns together

>Before

1	3          
4	8          
8	0          
10	77         

>After

3	1          
8	4          
0	8          
77	10         
```
$ awk '{print $2"\t"$1}' file.txt
```
Merge the content of two columns to make a single column
>Before

1	3          
4	8          
8	0          
10	77         

>After

13         
48         
80         
1077             

```
$ awk '{print $1$2}' file.txt
```

Remove duplicate lines after first occurrence

```$ awk '! a[$0]++' file_name.txt```

**Linux command to get the amino acids count**
```bash
$ cat fasta_file | grep -v ">" | grep -o "[ACDEFGHIKLMNOPQRSTUVWY]" | sort | uniq -c
```

**Linux command to get the base count**
```bash
$ cat fasta_file | grep -v ">" | grep -o "[ATGC]" | sort | uniq -c
```
**Linux command to get complementary DNA sequence**
```bash
$ cat fasta_file | grep -v ">" | tr ATGC TACG
```
**Linux command to get reverse complementary DNA sequence**
```bash
$ cat fasta_file | grep -v ">" | rev | tr ATGC TACG
```
**Linux command to get mRNA sequence**
```bash
$ cat fasta_file | grep -v ">" | tr ATGC AUGC
```
