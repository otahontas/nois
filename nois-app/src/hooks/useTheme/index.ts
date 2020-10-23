import { useState } from "react";

import { Theme } from "../../contexts/ThemeContext";

const useTheme = () => {
  const [theme, setTheme] = useState(Theme.Dark);

  const toggleTheme = () => {
    const nextTheme = theme === Theme.Light ? Theme.Dark : Theme.Light;
    setTheme(nextTheme);
  };

  return { theme, toggleTheme };
};

export default useTheme;
