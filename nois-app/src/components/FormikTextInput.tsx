import React from "react";

import { Input, Text } from "@ui-kitten/components";
import { useField } from "formik";
import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  input: {
    margin: 2,
  },
  errorText: {
    marginTop: 5,
    color: "red",
  },
});

const FormikTextInput = ({ name, ...props }) => {
  const [field, meta, helpers] = useField(name);
  const showError = meta.touched && meta.error;

  return (
    <>
      <Input
        status={showError ? "danger" : "basic"}
        onChangeText={value => helpers.setValue(value)}
        onBlur={() => helpers.setTouched(true)}
        value={field.value}
        style={styles.input}
        {...props}
      />
      {showError && <Text style={styles.errorText}>{meta.error}</Text>}
    </>
  );
};
export default FormikTextInput;
