import { useState } from "react";

import { Audio } from "expo-av";

const useRecording = () => {
  const [status, setStatus] = useState<string>("idle");
  const [error, setError] = useState<string>("");
  const [recording, setRecording] = useState<Audio.Recording | null>(null);
  const [url, setUrl] = useState<string | null>(null);
  const [sound, setSound] = useState<Audio.Sound | null>(null);
  const recordingSettings = Audio.RECORDING_OPTIONS_PRESET_HIGH_QUALITY;

  /**
   * Check permissions for recording, load recorder into memory and prepare it for
   * recording.
   */
  const prepare = async () => {
    setStatus("preparing");
    const recordingToPrepare = new Audio.Recording();
    const audioPermissions = await Audio.getPermissionsAsync();
    if (!audioPermissions.granted) return;
    const { canRecord } = await recordingToPrepare.prepareToRecordAsync(
      recordingSettings
    );
    return { canRecord, preparedRecording: recordingToPrepare };
  };

  /**
   * Start recording onto loaded recorder
   */
  const start = async () => {
    try {
      const { canRecord, preparedRecording } = await prepare();
      if (!canRecord) {
        setStatus("error");
        setError("Recording is not possible for some unknown reason");
        return;
      }
      setStatus("recording");
      await preparedRecording.startAsync();
      setRecording(preparedRecording);
    } catch (error) {
      setStatus("error");
      setError(error.message);
    }
  };

  /**
   * Stop recording, load recorded message to state and delete recording
   */
  const stop = async () => {
    try {
      if (!recording) {
        setStatus("error");
        setError("Stopping is not possible since there is no recording available.");
        return;
      }
      await recording.stopAndUnloadAsync();
      setStatus("recorded");
      const { sound: recordedSound } = await recording.createNewLoadedSoundAsync();
      setSound(recordedSound);
      setUrl(recording.getURI());
      setRecording(null);
    } catch (error) {
      setStatus("error");
      setError(error);
    }
  };

  /**
   * Preview recorded message
   */
  const preview = async () => {
    try {
      if (!sound) {
        console.log("no sound :(");
        setStatus("error");
        setError("There is no message to play");
        return;
      }
      await sound.replayAsync();
    } catch (error) {
      setStatus("error");
      setError(error);
    }
  };

  /**
   * Reset everything to basic state
   */
  const reset = async () => {
    setStatus("idle");
    setError("");
    setRecording(null);
    setUrl(null);
    setSound(null);
  };
  return [start, stop, preview, reset, status, error, url, reset];
};

export default useRecording;
