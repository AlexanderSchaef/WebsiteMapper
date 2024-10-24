# Website Mapper Project
By Alex Schaefer
## Main Idea:
Given some arbitrary link to a valid webpage, map out every page reachable from that page

## Current TODOs:
- [ ] Write the method for converting from relative to absolute links.
- [ ] Fix known issue of comparison of some link relations that does not recognize some links as already existing in the page
- [ ] Implement the repeating process of continuing into the next valid reachable link.
    - [ ] Figoure how to check if a page link is valid (likely just allow html pages
    - [ ] Stop the program from going past a certain depth
    - [ ] Stop the program from recursing back to pages it has already viewed
