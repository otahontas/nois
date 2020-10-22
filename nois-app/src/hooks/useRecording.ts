import { useMachine } from "@xstate/react";
import { Audio } from "expo-av";
import { Machine, assign } from "xstate";

const context = {
  error: null,
  recording: null,
  sound: null,
  localUrl: null,
};

const REJECT = {
  target: "rejected",
  actions: "setError",
};

const START = {
  target: "recording",
  actions: "setRecording",
};

const STOP = {
  target: "recorded",
  actions: ["setRecording", "setSound", "setLocalUrl"],
};
const RESET = {
  target: "idle",
  actions: "reset",
};

const recorderMachine = Machine(
  {
    id: "recorder",
    initial: "idle",
    context,
    states: {
      idle: {
        on: {
          PERMISSIONS_GIVEN: "idle",
          PERMISSIONS_DENIED: "idle",
          PERMISSIONS_AND_ASKING_AGAIN_DENIED: "permissionAndAskingAgainDenied",
          START,
          REJECT,
          RESET,
        },
      },
      recording: {
        on: {
          STOP,
          REJECT,
          RESET,
        },
      },
      recorded: {
        on: {
          REJECT,
          RESET,
        },
      },
      rejected: {
        on: {
          RESET,
        },
      },
      permissionAndAskingAgainDenied: {},
    },
  },
  {
    actions: {
      setError: assign({ error: (context, event) => event.error }),
      setRecording: assign({ recording: (context, event) => event.recording }),
      setSound: assign({ sound: (context, event) => event.sound }),
      setLocalUrl: assign({ localUrl: (context, event) => event.localUrl }),
      reset: assign({ error: null, recording: null, sound: null, localUrl: null }),
    },
  }
);

const useRecording = () => {
  const [state, send] = useMachine(recorderMachine);

  /**
   * Check permissions for recording, load recorder into memory and prepare it for
   * recording.
   */
  const prepare = async () => {
    const { granted, canAskAgain } = await Audio.getPermissionsAsync();

    if (!granted) {
      if (!canAskAgain) {
        send("PERMISSIONS_AND_ASKING_AGAIN_DENIED");
      } else {
        const { granted } = await Audio.requestPermissionsAsync();
        const stateChange = granted ? "PERMISSIONS_GIVEN" : "PERMISSIONS_DENIED";
        send(stateChange);
      }
      return;
    }

    const recording = new Audio.Recording();
    try {
      await recording.prepareToRecordAsync(Audio.RECORDING_OPTIONS_PRESET_HIGH_QUALITY);
      return recording;
    } catch (error) {
      send({ type: "REJECT", error: error.message });
      return;
    }
  };

  /**
   * Start recording onto loaded recorder
   */
  const start = async () => {
    try {
      const recording = await prepare();
      if (!recording) return;
      await recording.startAsync();
      send({ type: "START", recording });
    } catch (error) {
      send({ type: "REJECT", error: error.message });
    }
  };

  /**
   * Stop recording, load recorded message to state and delete recording
   */
  const stop = async () => {
    try {
      const { recording } = state.context;
      await recording.stopAndUnloadAsync();
      const { sound } = await recording.createNewLoadedSoundAsync();
      const localUrl = recording.getURI();
      send({ type: "STOP", recording: null, sound, localUrl });
    } catch (error) {
      send({ type: "REJECT", error: error.message });
    }
  };

  /**
   * Preview recorded message
   */
  const preview = async () => {
    try {
      const { sound } = state.context;
      await sound.replayAsync();
    } catch (error) {
      send({ type: "REJECT", error: error.message });
    }
  };

  /**
   * Reset everything to basic state
   */
  const reset = async () => send("RESET");

  return {
    start,
    stop,
    preview,
    reset,
    status: state.value,
    error: state.context.error,
    localUrl: state.context.localUrl,
  };
};

export default useRecording;
