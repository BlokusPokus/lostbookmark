sequenceDiagram
participant User
participant Frontend
participant Backend
participant XAPI
participant YouTubeAPI
participant FolderManager
participant Dashboard
participant BackgroundWorker

    User ->> Frontend: Log in / Connect to X and YouTube
    Frontend ->> XAPI: Redirect User for OAuth (X)
    XAPI ->> User: User logs in and approves app
    User ->> XAPI: Grant Authorization
    XAPI ->> Frontend: Redirect with Authorization Code
    Frontend ->> Backend: Send Authorization Code (X)
    Backend ->> XAPI: Exchange Code for Access Token
    XAPI ->> Backend: Access Token (X)

    Frontend ->> YouTubeAPI: Redirect User for OAuth (YouTube)
    YouTubeAPI ->> User: User logs in and approves app
    User ->> YouTubeAPI: Grant Authorization
    YouTubeAPI ->> Frontend: Redirect with Authorization Code
    Frontend ->> Backend: Send Authorization Code (YouTube)
    Backend ->> YouTubeAPI: Exchange Code for Access Token
    YouTubeAPI ->> Backend: Access Token (YouTube)

    User ->> Frontend: Request Bookmarks and Saved Videos
    Frontend ->> Backend: Fetch Bookmarked Posts and Videos
    Backend ->> XAPI: Fetch Bookmarked Posts
    XAPI ->> Backend: Return Posts
    Backend ->> YouTubeAPI: Fetch Watch Later Playlist
    YouTubeAPI ->> Backend: Return Videos
    Backend ->> Backend: Process and Clean Data
    Backend ->> Frontend: Send Processed Data
    Frontend ->> User: Display Tinder-like Interface

    User ->> Frontend: Interacts with Content (Like/Discard)
    Frontend ->> Backend: Save Feedback
    Backend ->> Backend: Store Preferences/History

    User ->> Frontend: Create/Organize Folder or Playlist
    Frontend ->> Backend: Request Folder/Playlist Creation
    Backend ->> FolderManager: Create Folder/Playlist
    FolderManager ->> DB: Save Folder/Playlist Info
    FolderManager ->> Frontend: Confirm Creation

    User ->> Frontend: Open Dashboard
    Frontend ->> Dashboard: Load User Data
    Dashboard ->> Backend: Request User Data
    Backend ->> DB: Fetch Data
    DB ->> Backend: Return Data
    Backend ->> Dashboard: Return Data for Display
    Dashboard ->> Frontend: Display Dashboard

    User ->> Backend: Request Batch Deletion of Bookmarks
    Backend ->> BackgroundWorker: Start Batch Deletion Process
    BackgroundWorker ->> XAPI: Delete Posts
    BackgroundWorker ->> YouTubeAPI: Delete Videos
    BackgroundWorker ->> Backend: Confirm Deletion
    Backend ->> Frontend: Notify User of Successful Deletion
