# README #

## About ##

This is the frontend to the extremely alpha BsBang project indexing Bioschemas (http://bioschemas.org) indexing project.

The main site running this frontend is at http://bsbang.science

## Install ##
1. Copy bsbang.cfg.example to bsbang.cfg and change SECRET_KEY to your secret key and point SOLR_URL to your Solr install
2. Execute python3 app.py

To install in Apache2
1. Install the Python3 mod_wsgi module (package libapache2-mod-wsgi-py3 in Debian/Ubuntu)
2. Configure Apache2 with install/apache2/bsbang.conf
3. Create /var/www/bsbang
4. Copy install/apache2/bsbang.wsgi to /var/www/bsbang, editing sys.path.insert() to point to your bsbang installation location

## Contact ##
Brought to you by the Micklem Lab at Cambridge University in the UK (http://www.micklemlab.org/)

Comments/suggestions please send to justincc AT intermine.org or tweet me (@justincc).
