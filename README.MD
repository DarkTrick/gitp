# What is this?
gitp is a command line tool aiming to simplify the git interface.

Concrete example: "How do I delete a remote branch?"

**git**
```
git push origin --delete
```

**gitp**
```
git branch delete --remote
```

# Background
Sometimes git feels like perl: for whatever you want to do, you need a internet search and the result is so hard to remember that you need to check it everytime you want to run it.

If you cannot relate to this, feel free to ignore this project.

# Dependencies
- Python 3.10
- `git` must be installed

# How to use
## Install
### Install With pip
 `pip install gitp`

### Install From Source
```
cd src
pip install .
```

uninstall from source
`pip uninstall gitp`

## run
`gitp --help`


# Development

## venv
(No external packages are needed so far; so no venv should be necessary)

## Architecture
Commands are implemented in the `commands` subfolder

## Testing
(not maintained, yet)
```
cd src
python3 -m unittest
```


## How gitp works
It uses Python's `subprocess` to run git commands


# Project Character

The following is a list possible abstract goals a software could have, and a rating how much effort is currently put into it.

- Usability: 100%
- Security: 0% (Do not run as root)

