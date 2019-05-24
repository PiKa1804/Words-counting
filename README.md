# words-counting

Web application in Flask, Python (with Bootstrap, JQuery and DataTables).

Getting URL address and searching website for keywords in metadata.

Simple algorithm:
1) Writting URL address like www.gs24.pl (without http/s protocol).
2) Checking URL's robot.txt (can/shouldn't scrape website).
3) Adding protocol.
4) Searching for keywords.
5) Reading all text on main site.
6) Comparing keywords with text (can develope that with regex in the future).
7) Counting frequency.
8) Showing results.

Example websites:
1) www.gs24.pl - lots of keywords
2) www.tauron.pl - one keyword
3) www.cda.pl - no keywords
4) www.pracuj.pl - shouldn't scrape this website
5) www.pl.pl - can't connect, website doesn't exsist



