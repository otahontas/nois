# Nois

Anonymous voice message app. Project is still in very WIP status.

## Table of contents

* [General info](#general-info)
* [Setup](#setup)

## General info

Nois is a mobile application with jodel-style conversations, but with audio
messages. It is built with following stack:

* Application:
  * [Expo](https://expo.io/)
    * a React Native app framework / platform for building and publishing
  * [UI Kitten](https://akveo.github.io/react-native-ui-kitten/) UI framework
  * [Apollo GraphQL client](https://www.apollographql.com/docs/react/)
    * GraphQL client also handling most of the global app state management
  * [Formik](https://www.formik.org) for forms
  * [Xstate](https://xstate.js.org/) for handling complicated local state changes
* Cloud stuff:
  * [Hasura](https://hasura.io/) running in load-balanced Hasura Cloud.
    * Exposes one GraphQL-api, covering most of the backend business logic
  * [Yugabyte](https://www.yugabyte.com/) DB running in Yugabyte Cloud.
    * Postgres based distributed SQL database
  * [Auth0](https://auth0.com/)
    * Authentication and authorization platform

For more detailed look, see [app-architecture.md](docs/app-architecture.md) and
[cloud-architecture.md](docs/cloud-architecture.md) in docs folder.

## Setup

Prerequisites:

* Expo, 3.28.0+
* Yarn, 1.22.10+
* Node, 14+

1. Install project by running `yarn install`.
2. Launch expo dev client by running `expo start`. This should open dev tools
   in your browser.
3. Open the app in either simulator or with expo app in a real phone. Check
   dev tools for detailed info.
