
""" File:           defines.py
    Author:         sree/iiaballoongroup
    Last change:    2015/03/30

    Python Interface for OceanOptics Spectometer 
    Some definition stuff...
"""

#----------------------------------------------------------

class OceanOpticsError(Exception):
    pass

MAYA2000PRO_TRIGGER_MODES = {
        'normal' : 0,
        'external_HW_lvl' : 1,
        'external_sync' : 2,
        'external_HW_edge' : 3 
        }


