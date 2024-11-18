import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./components/auth/LoginPage";
import SwipeableView from "./components/bookmarks/SwipeableView";
import Dashboard from "./components/dashboard/Dashboard";
import "./styles/App.css";

const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route
            path="/swipe"
            element={<SwipeableView bookmarks={[]} onSwipe={() => {}} />}
          />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/" element={<LoginPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
