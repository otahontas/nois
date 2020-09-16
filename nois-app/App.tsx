import React from 'react';
import * as eva from '@eva-design/eva';
import { SafeAreaView,  StyleSheet, Platform, StatusBar } from 'react-native';
import { ApplicationProvider, IconRegistry } from '@ui-kitten/components';
import { default as theme } from './theme.json';
import { EvaIconsPack } from '@ui-kitten/eva-icons';
import Home from "./src/components/Home";

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "white",
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0
  },
});

const App = () => (
  <>
    <IconRegistry icons={EvaIconsPack} />
    <ApplicationProvider {...eva} theme={{...eva.dark, ...theme}}>
        <SafeAreaView style={styles.safeArea}>
          <Home />
        </SafeAreaView>
    </ApplicationProvider>
  </>
);

export default App;
