import React from "react";
const LoginPage: React.FC = () => {
  const handleTwitterLogin = async () => {
    const oauth2_url =
      `https://twitter.com/i/oauth2/authorize?` +
      `response_type=code` +
      `&client_id=${TWITTER_CLIENT_ID}` +
      `&redirect_uri=${TWITTER_REDIRECT_URI}` +
      `&scope=tweet.read users.read bookmark.read` +
      `&state=state` +
      `&code_challenge=challenge` +
      `&code_challenge_method=plain`;

    window.location.href = oauth2_url;
  };

  const handleYouTubeLogin = async () => {
    // Implement YouTube OAuth login
  };

  return (
    <div className="login-container">
      <h1>Lost Bookmark</h1>
      <div className="login-buttons">
        <button onClick={handleTwitterLogin}>Connect to X</button>
        <button onClick={handleYouTubeLogin}>Connect to YouTube</button>
      </div>
    </div>
  );
};

export default LoginPage;
