import React from "react";

import { Button, Layout, Icon, Text, IconProps } from "@ui-kitten/components";
import { StyleSheet } from "react-native";

import useRecorder from "../hooks/useRecorder";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});

const MicIcon = (props: IconProps) => <Icon {...props} name="mic-outline" />;

const StopIcon = (props: IconProps) => <Icon {...props} name="stop-circle-outline" />;

const PlayIcon = (props: IconProps) => <Icon {...props} name="play-circle-outline" />;

const Recorder = () => {
  const { start, stop, preview, reset, status } = useRecorder();
  console.log(status);

  switch (status) {
    case "permissionsAndAskingAgainDenied":
      return (
        <Text appearance="alternative" status="basic">
          Recording is not possible, since you have denied this app from asking
          permissions to use your microphone. Maybe allow microphone usage in settings?
        </Text>
        // TODO: Link to settings here
        // TODO: Reload app after setting microphone
      );
    case "recorded":
      return (
        <>
          <Text appearance="alternative" category="h4" status="primary">
            Preview recording below
          </Text>
          <Button size="giant" accessoryLeft={PlayIcon} onPress={preview} />
          <Text appearance="alternative" status="basic">
            If you are ok with the recording, give it a title below
          </Text>
          <Text>Insert form here</Text>
          <Button onPress={reset}>Cancel</Button>
        </>
      );
    default:
      return (
        <Button
          size="giant"
          accessoryLeft={status === "recording" ? StopIcon : MicIcon}
          onPressIn={start}
          onPressOut={stop}
        />
      );
  }
};

const Home = () => {
  return (
    <Layout style={styles.container}>
      <Recorder />
    </Layout>
  );
};

export default Home;
