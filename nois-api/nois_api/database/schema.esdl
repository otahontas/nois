module default {
    type Message {
        required property title -> str;
        index on (.title);
    }
}
