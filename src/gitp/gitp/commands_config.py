"""
  File structure
  ==============

  No entry must start with `--`

  __cmd:
      Type: array
      Specifies the commands to be run.

  __description:
      Type: array
      Explanation shown for the command when --help was run.

  __cmddescription:
      Type: array
      Explanation of how the command works. This is shown,
      when the user shows the command of a command.
  __constraints:
      Type: Array
      Set contraints for a command. E.g. branches the command will
      not work on
      Constraints:
        - `disabled for: $branchname`
          - Will not allow the command to run for the branch $branchname.

  __approve:
      Type: object
      Spawns a question asked the user prior to run the command.

      _msg:
        Type: Array
        Text shown on screen
      _actions
        Type: Array of key-value pairs:
        key: possible answer to type in
            Empty key = empty input / unknown input
        value: command to be executed.
            `_run` = run the command.
            `_abort` = abort the execution of the command immediately.


  Command line parameters: ${1}, ${2}, ....
  Special parameters:
    - ${currentbranch}
      - denotes the current branch you're working on
    - ${remotebranch}
      - denotes the remote branch of the branch you're working on
"""

commandDB = {
  "branch": {
    "checkout": {
      "remote": {
        "${1}": {
          "__cmd": ["git fetch ${1}",
                  "git checkout ${1}"],
          "__description": ["Checkout a branch from remote repository"],
          "__cmddescription": [""],
        },
      },
    },
    "create": {
      "${1}": {
        "__cmd": ["git checkout -b ${1}"],
        "__description": ["Create a new branch and switch to it"]
      }
    },
    "connect": {
      # TODO: add support for this
      #"__cmd": ["git branch --set-upstream-to=origin/${currentbranch}"],
      #"__description": ["Connect current branch with remote branch with the same name"],
      "to": {
        "${1}":{
          "__cmd": ["git branch --set-upstream-to=origin/${1}"],
          "__description": ["Connect current branch with remote branch with the same name"]
        },
      }
    },
    "rename": {
      "${1}":
      {
        "__cmd": ["git branch -m ${1}"],
        "__description": ["Renames the current branch to ${1}"],
      }
    },
    "reset": {
      "to":{
        "remote":{
          "${1}": {
            "__cmd": ["git fetch origin",
                      "git checkout ${1}",
                      "git reset --hard origin/${1}",
                      "git branch",
                      ],
            "__cmddescription": ["At the end, just show all branches"],
            "__description": ["Reset local changes to the remote state",
                              "Ignore untracked files",
                              "Ignore gitignore files"],
            }
        }
        # TODO: add support for ${currentbranch}
          #{
          #"__cmd": ["git fetch origin",
          #          "git checkout ${currentbranch}",
          #          "git reset --hard origin/${currentbranch}",
          #          "git branch",
          #          ],
          #"__cmddescription": ["At the end, just show all branches"],
          #"__description": ["Reset local changes to the remote state",
          #                  "Ignore untracked files",
          #                  "Ignore gitignore files"],
          #}
        },
      },
    "delete":{
      "remote":{
        "${1}": {
          "__description": ["Deletes remote branch"],
          # Automatically show "sorry, I will not run this command for ${branch}.
          # Please do it manually: ${__cmd}
          # TODO: not working, yet
          "__constraints": [
                            "disabled for: master",
                            "disabled for: develop",
                            "disabled for: release",
                            ],
          # TODO: not working, yet
          "__approve": {"_msg":[
                            "DANGER ZONE",
                            "===========",
                            "Delete the following ***remote branch(`origin`):",
                            "      ${remotebranch}",
                            "Are you sure to delete? (yes/no): ",
                          ],
                          "_actions": [
                            {"yes": "_run"},
                            {"no": "_abort"},
                            {"": "_abort "}
                          ]
                        },
          "__cmd": ["git push origin --delete ${1}"],
        }
      },
    },
  },
  "branches": {
    "show": {
      "remote": {
        "__cmd": ["git branch -r"]
      },
      "local": {
        "__cmd": ["git branch -l"]
      },
      "all": {
        "__cmd": ["git branch -a"]
      }
    },
  },
  "commit": {
    "delete": {
      "last": {
        "__cmd": ["git reset --hard HEAD~1"],
        "__cmddescription": ["`HEAD~1` will delete the last 'one' commit.",
                           "`hard` will delete all changes"],
        "__description": ["Delete last commit and discard all changes"]
      }
    },
    "undo": {
      "last": {
        "__cmd": ["git reset HEAD~1"],
        "__cmddescription": ["`HEAD~1` will remove the last 'one' commit from history.",
                           "No other option given <=> keep the changes"],
        "__description": ["Undo last commit but keep the changes"]
      }
    }
  }
}
