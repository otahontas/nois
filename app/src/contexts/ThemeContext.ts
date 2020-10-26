import React from "react";

export enum Theme {
  Dark = "dark",
  Light = "light",
}

export type ThemeContextType = {
  theme: Theme;
  toggleTheme: (Theme: Theme) => void;
};

const ThemeContext = React.createContext<ThemeContextType>({
  theme: Theme.Dark,
  toggleTheme: theme => console.log(`Theme not provided, current theme is ${theme}`),
});

export default ThemeContext;
