import React from "react";

import { Button, Layout, Icon, Text, IconProps } from "@ui-kitten/components";
import { Formik } from "formik";
import { StyleSheet, View } from "react-native";

import FormikTextInput from "../components/FormikTextInput";
import useRecorder from "../hooks/useRecorder";

const styles = StyleSheet.create({
  formContainer: {
    padding: 15,
  },
  fieldContainer: {
    marginBottom: 15,
  },
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});

const MicIcon = (props: IconProps) => <Icon {...props} name="mic-outline" />;

const StopIcon = (props: IconProps) => <Icon {...props} name="stop-circle-outline" />;

const PlayIcon = (props: IconProps) => <Icon {...props} name="play-circle-outline" />;

const AddRecordingForm = ({ onSubmit }) => {
  return (
    <View style={styles.formContainer}>
      <View style={styles.fieldContainer}>
        <FormikTextInput placeholder="Recording title" name="recordingTitle" />
      </View>
      <Button onPress={onSubmit}>Send recording</Button>
    </View>
  );
};

const Recorder = () => {
  const { start, stop, preview, reset, status } = useRecorder();
  const onSubmit = async values => console.log("form values:", values);

  switch (status) {
    case "permissionsAndAskingAgainDenied":
      return (
        <>
          <Text appearance="alternative" status="basic">
            Recording is not possible, since you have denied this app from asking
            permissions to use your microphone. Maybe allow microphone usage in
            settings?
          </Text>
          <Button onPress={reset}>Cancel</Button>
        </>
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
          <Formik initialValues={{ recordingTitle: "" }} onSubmit={onSubmit}>
            {({ handleSubmit }) => <AddRecordingForm onSubmit={handleSubmit} />}
          </Formik>
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
