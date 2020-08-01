# **Eigenface Filter (Oh My Py)**

## **Project Link**

[Eigenface Production v 1.0](https://github.com/osulluke/eigenface-production)

## **Description / Purpose**

At a high level, this project's purpose is to be able to compare the image of a face against a *database* of known faces for identification. Specifically, the project is implemented by taking a video stream and "scraping" faces from it, turning them into X x Y images, then into a vector (XY x 1), and then measuring the "distance" between that face and all others in the database. Novel vectors that are outside a certain distance from known faces/vectors (i.e. faces that are in the database) will be classified as not recognized, and vectors that are within the distance will be classified as a certain individual contained within the database.

As individuals are identified as known or unknown, end-user functionality is implemented via an *automatic muting capability* which enhances a user's experience while watching regular television programming in real time.

## **Installation / Usage / Initialization**

First, you will need to clone the respository from GitHub:

```
git clone https://github.com/osulluke/eigenface-production.git
```
This is a public repo, so there should be no issue gaining access.

Once it is cloned, please `cd eigenfaces` in order to access the main project directory and then simply run the following command:
```
./run.sc
```

Based on testing using the **rustysnake** version of Ubuntu, there should be nothing required in the way of `sudo` or extra commands (such as `chmod`) required in order to get the page running.

The entire app will install all required libraries, query our cloud database, build all of the face recognizers, and open our server (which will be locally hosted) to the home page, allowing the user to navigate accordingly.

## **"How to use our program"**

Because watching an entire 30-minute episode of a TV program is unrealistic for our purposes in this class, there are a number of links provided to short clips of the TV show *The Office*, as well as links to commercials which represent commercial breaks. In order to best use the program and see the software in operation, it will be most useful to follow this procedure:

*Update (1 Aug): it is still possible to use the listed steps below, but we thought it better to provide a short clip with embedded commercials - so, selecting the "ShortClip.mp4" link will provide a 'one-stop' shop to see the application operate.*

1. Click on the blue button from the homepage labeled *Play Media*. This will take you to a page that will enable you to play different show clips and different commercial clips.
2. Open a show clip; watch for a short time (about 30-60 seconds).
3. Go "back" to the *Play Media* page and select a commercial clip (appropriately labeled). Watch this clip until it becomes muted to demonstrate the program's capability.
4. Once the program mutes the video stream, go back to *Play Media* and select a different show clip, then watch until the show is un-muted.
5. Repeat the above as required (show - commercial - show - ... ).

During the operation, on the command line, user messages are produced that provide feedback as to who is being identified and whether or not the program is recognizing *Show* or *Commercial*, but the bottom line to the user is whether or not the show is allowed regular volume, and whether annoying commercials are automatically muted.

Stop / close the program by "Ctrl+C" on the Ubuntu command line.

## **Contributions**
**Remee Agbayani:** Front end menu, stylesheet, database, s3 video player, facial recognition import, OpenCV facial recognition to player.

**Moise Jean:** Sellinum player controls, software testing.

**Luke O'Sullivan:** Documentation, app structure/design, eigen implementation, project manager, git master, class creation, program compliation, submissions.

**Zihan Shu:** Presentation, frontend design, frontend video player.

**Xinxin Wu:** OpenCV implementation, video player.
