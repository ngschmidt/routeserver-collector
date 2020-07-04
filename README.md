# Route Server Collection Methods

## Synopsis

Collect a table of routes from specific devices, and convert to a simple format for comparison, consistency checks, etc.

## Table Format

|Device|Route Table|Network|Type|Nexthop|
|---|---|---|---|---|
|Lab-1  |default    |1.1.1.1/32 |Static |None   |

## To use these examples

Run these python scripts

## Tested Platforms

NX-OS 9.3

### Dependencies

* Python 3.
* Django Core. Required for URL/URI Validation and parsing.

## TODO

* Put into a postgres database or something, historical data is great
* Secretes management
* Use YANG instead of a simple table?

## Authors

* **Nick Schmidt**
