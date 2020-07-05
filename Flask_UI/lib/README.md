# **Design Document**

## This is a description of the UML document that outlines the classes needed to complete the project. Reference the EigenFace.pdf file for the graphical depiction of this description.

## **Backend**

The backend consists of a database (either SQLite3 or MySQL) and a python class **DataConnector** that provides a simplified interface to pushing and pulling data from the datastore.

## **Middleware / Functionality**

The meat of the functionality is contained in a few classes. These are **FaceTester**, **StreamController**, and the most important class **FaceSpace**.

### **FaceTester class**

This class will maintain an array of faces and a connection to the database. The functions provided will do a few things.

1. It will test images to determine if there is actually a face present; this is important because the current face scanning algorithm scrapes parts of the image that are not faces.
2. It will need to 'orient' the face images so that the features generally occupy the same place in the image.
3. It will convert images to greyscale.
4. It will turn the image into a vector to prepare it to be passed to the FaceSpace class.
5. It will send newly identified faces to the database.

### **FaceSpace Class**

This class will host the most important part of the "functionality" of the program.

It will keep a variable representing the SVD/PCA of the *FaceSpace*

It will keep a variable of vectors; each vector representing the *average* of a certain character (i.e. average Jim, average Pam, etc...the sum total of the character's face, divided by the number of images used to construct the sum).

1. It will be able to Create the representation of the FaceSpace
2. It will be able to project vectors onto the FaceSpace matrix/SVD/PCA
3. It will be able to calculate the Euclidean distance of a given vector to the other vectors in FaceSpace.
4. It will be able to determine which *average* face vector it is closest to in order to "ID" a face.
5. It will be able to return a face identity to the **FaceTester** class.

### **StreamController Class**

This class will maintain an array of face IDs that have been seen on screen along with a timestamp for when the were seen.

It will maintain a set of variables that will control when and how the video stream is displayed (**displayStream**, **muteStream**, **dimStream**, and **adjustVolume**)

1. It will be able to push a recognized face to the array of face IDs.
2. It will send a control message to the front end consisting of the control variables the class hosts.
3. It will be able to calculate a *probability* that a commercial is being shown. This will be used to determine how the control variables are set.

## **Front End**

This refers to the webpage and interactive capabilities provided by the application.

It is able to pass data to the **StreamController** class.