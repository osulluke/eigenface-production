from DataConnector import DataConnector
from FaceProcessor import FaceProcessor
from FaceSpace import FaceSpace
from StreamController import StreamController

class EigenScreener:

    """
    This class is a "composition" of other objects that are used to identify faces, control
    database access, control the video stream, and test faces that are found in the stream.

    Attributes:
        vid_stream:         the base video stream a user desires to watch
        data_connection:    A DataConnector() object
        face_processor:     A FaceProcessor() object
        face_space:         A FaceSpace() object
        stream_controller:  A StreamController() object
    """
    
    def __init__(self):
        vid_stream = ""
        data_connection = DataConnector()
        face_processor = FaceProcessor()
        face_space = FaceSpace()
        stream_controller = StreamController()

if __name__ == "__main__":
    eigen_screener = EigenScreener()