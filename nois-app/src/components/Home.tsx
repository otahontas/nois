import React, { useState, useEffect } from 'react';
import { Alert, StyleSheet } from 'react-native';
import { Button, Layout, Text, Icon} from '@ui-kitten/components';
import { Audio } from 'expo-av';

const styles = StyleSheet.create({
  container: {
    flex: 1, 
    justifyContent: 'center', 
    alignItems: 'center'
  }
})

const MicIcon = (props) => (
  <Icon {...props} name='mic-outline'/>
);

const StopIcon = (props) => (
  <Icon {...props} name='stop-circle-outline'/>
)


const Home = () => {
  const recordingObject = new Audio.Recording();
  const [recording, setRecording] = useState<boolean>(false);

  const checkAudioPermissions = async () => {
    const audioPermissions = await Audio.getPermissionsAsync();

    if (!audioPermissions.granted) {
      if (!audioPermissions.canAskAgain) {
        Alert.alert(
          "Audio recording not possible",
          "You have denied this app from getting any audio permissions, so recording is not possible",
          [{ text: "OK" }],
          { cancelable: false }
        );
        return false;
      } else {
        const request = await Audio.requestPermissionsAsync()
        if (!request.granted) {
          Alert.alert(
            "Audio recording not possible",
            "Recording messages is not possible if no permissions are granted",
            [{ text: "OK" }],
            { cancelable: false }
          );
          return false;
        } 
        return true;
      };
    }
    return true;
  }



  const startRecording = async () => {
    console.log("starting")
    const permissionsOk = await checkAudioPermissions()
    console.log(permissionsOk)
    if (!permissionsOk) return
      
    try {
      await recordingObject.prepareToRecordAsync(Audio.RECORDING_OPTIONS_PRESET_HIGH_QUALITY);
      await recordingObject.startAsync();
    } catch (error) {
      console.log("error when starting:", error);
    }
    setRecording(true);
    console.log("rec status", recording)
  };

  const stopRecording = async () => {
    console.log("stopping")
    try {
      await recordingObject.stopAndUnloadAsync()
    } catch (error) {
      console.log("error when stopping:", error);

    }
    setRecording(false);
    console.log("rec status", recording)
  }

  return (
    <Layout style={styles.container}>
        <Button size="giant" 
          accessoryLeft={recording ? StopIcon : MicIcon} 
          onPressIn={startRecording}
          onPressOut={stopRecording}
      />
    </Layout>
  );
};

export default Home;
