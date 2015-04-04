# Roadmap

## Improvements

* end2end tests (selenium-python?)
* parametrization (place, date...)
* containerization and developers installation guide


### Server

* move to python 3.4+
* performance test for APIs (<5s)
* dependencies upgrade

Design choice:
* rewrite smaller and more scalable APIs
* cache (asyncronous caching with Celery?)


### Client

* rewrite with Angular2, new router
* builder/dev scripts (Makefile, Gulp..)
* dependencies upgrade

Known bugs:
* title link (doesn't move tabs selection accordingly)
* login form


## New features

* i18n support + Italian translation
* Android app (Ionic?)
* exporting data in .ods format (TBD)
* add filters and different ways of ordering in some views (TBD)
