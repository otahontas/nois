import React from 'react';
import * as eva from '@eva-design/eva';
import { SafeAreaView,  StyleSheet, Platform, StatusBar } from 'react-native';
import { ApplicationProvider, IconRegistry } from '@ui-kitten/components';
import { default as themeColors } from './theme.json';
import { EvaIconsPack } from '@ui-kitten/eva-icons';
import Home from "./src/screens/Home";
import AuthStorage from './src/utils/authStorage';
import AuthStorageContext from './src/contexts/AuthStorageContext';
import ThemeContext from './src/contexts/ThemeContext';
import useTheme from './src/hooks/useTheme';

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "white",
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0
  },
});

const authStorage = new AuthStorage();

const App: React.FC = () => {
  const { theme, toggleTheme } = useTheme();

  // TODO: Set applicationProvider to use theme later
  return (
  <>
    <IconRegistry icons={EvaIconsPack} />
    <AuthStorageContext.Provider value={authStorage}>
      <ThemeContext.Provider value={{ theme, toggleTheme }}>
        <ApplicationProvider {...eva} theme={{...eva.dark, ...themeColors}}>
          <SafeAreaView style={styles.safeArea}>
            <Home />
          </SafeAreaView>
        </ApplicationProvider>
      </ThemeContext.Provider>
    </AuthStorageContext.Provider>
  </>
);
}

export default App;
