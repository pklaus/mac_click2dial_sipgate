# clean the directory from unneeded files

all: dist/SipgateClickTodial.bundle

dist/SipgateClickTodial.bundle:
	python2.6 setup.py py2app

install: dist/SipgateClickTodial.bundle
	@-rm -rf ~/Library/Address\ Book\ Plug-Ins/SipgateClickTodial.bundle
	@mv dist/SipgateClickTodial.bundle ~/Library/Address\ Book\ Plug-Ins/
	@echo 'Moved "dist/SipgateClickTodial.bundle" to "~/Library/Address Book Plug-Ins/".'
	@echo "Please copy the sample configuration file to ~/.clicktodial.conf and adjust to your settings."

.PHONY : clean
clean :
	@-rm -rf *~ build dist *.pyc
