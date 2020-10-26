module default {
    type Message {
        required property title -> str;
        required property created_at -> datetime;
        index on (.title);
    }
}
