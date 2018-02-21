# README #

## About ##

This is the frontend to the extremely alpha Buzzbang project indexing Bioschemas (http://bioschemas.org) indexing project.

It currently only crawls DataCatalog and PhysicalEntity (soon to be renamed to BioChemEntity) JSON-LD found at pre-registered
URLs, either webpages or sitemap.xml. 

The main site running this frontend is at http://buzzbang.science

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

## TODO ##
Future plans include:

* Greatly improve the basic look for the website (logo and style)
* When displaying results, do boxout information that is useful to the user, in a similiar style to Google info-boxes
 (e.g. how many datasets a data catalog has, the information on the hosting biobank for a particular found biological sample.
 This will require significant improvements to the scope of the corresponding crawler and how it stores crawled
 structured data.
* Allow users to register URLs for crawling via the website. To do this, the crawler will also need filtering and 
limiting control to prevent crashes from malicious, malformed or simply huge crawl targets.


## Hacking ##

Contributions welcome!  Please

* Conform to the PEP 8 style guide.

Thanks!

