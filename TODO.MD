
# General
- rewrite help function
- add support for:
  - show help of a specific command (instead of listing it)
    - with --help
    - (impl: Command should also be able to be used for
      returning help information for a specific command
  - "--help" command should also show a small help
- add support for showing the command
- add support for ${currentbranch}
  - careful: until now everything done is none-gitp-specific,
    so before doing this, you HAVE TO divide functionality!


- don't use variables in command tree anymore

- remove "gitp" from code"
- turn into template package
- create project with the package and a config file

# Study
- Search for "TODO!TEST ARCHITECTURE"
  - ... and apply the result

