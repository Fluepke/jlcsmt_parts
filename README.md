# JLCSMT parts library

This repository contains a script `fetch_parts.py` to fetch all parts that [JLC SMT](https://jlcpcb.com/smt-assembly) offers.

Usage: `fetch_parts.py [keyword]`
Use `fetch_parts.py ''` to fetch all the parts.
Progress is print to **stderr**.

Use `| jq 'map(select(.componentLibraryType == "base"))'` to filter for the basic parts.

`jlcsmt_parts.json` contains (probably) all the parts. **Count: 32860**
`jlcsmt_basic_parts.json` contains (probably) all the basic parts. **Count: 672** 
