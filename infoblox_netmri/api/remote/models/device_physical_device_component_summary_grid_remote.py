from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePhysicalDeviceComponentSummaryGridRemote(RemoteModel):
    """
    

    
    |  ``DevicePhysicalID:`` none
    |  ``attribute type:`` string
    
    |  ``Network:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceID:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceName:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceModel:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceVersion:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalName:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalDescr:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalClass:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalSerialNum:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalModelName:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalHardwareRev:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalFirmwareRev:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalSoftwareRev:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalAlias:`` none
    |  ``attribute type:`` string
    
    |  ``PhysicalAssetID:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("DevicePhysicalID",
                  "Network",
                  "DeviceID",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceName",
                  "DeviceModel",
                  "DeviceVendor",
                  "DeviceVersion",
                  "PhysicalName",
                  "PhysicalDescr",
                  "PhysicalClass",
                  "PhysicalSerialNum",
                  "PhysicalModelName",
                  "PhysicalHardwareRev",
                  "PhysicalFirmwareRev",
                  "PhysicalSoftwareRev",
                  "PhysicalAlias",
                  "PhysicalAssetID",
                  )

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    