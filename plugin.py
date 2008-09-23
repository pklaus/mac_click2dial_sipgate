#! /usr/bin/evn python
"""
Apple Address Book Plugin for sipgate click to dial function

author: Marcel Lauhoff <mlirq0.org>

"""

from AddressBook import *
from AppKit import *


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

        
        
        # testing ... 
        pboard = NSPasteboard.generalPasteboard()
        pboard.declareTypes_owner_([NSStringPboardType], None)
        pboard.setString_forType_(use_phone, NSStringPboardType)

