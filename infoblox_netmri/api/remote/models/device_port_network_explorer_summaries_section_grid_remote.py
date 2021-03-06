from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePortNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """
    

    
    |  ``id:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceID:`` none
    |  ``attribute type:`` string
    
    |  ``PortProtocol:`` none
    |  ``attribute type:`` string
    
    |  ``Port:`` none
    |  ``attribute type:`` string
    
    |  ``ExpectedService:`` none
    |  ``attribute type:`` string
    
    |  ``port_count:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("id",
                  "DeviceID",
                  "PortProtocol",
                  "Port",
                  "ExpectedService",
                  "port_count",
                  )

    
    
    
    
    
    
    