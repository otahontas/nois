import { Audio } from "expo-av";
import { Machine, assign } from "xstate";

/**
 * State machine for hook and its type definitions
 */

// TODO: Use immer instead of manual pure functions
type RecorderEvent =
  | { type: "PERMISSIONS_GIVEN" }
  | { type: "PERMISSIONS_DENIED" }
  | { type: "PERMISSIONS_AND_ASKING_AGAIN_DENIED" }
  | { type: "REJECT"; error: string }
  | { type: "START"; recording: Audio.Recording }
  | { type: "STOP"; sound: Audio.Sound; localUrl: string }
  | { type: "RESET" };

interface RecorderContext {
  error: string;
  recording: Audio.Recording | null;
  sound: Audio.Sound | null;
  localUrl: string;
}

const context = {
  error: "",
  recording: null,
  sound: null,
  localUrl: "",
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
  actions: ["resetRecording", "setSound", "setLocalUrl"],
};
const RESET = {
  target: "idle",
  actions: "reset",
};

const recorderMachine = Machine<RecorderContext, RecorderEvent>(
  {
    id: "recorder",
    initial: "idle",
    context,
    states: {
      idle: {
        on: {
          PERMISSIONS_GIVEN: "idle",
          PERMISSIONS_DENIED: "idle",
          PERMISSIONS_AND_ASKING_AGAIN_DENIED: "permissionsAndAskingAgainDenied",
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
      permissionsAndAskingAgainDenied: {},
    },
  },
  {
    actions: {
      // TODO: Fix typescript errors here
      setError: assign({ error: (_context, event) => event.error }),
      setRecording: assign({ recording: (_context, event) => event.recording }),
      setSound: assign({ sound: (_context, event) => event.sound }),
      setLocalUrl: assign({ localUrl: (_context, event) => event.localUrl }),
      reset: assign({
        error: (_context, _event) => "",
        recording: (_context, _event) => null,
        sound: (_context, __event) => null,
        localUrl: (_context, _event) => "",
      }),
      resetRecording: assign({ recording: (_context, _event) => null }),
    },
  }
);

export default recorderMachine;
