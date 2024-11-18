import React from "react";
import { Bookmark } from "../../types/bookmark";
import BookmarkCard from "./BookmarkCard";

interface SwipeableViewProps {
  bookmarks: Bookmark[];
  onSwipe: (bookmarkId: string, direction: "left" | "right") => void;
}

const SwipeableView: React.FC<SwipeableViewProps> = ({
  bookmarks,
  onSwipe,
}) => {
  const handleLike = (id: string) => {
    onSwipe(id, "right");
  };

  const handleDiscard = (id: string) => {
    onSwipe(id, "left");
  };

  return (
    <div className="swipeable-container">
      {bookmarks.map((bookmark) => (
        <BookmarkCard
          key={bookmark.id}
          bookmark={bookmark}
          onLike={handleLike}
          onDiscard={handleDiscard}
        />
      ))}
    </div>
  );
};

export default SwipeableView;
