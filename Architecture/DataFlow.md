graph TD
%% External Entities
User[User] -->|Requests to Delete Multiple Bookmarks| Auth[Authentication]
XAPI[X API] -->|Provides Bookmarks| FetchData[Data Fetching]
YTAPI[YouTube API] -->|Provides Saved Videos| FetchData

    %% Processes
    Auth -->|Returns Token| UserStore[User Data Store]
    FetchData -->|Fetch Bookmarks & Videos| CleanData[Data Cleaning]
    CleanData -->|Cleans Data| ContentStore[Content Data Store]
    UserStore -->|User Preferences & Tokens| FetchData

    %% User Interactions
    User -->|Likes/Discards| CleanData
    User -->|Adds to Bookmark/Playlist| ContentStore
    User -->|Creates New Bookmark/Playlist| ContentStore
    User -->|Deletes Multiple Bookmarks| ContentStore

    %% Backend Deletion Handling
    ContentStore -->|Batch Request for Deletion| BatchDelete[Batch Deletion Process]
    BatchDelete -.->|Bulk Delete Request| XAPI
    BatchDelete -->|Handles Rate Limiting| RetryLogic[Retry Logic for Deletion]
    RetryLogic -->|Wait for Rate Limit Reset| BatchDelete
    BatchDelete -->|Delete from Content Data Store| ContentStore

    %% Data Flows
    ContentStore -->|Displays Data| User

    %% Data Deletion Flow
    CleanData -.->|Delete Data| ContentStore
    ContentStore -.->|Delete Discarded Items| ContentStore
