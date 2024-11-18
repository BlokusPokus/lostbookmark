graph LR
subgraph Frontend
F1[React App]
end

    subgraph Backend
        B1[Python API Server]
        B2[Background Worker Celery]
        DB[PostgreSQL/MySQL]
        Cache[Redis Cache]
        FolderManager[Folder/Classification Manager]
        Dashboard[Dashboard]
    end

    subgraph External APIs
        XAPI[X API]
        YTAPI[YouTube API]
    end

    subgraph Auth
        OAuth[OAuth 2.0 Provider]
    end

    F1 -..-> B1
    B1 --> DB
    B1 --> Cache
    B1 --> XAPI
    B1 --> YTAPI
    B1 --> OAuth
    B2 --> DB
    B2 --> XAPI
    B2 --> YTAPI
    B1 --> FolderManager
    FolderManager --> DB
    B1 --> Dashboard
    Dashboard --> DB

    F1 --> Dashboard
    FolderManager --> F1

# Frontend

## React App:

Responsible for the user interface.
Handles OAuth flows for X and YouTube.
Implements the swipeable Tinder-like interface.
Sends user actions (e.g., likes/discards) to the backend via APIs.

## Backend

Python API Server (e.g., Flask, Django, or FastAPI):
Serves as the bridge between the frontend and external APIs.
Handles user authentication (e.g., token exchanges for X and YouTube).
Fetches, cleans, and processes data from X and YouTube.
Manages rate limits (e.g., with queuing or caching).
Stores user preferences and data in the database.
Background Worker (e.g., Celery):
Processes queued tasks, such as refreshing data or handling bulk requests.

## Database

Relational Database (e.g., PostgreSQL or MySQL):
Stores user data:
OAuth tokens for X and YouTube (encrypted).
User preferences (liked/discarded content).
Cached bookmarks/videos for faster access.
Cache (e.g., Redis):
Temporarily stores API responses to reduce redundant calls.

## External APIs

X API:
Provides access to user bookmarks.
Enforces rate limits, requiring careful usage and caching.
YouTube API:
Provides access to user’s saved videos.
Enforces its own rate limits.

## Authentication and Authorization

OAuth 2.0:
Used for secure access to X and YouTube APIs.
Handles token exchanges and refreshes.
