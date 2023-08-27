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
2. [Python - markdown convert](https://segmentfault.com/q/1010000043277064)


- Python Download from URL

1. [Python - Download IMAGE from URL by requests](https://blog.51cto.com/u_16099185/6385805)
2. [Python - Download image from URL](https://ithelp.ithome.com.tw/articles/10211545)
3. [Python - Download images from URL 2](https://tw.from-locals.com/python-download-web-images/)
4. [Python - file operation - about path](https://medium.com/seaniap/python-%E4%BD%BF%E7%94%A8%E6%AA%94%E6%A1%88%E7%B3%BB%E7%B5%B1-eaecbe7001dd)
5. [Python - Download image](https://www.geeksforgeeks.org/how-to-download-an-image-from-a-url-in-python/)
6. [Python - Download Image from URL and save it](https://www.jianshu.com/p/938763947de3)

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
5. [Fix - Bad Descriptor Error](https://developer.aliyun.com/article/401335)



## Information 

- Programming Language: Python
- Author: Leo

