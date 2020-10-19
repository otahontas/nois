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
  
  // TODO: Maybe change the recordingSettings later, aac doesn't look like a good choice
  //
  //
  const recordingSettings = {
    android: {
      extension: ".m4a",
      outputFormat: Audio.RECORDING_OPTION_ANDROID_OUTPUT_FORMAT_MPEG_4,
      audioEncoder: Audio.RECORDING_OPTION_ANDROID_AUDIO_ENCODER_AAC,
      sampleRate: 44100,
      numberOfChannels: 2,
      bitRate: 128000,
    },
    ios: {
      extension: ".m4a",
      outputFormat: Audio.RECORDING_OPTION_IOS_OUTPUT_FORMAT_MPEG4AAC,
      audioQuality: Audio.RECORDING_OPTION_IOS_AUDIO_QUALITY_MIN,
      sampleRate: 44100,
      numberOfChannels: 2,
      bitRate: 128000,
      linearPCMBitDepth: 16,
      linearPCMIsBigEndian: false,
      linearPCMIsFloat: false,
    },
  };

  const audioModeSettings = {
    allowsRecordingIOS: true,
    interruptionModeIOS: Audio.INTERRUPTION_MODE_IOS_DO_NOT_MIX,
    playsInSilentModeIOS: true,
    shouldDuckAndroid: true,
    interruptionModeAndroid: Audio.INTERRUPTION_MODE_ANDROID_DO_NOT_MIX,
    playThroughEarpieceAndroid: false,
    staysActiveInBackground: true,
  }

  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [recording, setRecording] = useState<any>(null);

  const startRecording = async () => {

    await Audio.setAudioModeAsync(audioModeSettings)

    const _recording = new Audio.Recording();
    try {
      await _recording.prepareToRecordAsync(recordingSettings)
      setRecording(_recording);
      await _recording.startAsync();
      console.log("recording now")
      setIsRecording(true);
    } catch (error) {
      console.error("error while recording:", error);
    }
  }
  
  const stopRecording = async () => {
    try {
      await recording.stopAndUnloadAsync();
    } catch (error) {
      console.error("error while stopping recording:", error);
    }
    setIsRecording(false);
  }

  // Add listening possibility after rec

  /*   if (!audioPermissions.granted) { */
  /*     if (!audioPermissions.canAskAgain) { */
  /*       Alert.alert( */
  /*         "Audio recording not possible", */
  /*         "You have denied this app from getting any audio permissions, so recording is not possible", */
  /*         [{ text: "OK" }], */
  /*         { cancelable: false } */
  /*       ); */
  /*     } else { */
  /*       const request = await Audio.requestPermissionsAsync() */
  /*       if (!request.granted) { */
  /*         Alert.alert( */
  /*           "Audio recording not possible", */
  /*           "Recording messages is not possible if no permissions are granted", */
  /*           [{ text: "OK" }], */
  /*           { cancelable: false } */
  /*         ); */
  /*       } */
  /*       return request.granted; */
  /*     }; */
  /*   return audioPermissions.granted; */
  /*   } */
  /* } */



  /* const startRecording = async () => { */
  /*   console.log("starting") */
  /*   const permissionsOk = await checkAudioPermissions() */
  /*   console.log(permissionsOk) */
  /*   if (!permissionsOk) return */
      
  /*   try { */
  /*     await recordingObject.prepareToRecordAsync(Audio.RECORDING_OPTIONS_PRESET_HIGH_QUALITY); */
  /*     await recordingObject.startAsync(); */
  /*   } catch (error) { */
  /*     console.log("error:", error); */
  /*   } */
  /*   setRecording(true); */
  /*   console.log("rec status", recording) */
  /* }; */

  /* const stopRecording = async () => { */
  /*   console.log("stopping") */
  /*   try { */
  /*     await recordingObject.stopAndUnloadAsync(); */
  /*   } catch (error) { */
  /*   } */
  /*   setRecording(false); */
  /*   console.log("rec status", recording) */
  /* } */

  return (
    <Layout style={styles.container}>
        <Button size="giant" 
          accessoryLeft={isRecording ? StopIcon : MicIcon} 
          onPressIn={startRecording}
          onPressOut={stopRecording}
      />
    </Layout>
  );
};

export default Home;
