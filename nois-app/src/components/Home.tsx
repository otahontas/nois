import React, { useState } from 'react';
import { Alert, StyleSheet } from 'react-native';
import { Button, Layout, Text, Icon} from '@ui-kitten/components';
import { Audio } from 'expo-av';
import * as FileSystem from 'expo-file-system';

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

const PlayIcon = (props) => (
  <Icon {...props} name='play-circle-outline'/>
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

  const recordingModeSettings = {
    allowsRecordingIOS: true,
    interruptionModeIOS: Audio.INTERRUPTION_MODE_IOS_DO_NOT_MIX,
    playsInSilentModeIOS: true,
    shouldDuckAndroid: true,
    interruptionModeAndroid: Audio.INTERRUPTION_MODE_ANDROID_DO_NOT_MIX,
    playThroughEarpieceAndroid: false,
    staysActiveInBackground: true,
  }

  const playingModeSettings = {      
    allowsRecordingIOS: false,
    interruptionModeIOS: Audio.INTERRUPTION_MODE_IOS_DO_NOT_MIX,
    playsInSilentModeIOS: true,
    playsInSilentLockedModeIOS: true,
    shouldDuckAndroid: true,
    interruptionModeAndroid: Audio.INTERRUPTION_MODE_ANDROID_DO_NOT_MIX,
    playThroughEarpieceAndroid: false,
    staysActiveInBackground: true
  }

  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [isRecorded, setIsRecorded] = useState<boolean>(false);
  const [recording, setRecording] = useState<any>(null);
  const [sound, setSound] = useState<any>(null);

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
        return false
      } else {
        const request = await Audio.requestPermissionsAsync()
        if (!request.granted) {
          Alert.alert(
            "Audio recording not possible",
            "Recording messages is not possible if no permissions are granted",
            [{ text: "OK" }],
            { cancelable: false }
          );
          return false
        }
        return true
      };
    }
    return true
  }

  const startRecording = async () => {
    const permissionsOk = await checkAudioPermissions();
    console.log("starting, permissions: ", permissionsOk);
    if (!permissionsOk) return

    await Audio.setAudioModeAsync(recordingModeSettings)

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
    const permissionsOk = await checkAudioPermissions();
    if (!permissionsOk) return
    try {
      await recording.stopAndUnloadAsync();
    } catch (error) {
      console.error("error while stopping recording:", error);
    }
    const info = await FileSystem.getInfoAsync(recording.getURI());
    console.log(`FILE INFO: ${JSON.stringify(info)}`);
    await Audio.setAudioModeAsync(playingModeSettings)
    const { sound: _sound } = await recording.createNewLoadedSoundAsync(
      {
        isLooping: true,
        isMuted: false,
        volume: 1.0,
        rate: 1.0,
        shouldCorrectPitch: true,
      }
    );
    setSound(_sound);
    setIsRecording(false);
    setIsRecorded(true);
  }

  const previewRecording = async () => {
    try {
      await sound.playAsync();
    } catch (error) {
      console.error("Error happened while playing file", error)
    }
  }

  return (
    <Layout style={styles.container}>
      {isRecorded
        ? <>
            <Text>Preview recording?</Text>
            <Button size="giant" 
              accessoryLeft={PlayIcon} 
              onPress={previewRecording}
            />
          </>
        : <Button size="giant" 
            accessoryLeft={isRecording ? StopIcon : MicIcon} 
            onPressIn={startRecording}
            onPressOut={stopRecording}
          />
      }
    </Layout>
  );
};

export default Home;
