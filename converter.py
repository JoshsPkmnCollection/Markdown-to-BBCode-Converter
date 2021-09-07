lines_to_output = []

with open("input.txt", 'r') as file_in:
    for line in file_in:
        line = line.strip()
        line = line.replace("<br>", "") # BBCode doesn't need breaks, it automatically adds newlines

        # convert headers to bold
        if line.startswith("# "):
            line = "[b][font size=\"5\"]" + line.split("# ")[1] + "[/font][/b]"
        elif line.startswith("#"):
            line = "[b][font size=\"5\"]" + line.split("#")[1] + "[/font][/b]"

        # convert horizontal rules
        if line == "---":
            line = "[hr]"

        if line.startswith("<img"):
            line = "[img style=\"width:500px;\"" + line.split("<img")[1].split(">")[0] + "]"

        lines_to_output.append(line)

with open("output.txt", 'w') as file_out:
    for line in lines_to_output:
        file_out.write(line + "\n")
