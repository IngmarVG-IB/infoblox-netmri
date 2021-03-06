from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class NotificationSentGridRemote(RemoteModel):
    """
    

    
    |  ``NotificationID:`` none
    |  ``attribute type:`` string
    
    |  ``Destination:`` none
    |  ``attribute type:`` string
    
    |  ``Timestamp:`` none
    |  ``attribute type:`` string
    
    |  ``Method:`` none
    |  ``attribute type:`` string
    
    |  ``Category:`` none
    |  ``attribute type:`` string
    
    |  ``Type:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("NotificationID",
                  "Destination",
                  "Timestamp",
                  "Method",
                  "Category",
                  "Type",
                  )

    
    
    
    
    
    
    