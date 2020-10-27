module default {
    type Message {
        required property title -> str;
        required property created_at -> datetime;
        required property recording_content_type -> str;
        required property recording_extension -> str;
        index on (.title);
    }
}
