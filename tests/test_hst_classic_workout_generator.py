import unittest
import sys
import os
import os.path

sys.path.append(os.getcwd())
from hst_classic_workout_generator import (
    get_config,
    create_macro_training_protocol,
    create_micro_training_protocol,
    create_training_protocol_by_excercise,
    get_training_unit_weights,
    create_markdown_markup_micro_training_protocol,
    create_markdown_markup_macro_training_protocol,
    write_to_file,
    create_pdf_from_markdown,
)


class TestHstClassicWorkoutGenerator(unittest.TestCase):

    macro_training_protocol_dict = {
        "15RM": [
            {
                "title": "bench press",
                "training_unit_1": 15.83,
                "training_unit_2": 16.66,
                "training_unit_3": 17.5,
                "training_unit_4": 18.33,
                "training_unit_5": 19.17,
                "training_unit_6": 20.0,
            }
        ],
        "10RM": [
            {
                "title": "bench press",
                "training_unit_1": 19.79,
                "training_unit_2": 20.83,
                "training_unit_3": 21.87,
                "training_unit_4": 22.92,
                "training_unit_5": 23.96,
                "training_unit_6": 25.0,
            }
        ],
        "5RM": [
            {
                "title": "bench press",
                "training_unit_1": 21.37,
                "training_unit_2": 22.5,
                "training_unit_3": 23.62,
                "training_unit_4": 24.75,
                "training_unit_5": 25.87,
                "training_unit_6": 27.0,
            }
        ],
    }

    def test_get_config(self):
        self.assertIsNotNone(get_config())

    def test_create_macro_training_protocol(self):
        input = {
            "progression_percentage": 4.17,
            "exercises": [
                {
                    "title": "bench press",
                    "15RM": 20.0,
                    "10RM": 25.0,
                    "5RM": 27.0,
                }
            ],
        }
        expected = {
            "15RM": [
                {
                    "title": "bench press",
                    "training_unit_1": 15.83,
                    "training_unit_2": 16.66,
                    "training_unit_3": 17.5,
                    "training_unit_4": 18.33,
                    "training_unit_5": 19.17,
                    "training_unit_6": 20.0,
                }
            ],
            "10RM": [
                {
                    "title": "bench press",
                    "training_unit_1": 19.79,
                    "training_unit_2": 20.83,
                    "training_unit_3": 21.87,
                    "training_unit_4": 22.92,
                    "training_unit_5": 23.96,
                    "training_unit_6": 25.0,
                },
            ],
            "5RM": [
                {
                    "title": "bench press",
                    "training_unit_1": 21.37,
                    "training_unit_2": 22.5,
                    "training_unit_3": 23.62,
                    "training_unit_4": 24.75,
                    "training_unit_5": 25.87,
                    "training_unit_6": 27.0,
                }
            ],
        }
        self.assertEqual(create_macro_training_protocol(input), expected)

    def test_create_micro_training_protocol(self):
        input = [
            {
                "title": "bankdrücken schrägbank",
                "15RM": 20.0,
                "10RM": 25.0,
                "5RM": 27.0,
            }
        ]
        expected = [
            {
                "title": "bankdrücken schrägbank",
                "training_unit_1": 15.83,
                "training_unit_2": 16.66,
                "training_unit_3": 17.5,
                "training_unit_4": 18.33,
                "training_unit_5": 19.17,
                "training_unit_6": 20.0,
            }
        ]
        self.assertEqual(create_micro_training_protocol("15RM", input), expected)

    def test_create_training_protocol_by_excercise(self):
        input = {"title": "schredder", "15RM": 20.0, "10RM": 25.0, "5RM": 27.0}
        expected = {
            "title": "schredder",
            "training_unit_1": 15.83,
            "training_unit_2": 16.66,
            "training_unit_3": 17.5,
            "training_unit_4": 18.33,
            "training_unit_5": 19.17,
            "training_unit_6": 20.0,
        }

        self.assertEqual(
            create_training_protocol_by_excercise("15RM", input),
            expected,
        )

    def test_get_training_unit_weights(self):
        expected = [45.0, 48.0, 51.0, 54.0, 57.0, 60.0]
        rm_weight = 60.0
        progression_percentage = 5.0
        self.assertEqual(
            get_training_unit_weights(rm_weight, progression_percentage),
            expected,
        )

    def test_create_markdown_markup_micro_training_protocol(self):
        self.assertIsNotNone(
            create_markdown_markup_micro_training_protocol(
                self.macro_training_protocol_dict, "15RM"
            )
        )

    def test_create_markdown_markup_macro_training_protocol(self):
        self.assertIsNotNone(
            create_markdown_markup_macro_training_protocol(
                self.macro_training_protocol_dict
            )
        )

    def test_write_to_file(self):
        filename = "lorem.txt"
        write_to_file("lorem", filename)
        self.assertTrue(os.path.isfile(filename))
        os.remove(filename)

    def test_create_pdf_from_markdown(self):
        markdown = "# markdown"
        create_pdf_from_markdown(markdown)
        filename = "training_protocol.pdf"
        self.assertTrue(os.path.isfile(filename))
        os.remove(filename)


if __name__ == "__main__":
    unittest.main()
