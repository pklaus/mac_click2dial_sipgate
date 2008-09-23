#! /usr/bin/evn python
# -*- coding: utf-8 -*-

"""
Apple Address Book Plugin for sipgate click to dial function

author: Marcel Lauhoff <ml@irq0.org>

"""

from AddressBook import *
from AppKit import *

from sipgate import *

class SipgateClickToDial(NSObject):
    def actionProperty(self):
        return kABPhoneProperty

    def titleForPerson_identifier_(self, person, identifier):
        return u"Dial (Sipgate Click2Dial)"
    
    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return len(person.phone()) > 0

    def performActionForPerson_identifier_(self, person, identifier):
        phones = person.valueForProperty_(kABPhoneProperty)
        use_phone = phones.valueForIdentifier_(identifier)

        s = SimpleSipgateApi("serious","callthepower")
        s.call("sip:8725569@sipgate.de", makeSipUri(use_phone)) 
        
#         # testing ... 
#         pboard = NSPasteboard.generalPasteboard()
#         pboard.declareTypes_owner_([NSStringPboardType], None)
#         pboard.setString_forType_(use_phone , NSStringPboardType)

