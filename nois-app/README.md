# Nois app

This folder contains source for Nois application, which is mainly built with Typescript, React Native / Expo, Apollo GraphQL -client and UI Kitten -framework.

[![Code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![App: Code style check](https://github.com/otahontas/nois/workflows/App:%20Code%20style%20check/badge.svg)](https://github.com/otahontas/nois/actions?query=workflow%3A%22App%3A+Code+style+check%22)

## Installation

Prerequisites:
- [Expo](https://expo.io/), 3.28.0+
- [Yarn](https://yarnpkg.com/), 1.22.10+
- [Node](https://nodejs.org/en/), 14+

Install project by cloning the repo and running `yarn install`.

## Usage

- Launch project by running `expo start` and open app in either simulator or with expo app in a real phone.

## App structure

- Following stucture is followed:
  - components: Reusable components
  - contexts: React context providers
  - graphql: GraphQL queries, mutations and fragments
  - hooks: Custom React hooks
  - screens: Application screens built with components
  - utils: Different helper utils for application

## Tests

- Code style and coding error tests can be run with `yarn lint` and (most) errors can be fixed with `yarn lint:fix`.
  - Project uses prettier and eslint with some plugins (such as import sorting, typescript) to ensure a consistent style accross app codebase.
  - See `.prettierrc` and `.eslintrc` for specific configurations.
- Tests are also run in CI-pipeline with Github Actions
