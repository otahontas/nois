import React from "react";

import { Button, Layout, Icon } from "@ui-kitten/components";
import { StyleSheet } from "react-native";

import useRecording from "../hooks/useRecording";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});

const MicIcon = props => <Icon {...props} name="mic-outline" />;

const StopIcon = props => <Icon {...props} name="stop-circle-outline" />;

// const PlayIcon = props => <Icon {...props} name="play-circle-outline" />;

const Home = () => {
  const [start, stop, status] = useRecording();

  //const checkAudioPermissions = async () => {
  //  const audioPermissions = await Audio.getPermissionsAsync();
  //  if (!audioPermissions.granted) {
  //    if (!audioPermissions.canAskAgain) {
  //      Alert.alert(
  //        "Audio recording not possible",
  //        "You have denied this app from getting any audio permissions, so recording is not possible",
  //        [{ text: "OK" }],
  //        { cancelable: false }
  //      );
  //      return false;
  //    } else {
  //      const request = await Audio.requestPermissionsAsync();
  //      if (!request.granted) {
  //        Alert.alert(
  //          "Audio recording not possible",
  //          "Recording messages is not possible if no permissions are granted",
  //          [{ text: "OK" }],
  //          { cancelable: false }
  //        );
  //        return false;
  //      }
  //      return true;
  //    }
  //  }
  //  return true;
  //};
  //   {isRecorded ? (
  //     <>
  //       <Text>Preview recording?</Text>
  //       <Button size="giant" accessoryLeft={PlayIcon} onPress={previewRecording} />
  //     </>
  //   ) : (

  return (
    <Layout style={styles.container}>
      <Button
        size="giant"
        accessoryLeft={status === "recording" ? StopIcon : MicIcon}
        onPressIn={start}
        onPressOut={stop}
      />
    </Layout>
  );
};

export default Home;
