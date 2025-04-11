# PiHole Configuration Files

## Introduction
This 


sqlite3 is installed on the system for directly accessing the database.
To access gravity.db for manual edits:

```
cd /opt/docker/pihole/etc-pihole
sqlite3 ./gravitydb
```

`.tables` - to list tables:
`.schema <tablename>` to show the table schema

**domainlist** contains the manual entries for blacklist/whitelist, which are listed under "Domains" in the WebUI.
* type: Exact Allow = 0
* type: Exact Deny = 1

**adlist** contains the URLs for all of the adlists the gravitydb will be updated using, both whitelists and blacklists.
Note: the type value is backwards to the domainlist:
* type: Exact Allow = 1
* type: Exact Deny = 0

* CTRL+D to quit the sqlite3 client

## Notes

Took out the following, as the blacklist is included in the base pihole docker image:
"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts","Steven Black Blocklist"