/// trace(...)
var r = string(argument[0]), i;
for (i = 1; i < argument_count; i++) {
    r += ", " + string(argument[i])
}
show_debug_message(r)
f = file_text_open_append(working_directory + "log.txt");
file_text_write_string(f, r);
file_text_writeln(f);
file_text_close(f);
show_debug_message(working_directory + "log.txt");
