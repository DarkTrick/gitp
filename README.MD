What is this?
=============
gitp (=git power) is a command line tool with the objective to improve user experience of git.

Concrete example: "How do I delete a remote branch?"

**git**
```
git push origin --delete
```

**gitp**
```
git branch delete remote
```


Background
==========
Sometimes git feels like perl: whatever you want to do, you need a google search and the result is so hard to remember, that you need to check it everytime you want to run it.

Internet: "Idiot! Just use git alias!".

Well, feel free to ignore this project.
In general the problem with git alias is, that
1) you first need to know the actual correct git command (and the existence of git alias) in order to set it up.
2) your aliases are different to your peer's aliases. So you cannot share commands. Gitp will provide a more standardized way for aliases.


Dependencies
============

- `git` must be installed
