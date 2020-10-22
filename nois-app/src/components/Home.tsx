import React from "react";

import { Button, Layout, Icon, Text } from "@ui-kitten/components";
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

const PlayIcon = props => <Icon {...props} name="play-circle-outline" />;

const Home = () => {
  const [start, stop, preview, reset, status] = useRecording();

  return (
    <Layout style={styles.container}>
      {status === "recorded" ? (
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
      ) : (
        <Button
          size="giant"
          accessoryLeft={status === "recording" ? StopIcon : MicIcon}
          onPressIn={start}
          onPressOut={stop}
        />
      )}
    </Layout>
  );
};

export default Home;
