from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class StorageMgmtGridRemote(RemoteModel):
    """
    

    
    |  ``id:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceName:`` none
    |  ``attribute type:`` string
    
    |  ``VolumeSize:`` none
    |  ``attribute type:`` string
    
    |  ``StorageCategory:`` none
    |  ``attribute type:`` string
    
    |  ``VolumeGroup:`` none
    |  ``attribute type:`` string
    
    |  ``Locked:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("id",
                  "DeviceName",
                  "VolumeSize",
                  "StorageCategory",
                  "VolumeGroup",
                  "Locked",
                  )

    
    
    
    
    
    
    