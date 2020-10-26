# Application

This folder contains source for Nois application. Following technologies are used:
- [Typescript](https://www.typescriptlang.org/), main language
- [Expo](https://expo.io/), an app framework / platform for building and publishing application itself
- [Node](https://nodejs.org/en/), javascript runtime
- [UI Kitten](https://akveo.github.io/react-native-ui-kitten/), UI framework
- [Yarn](https://classic.yarnpkg.com/lang/en/), dependency management 
- [Apollo GraphQL client](https://www.apollographql.com/docs/react/), GraphQL client also handling most of the app state management
- [React Context](https://reactjs.org/docs/context.html), app state management for local data related stuff
- [Formik](https://www.formik.org), form library
- [Xstate](https://xstate.js.org/), state machine library for some custom hook state changes

[![Code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![App: Code style check](https://github.com/otahontas/nois/workflows/App:%20Code%20style%20check/badge.svg)](https://github.com/otahontas/nois/actions?query=workflow%3A%22App%3A+Code+style+check%22)

## Installation

Prerequisites:
- Expo, 3.28.0+
- Yarn, 1.22.10+
- Node, 14+

Install project by running `yarn install`.

## Usage

- Launch expo dev client by running `expo start`. This should open dev tools in your browser.
- Open the app in either simulator or with expo app in a real phone. Check dev tools for detailed info.

## App structure

- App is included in `src` folder with following subfolders:
  - `components`: Reusable components
  - `contexts`: React context providers
  - `graphql`: GraphQL queries, mutations and fragments
  - `hooks`: Custom React hooks
  - `screens`: Application screens built with components
  - `utils`: Different helper utils for application

## Tests and checks

- Code style and coding error tests can be run with `yarn lint` and (most) errors can be fixed with `yarn lint:fix`.
  - Project uses prettier and eslint with some plugins (such as import sorting, typescript) to ensure a consistent style accross app codebase.
  - See `.prettierrc` and `.eslintrc` for specific configurations.
- Tests are also run in CI-pipeline with Github Actions
