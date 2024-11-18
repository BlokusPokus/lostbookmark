import React from "react";
import { Bookmark } from "../../types/bookmark";

const Dashboard: React.FC = () => {
  const [savedBookmarks, setSavedBookmarks] = React.useState<Bookmark[]>([]);

  React.useEffect(() => {
    // Fetch saved bookmarks
  }, []);

  return (
    <div className="dashboard">
      <h2>Your Saved Bookmarks</h2>
      <div className="dashboard-content">{/* Add dashboard content */}</div>
    </div>
  );
};

export default Dashboard;
