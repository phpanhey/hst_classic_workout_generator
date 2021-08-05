import json
import os


def main():
    config = get_config()
    macro_training_protocol_dict = create_macro_training_protocol(config)
    macro_training_protocol_markdown = create_markdown_markup_macro_training_protocol(
        macro_training_protocol_dict
    )
    create_pdf_from_markdown(macro_training_protocol_markdown)


def get_config():
    with open("config.json", "r") as file:
        return json.loads(file.read())


def create_macro_training_protocol(config):
    exercises = config["exercises"]
    return {
        "15RM": create_micro_training_protocol("15RM", exercises),
        "10RM": create_micro_training_protocol("10RM", exercises),
        "5RM": create_micro_training_protocol("5RM", exercises),
    }


def create_micro_training_protocol(rm_type, exercises):
    return [
        create_training_protocol_by_excercise(rm_type, excercise)
        for excercise in exercises
    ]


def create_training_protocol_by_excercise(rm_type, excercise):
    progression_percentage = get_config()["progression_percentage"]
    training_unit_weights = get_training_unit_weights(
        excercise[rm_type], progression_percentage
    )
    return {
        "title": excercise["title"],
        "training_unit_1": training_unit_weights[0],
        "training_unit_2": training_unit_weights[1],
        "training_unit_3": training_unit_weights[2],
        "training_unit_4": training_unit_weights[3],
        "training_unit_5": training_unit_weights[4],
        "training_unit_6": training_unit_weights[5],
    }


def get_training_unit_weights(rm_weight, progression_percentage):
    res = []
    start_percentage = 100 - 5 * progression_percentage

    for i in range(6):
        res.append(round(rm_weight / 100 * start_percentage, 2))
        start_percentage += progression_percentage

    return res


def create_markdown_markup_micro_training_protocol(
    macro_training_protocol_dict, rm_type
):
    markdown = f"## Cycle {rm_type}\n"
    markdown += "|exercise|unit_1|unit_2|unit_3|unit_4|unit_5|unit_6|\n"
    markdown += "|--------|------|------|------|------|------|------|\n"
    for excercise in macro_training_protocol_dict[rm_type]:
        excercise_title = excercise["title"]
        unit_1 = excercise["training_unit_1"]
        unit_2 = excercise["training_unit_2"]
        unit_3 = excercise["training_unit_3"]
        unit_4 = excercise["training_unit_4"]
        unit_5 = excercise["training_unit_5"]
        unit_6 = excercise["training_unit_6"]
        markdown += f"|{excercise_title}|{unit_1}|{unit_2}|{unit_3}|{unit_4}|{unit_5}|{unit_6}|\n"
    return markdown


def create_markdown_markup_macro_training_protocol(macro_training_protocol_dict):
    markdown = "# hst macro-cycle trainingprotocol\n"
    markdown += create_markdown_markup_micro_training_protocol(
        macro_training_protocol_dict, "15RM"
    )
    markdown += create_markdown_markup_micro_training_protocol(
        macro_training_protocol_dict, "10RM"
    )
    markdown += create_markdown_markup_micro_training_protocol(
        macro_training_protocol_dict, "5RM"
    )
    return markdown


def write_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)


def create_pdf_from_markdown(markdown):
    write_to_file(markdown, "training_protocol.md")
    os.system(
        "pandoc training_protocol.md -o training_protocol.pdf --pdf-engine=xelatex"
    )


if __name__ == "__main__":
    main()
