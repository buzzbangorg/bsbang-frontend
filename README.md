# README #

## About ##

This is the frontend to the extremely alpha Buzzbang project indexing Bioschemas (http://bioschemas.org) indexing project.

It currently only crawls DataCatalog and PhysicalEntity (soon to be renamed to BioChemEntity) JSON-LD found at pre-registered
URLs, either webpages or sitemap.xml. 

The main site running this frontend is at http://buzzbang.science

## Install ##

These instructions are for Linux.  No plans to support Windows at this time.

1. Copy bsbang.cfg.example to bsbang.cfg and change SECRET_KEY to your secret key and point SOLR_URL to your Solr install
2. Execute python3 app.py

To install in Apache2
1. Install the Python3 mod_wsgi module (package libapache2-mod-wsgi-py3 in Debian/Ubuntu)
2. Configure Apache2 with install/apache2/bsbang.conf
3. Create /var/www/bsbang
4. Copy install/apache2/bsbang.wsgi to /var/www/bsbang, editing sys.path.insert() to point to your bsbang installation location

## TODO ##
Future plans include:

* Make crawler periodically re-crawl.
* Understand much more structure (e.g. DataSet elements within DataCatalog).
* Parse other Bioschemas and schema.org types used by life sciences websites (e.g. Organization, Service, Product)
* Allow users to register URLs for crawling via the website.
* Add mongodb for capturing crawled JSON-LD (currently I only have Solr but need something else as a general docstore).
* Crawl and understand PhysicalEntity/BioChemEntity/ResearchEntity once this matures further.

Any other suggestions welcome as Github issues for discussion or as pull requests.

## Contact ##
Brought to you by the Micklem Lab at Cambridge University in the UK (http://www.micklemlab.org/), with funding from the
BBSRC (http://www.bbsrc.ac.uk/)

Comments/suggestions please send to justincc AT intermine.org or tweet me (@justincc).
