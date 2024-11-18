export interface Bookmark {
  id: string;
  type: "twitter" | "youtube";
  title: string;
  description?: string;
  imageUrl?: string;
  url: string;
  createdAt: string;
  content: any;
}

export interface BookmarkAction {
  id: string;
  action: "like" | "discard";
  timestamp: string;
}
