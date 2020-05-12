class Parcel:
    """
    Stores parcel information for single delivery
    Target is a destination Node
    Default package volume for poc is 1, for easier UUID unpacking
    """
    def __init__(self, uuid, target, volume, current_location, geolocation_pickup=None, geolocation_delivery=None, type=None):
        self.volume = volume
        self.target = target
        self.uuid = uuid
        self.current_location = current_location
        self.type = type
        #self.geolocation_pickup = geolocation_pickup
        #self.geolocation_delivery = geolocation_delivery
