class stream_controller:
    
    """
    This class provides the connection to the front-end of the project, serving 
    control what the user will see given events that take place in the video stream.

    Attributes:
        face_ID_Array[_ID, _timeStamp]:     array of tuples [(faceIDs, time}] recently seen on screen with their timestamp
        displayStream:                      boolean to control whether the 'raw' stream is shown or not
        muteStream:                         boolean to mute the userStream
        dimStream:                          double that will change the display brightness during commercial breaks
        adjustVolume:                       double that will adjust the volume during commercial breaks

    Methods:
        pushFaceID(_ID, _timeStamp):        adds a character to the list of characters recently seen
        sendControlMessage(message):        sends a tuple containing the control variables to be activated
        commercialProbability():            calculates the probability that the stream is currently a commercial
    """

    def __init__(self):
        """
        Initialization of StreamController object
        """

    def push_face_id(self, _ID, _timeStamp):
        """
        Pushes a tuple containing the face_ID of a character and the timestamp it was seen

            Parameters:
                _ID (int):          integer representing the character ID
                _timestamp(int):    integer representing what time the character was seen

            Returns:
                none
        """

    def send_control_message(self, message):
        """
        This function will send a control message to the front end so the display the user sees can be 
        adjusted according to their desires and what happens on the screen.

            Parameters:
                message(Dictionary):    dictionary containing the instance variables of the class relating to video control

            Returns:
                None
        """

    def commercial_probability(self):
        """
        Uses methodology to calculate the probability that a commercial is being shown on the screen.

            Parameters:
                None, but has access to the array of characters (and other _IDs) that are on screen and their timestamps

            Returns:
                prob (double):      double representing the probability that the stream is hosting a commercial
        """

if __name__ == "__main__":
    stream_controller = stream_controller()