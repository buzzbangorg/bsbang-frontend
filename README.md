# README #

## About ##

This is the frontend to the alpha Buzzbang project indexing [Bioschemas](http://bioschemas.org) markup. Please see https://github.com/buzzbangorg/buzzbang-doc/wiki for more information.

The main site running this frontend is at http://buzzbang.science
The recent developments have not been pushed to the domain yet. pleasefollwo the instructions to install and run the latest version in your local machine.

## Install ##

These instructions are for Linux. There are no plans to support Windows at this time.

* Copy bsbang.cfg.example to bsbang.cfg and change `SECRET_KEY` to your Flask secret key
 (see http://flask.pocoo.org/docs/0.12/quickstart/#sessions) and point `SOLR_URL` to your Solr install

Then, to run locally:
1. Execute `python3 app.py`

Or to run in Apache2:
1. Install the Python3 mod_wsgi module (package `libapache2-mod-wsgi-py3` in Debian/Ubuntu)
2. Configure Apache2 with `install/apache2/bsbang.conf`
3. Create `/var/www/bsbang`
4. Copy `install/apache2/bsbang.wsgi` to `/var/www/bsbang`, editing `sys.path.insert()` to point to the root of your
bsbang installation.

## MindMap ##

- [x] Load 10 results at a time and leave to remaining for further requests
- [x] Include previous and next button on the result page/Pagination
- [x] Integrate the spell-check module
- [ ] Update the aboutme page of the website
- [ ] Implement the suggester module to provide suggestion as you type
- [ ] Show 2 page numbers before and after the current page in the page navgation bar
- [ ] When displaying results, do boxout information that is useful to the user, in a similiar style to Google info-boxes(e.g. how many datasets a data catalog has, the information on the hosting biobank for a particular found biological sample.  This will require significant improvements to the scope of the corresponding crawler and how it stores crawled
 structured data.
- [ ] Allow users to register URLs for crawling via the website. To do this, the crawler will also need filtering and limiting control to prevent crashes from malicious, malformed or simply huge crawl targets.


## contributing ##

Contributions welcome!  Please

* Conform to the PEP 8 style guide.

Thanks!
