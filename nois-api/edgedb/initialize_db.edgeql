CREATE DATABASE nois;

CONFIGURE SYSTEM INSERT Port {
    protocol := "graphql+http",
    database := "nois",
    address := "0.0.0.0",
    port := 8888,
    user := "http",
    concurrency := 4,
};
