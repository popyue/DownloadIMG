# DownloadIMG
## Prepare 

- Install BeautifulSoup4
```
pip install beautifulsoup4
```

- Install markdown
```
pip install Markdown
```

- Install requests
```
pip install requests
```

## Description

> This code is created for downloading image from hackmd note.
> Before downloading, it is necsssary to set up the the note to view by everyone.

## Reference

- Python Regular Expression
1. [Return String from re](https://stackoverflow.com/questions/38579725/return-string-with-first-match-for-a-regex-handling-case-where-there-is-no-matc)
2. [Python - How to use regular expression](https://docs.python.org/zh-tw/3/howto/regex.html)
3. [Python - Regular Expression cheat sheet](https://www.geeksforgeeks.org/python-regex-cheat-sheet/)
4. [Python - Regular Expression match everything before 1st space](https://juejin.cn/s/regex%20match%20everything%20until%20next%20space)
5. [Regular Expression tutorial](https://medium.com/programming-with-data/2-%E6%AD%A3%E5%89%87%E8%A1%A8%E9%81%94%E5%BC%8F-regular-expression-26b9b9b908c6)
6. [Python - Extract substring by re](https://linuxhint.com/extract-substring-regex-python/)
7. [Python - 20 common usage for re](https://selflearningsuccess.com/pythonstring/)

- Python directory / file operation (creating, editing, storing)
1. [Python - Creating a directory](https://www.geeksforgeeks.org/create-a-directory-in-python/)
2. [Python - Open and read file](https://www.dataquest.io/blog/read-file-python/)

- Python string operation 
1. [Removing newline character from strings](https://www.geeksforgeeks.org/python-removing-newline-character-from-string/)


- Python BeautifulSoup
1. [BeautifulSoup Usage Guidline](https://beautiful-soup-4.readthedocs.io/en/latest/#a-regular-expression)
2. [Find element by class](https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class)
3. [Find element by class 2](https://scrapfly.io/blog/how-to-find-html-elements-by-class-with-beautifulsoup/)
4. [Find element by class 3](https://www.skytowner.com/explore/finding_elements_that_contain_all_the_specified_classes_in_beautiful_soup)


- Python Markdown Convert
1. [Use markdown Lib to convert markdown to HTML](https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-to-convert-markdown-text-to-html)

- Python error handling 
- Description:

> The main reason for the “local variable referenced before assignment” error in Python is using a variable that does not have local scope. 
> This also means referencing a local variable without assigning it a value in a function.

> The variable initialized inside the function will only be accessed inside the function, and these variables are known as local variables. 
> To use variables in the entire program, variables must be initialized globally. 

```
student = 'Mark'
def names():
	student = 'Lily'   <--- Error Part
	print(student)

names()
```

> In the above snippet, the “Student” variable is not marked as global, so when it is accessed inside the function, the Python interpreter returns an error.

> Note: We can access the outer variable inside the function, but when the new value is assigned to a variable, the “UnboundLocalError” appears on the screen.

1. [Fix - local variable 'a' referenced before assignment - 1](https://blog.csdn.net/a1786742005/article/details/88925525)
2. [Fix - local variable 'a' referenced before assignment - 2](https://sabe.io/blog/python-local-variable-referenced-before-assignment#google_vignette)
3. [Fix - local variable 'a' referenced before assignment - 3](https://itslinuxfoss.com/local-variable-referenced-assignment-python/)
4. [Fix - local variable 'a' referenced before assignment - 4](https://www.pythonpool.com/local-variable-referenced-before-assignment/)

## Information 

- Programming Language: Python
- Author: Leo

