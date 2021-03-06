from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SettingsSnmpMibsGridRemote(RemoteModel):
    """
    

    
    |  ``id:`` none
    |  ``attribute type:`` string
    
    |  ``vendor:`` none
    |  ``attribute type:`` string
    
    |  ``mib:`` none
    |  ``attribute type:`` string
    
    |  ``source:`` none
    |  ``attribute type:`` string
    
    |  ``version:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("id",
                  "vendor",
                  "mib",
                  "source",
                  "version",
                  )

    
    
    
    
    
    