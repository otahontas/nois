import React from "react";

const ThemeContext = React.createContext({
  theme: "light",
  toggleTheme: () => null,
});

export default ThemeContext;
