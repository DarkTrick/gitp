Generic Command parser

# How to use
parse(


# Development

## Design decisions

- Why not let DictTreeFinder search for "--help" or
  "--explain", ...?
  - Because these commands usually contain more semantic
    than simply showing a text.
    Generally iterating over the node or subnodes