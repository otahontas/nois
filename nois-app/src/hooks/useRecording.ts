import { useState } from "react";

import { Audio } from "expo-av";
// import * as FileSystem from "expo-file-system";

const useRecording = () => {
  const [status, setStatus] = useState<string>("idle");
  const [error, setError] = useState<any>(null);
  const [sound, setSound] = useState<Audio.Sound | null>(null);
  const [recording, setRecording] = useState<Audio.Recording | null>(null);
  const recordingSettings = Audio.RECORDING_OPTIONS_PRESET_HIGH_QUALITY;

  /**
   * Ask permissions for recording, load recorded into memory and prepare it for
   * recording.
   */
  const prepare = async () => {
    setStatus("preparing");
    const recordingToPrepare = new Audio.Recording();
    const { canRecord } = await recordingToPrepare.prepareToRecordAsync(
      recordingSettings
    );
    return { canRecord, preparedRecording: recordingToPrepare };
  };

  const start = async () => {
    const { canRecord, preparedRecording } = await prepare();
    if (!canRecord) return;
    try {
      const { isRecording } = await preparedRecording.startAsync();
      console.log(isRecording);
      setStatus("recording");
      setRecording(preparedRecording);
    } catch (error) {
      setStatus("error");
      setError(error);
    }
    setStatus("recording");
  };

  const stop = async () => {
    try {
      if (recording) {
        await recording.stopAndUnloadAsync();
        setStatus("done");
        const { sound: _sound } = await recording.createNewLoadedSoundAsync();
        setSound(_sound);
        setRecording(null);
      } else {
        // do this better
        setStatus("error");
      }
    } catch (error) {
      setStatus("error");
      setError(error);
    }
  };

  const preview = async () => {
    try {
      if (sound) {
        await sound.playAsync();
      }
    } catch (error) {
      setStatus("error");
      setError(error);
    }
  };

  return [start, stop, preview, status, error];
};

export default useRecording;
