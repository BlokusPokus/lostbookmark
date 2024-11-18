import React from "react";
import { Bookmark } from "../../types/bookmark";

interface BookmarkCardProps {
  bookmark: Bookmark;
  onLike: (id: string) => void;
  onDiscard: (id: string) => void;
}

const BookmarkCard: React.FC<BookmarkCardProps> = ({
  bookmark,
  onLike,
  onDiscard,
}) => {
  return (
    <div className="bookmark-card">
      {bookmark.imageUrl && (
        <img
          src={bookmark.imageUrl}
          alt={bookmark.title}
          className="bookmark-image"
        />
      )}
      <div className="bookmark-content">
        <h3>{bookmark.title}</h3>
        {bookmark.description && <p>{bookmark.description}</p>}
      </div>
      <div className="bookmark-actions">
        <button onClick={() => onDiscard(bookmark.id)}>Discard</button>
        <button onClick={() => onLike(bookmark.id)}>Like</button>
      </div>
    </div>
  );
};

export default BookmarkCard;
