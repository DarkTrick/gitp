# FAQ

*Question:*
Why do I need the nested `gitp` folder? Can't the structure be easier?

*Answer:*
No. Every folder within `src/gitp/` will be *installed* in `lib/python3.10/site-packages`. If you don't use the nesting, you'll end up with several folders in `site-packages`, and non-functioning python imports.

Why? Because (Ooops) the python environment sucks (again).