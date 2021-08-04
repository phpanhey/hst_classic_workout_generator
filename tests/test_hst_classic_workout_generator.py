import unittest
from hst_classic_workout_generator import (
    create_training_protocol_by_excercise,
    get_training_unit_weights,
)


class TestHstClassicWorkoutGenerator(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
