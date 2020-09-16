import React from 'react';
import { StyleSheet } from 'react-native';
import { Layout, Text} from '@ui-kitten/components';

const styles = StyleSheet.create({
  container: {
    flex: 1, 
    justifyContent: 'center', 
    alignItems: 'center'
  }
})

const Home = () => {
  return (
    <Layout style={styles.container}>
      <Text category='h1'>HOME</Text>
    </Layout>
  );
};

export default Home;
