#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
A plugin to call contacts via Sipgate directly from the Mac OS X Address Book
    website: <https://github.com/pklaus/mac_click2dial_sipgate#readme>

Authors:

* Marcel Lauhoff <ml →AT→ irq0.org>
* Philipp Klaus <philipp.klaus →AT→ gmail.com>

"""

from AddressBook import *
from AppKit import *

from ConfigParser import ConfigParser
import os.path
from sys import stderr

### Import the sipgate module from https://github.com/pklaus/python-sipgate-xmlrpc
### The Makefile will fetch it automatically (or you can run `make sipgate.py`):
import sipgate

from datetime import datetime

LOG_FILE=os.path.expanduser('~/.clicktodial.log')
CONF_FILE=os.path.expanduser('~/.clicktodial.conf')
SIPGATE_NET_TEMPLATE='sip:%s@sipgate.net'
DEFAULT_COUNTRY_CODE='49'

class SipgateClickToDial(NSObject):
    def actionProperty(self):
        return kABPhoneProperty

    def titleForPerson_identifier_(self, person, identifier):
        return u"Call via Sipgate"
    
    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return len(person.phone()) > 0

    def performActionForPerson_identifier_(self, person, identifier):
        phones = person.valueForProperty_(kABPhoneProperty)
        remote_number = phones.valueAtIndex_(phones.indexForIdentifier_(identifier))
        c = Caller()
        c.call(remote_number)

class Caller(object):
    """
    We need this Caller calls because we cannot add methods and variables
    to the SipgateClickToDial class as it inherits from NSObject
    and this hides all your added instance variables and methods.
    cf. <http://bit.ly/mUtinW>
    """

    def log(self, what):
        if self.get_log_enabled():
            # we may change logging as shown in <https://github.com/karlp/python-osm/commit/3ed60c5#diff-0>
            log = open(LOG_FILE,'a')
            log.write(datetime.utcnow().isoformat() +' - ' + what+'\n')
            log.close()

    def call(self,remote_number):
        self.log('Calling %s' % remote_number)
        try:
            s = self.get_api()
            self.log('sipgate.api constructed.')
            self.log('LocalUri %s' % self.get_local_uri())
            s.SessionInitiate( { 
                'RemoteUri': SIPGATE_NET_TEMPLATE % sipgate.helpers.FQTN(remote_number, self.get_country_code()),
                'LocalUri': self.get_local_uri(),
                'TOS': 'voice' } )
        ### Error handling:
        except sipgate.SipgateAPIProtocolError, e:
            if e.errcode == 401:
                stderr.write( 'The credentials you provided are incorrect: "%s" (Fault code: %d).\n' %(e.errmsg, e.errcode) )
            else:
                stderr.write( 'A protocol error occured when calling the API: "%s" (Fault code: %d).\n' %(e.errmsg, e.errcode) )
        except sipgate.SipgateAPIFault, e:
            stderr.write( 'A problem with an API call occured: "%s" (Fault code: %d).\n' %(e.faultString, e.faultCode) )
        except sipgate.SipgateAPISocketError, e:
            stderr.write( 'A low level network communication error (socket.error) occured: %s.\n' % e)
        except sipgate.SipgateAPIException, e:
            stderr.write( 'Some other problem accured while communicating with the Sipgate API: %s' % e )
        except Exception as e:
            stderr.write( 'A unpredicted problem of the type %s occured: %s' % (type(e), e) )
        self.log('sipgate.api.SessionInitiate was called.')

    def get_password(self):
        if self.get_conf('password'):
            return self.get_conf('password')
        raise NameError('Your configuration file must contain the value for `password`.')

    def get_log_enabled(self):
        if self.get_conf('logging_enabled'):
            return self.get_conf('logging_enabled').lower() == 'true'
        else:
            return False

    def get_user(self):
        if self.get_conf('user'):
            return self.get_conf('user')
        raise NameError('Your configuration file must contain the value for `user`.')

    def get_local_uri(self):
        if self.get_conf('phone'):
            return self.get_conf('phone')

        try:
            s = self.get_api()
            for own_uri in s.OwnUriListGet()['OwnUriList']:
                if own_uri['DefaultUri']: return own_uri['SipUri']
        except:
            raise NameError('Problem while looking for the default SIP URI.')

    def get_api(self):
        try:
            return self.api
        except:
            self.api = sipgate.api(self.get_user(),self.get_password(),'github.com/pklaus/mac_click2dial_sipgate')
            return self.api

    def get_country_code(self):
        if self.get_conf('cc'):
            return self.get_conf('cc')
        return DEFAULT_COUNTRY_CODE

    def get_conf(self, name):
        try:
            self.conf
        except:
            ## in Python 2.7 one could do:
            #self.conf = ConfigParser(allow_no_value=True)
            self.conf = ConfigParser()
            self.conf.read(CONF_FILE)
        try:
            return self.conf.get('account',name)
        except:
            return None

if __name__ == "__main__":
    c = Caller()
    import sys
    if len(sys.argv) == 1:
        print('To test this module, run it with a phone number as first parameter.')
        sys.exit(2)
    c.call(sys.argv[1])

