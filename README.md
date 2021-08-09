# hypertrophy specific training (hst) workout generator
[hypertrophy specific training](https://fitoverfat.com/hypertrophy-specific-training/) constists of a macrocycle, divided into 3 microcycles (15rm,10rm,5rm). this project will help you to generate your optimal training protocol. It creates the microcycles for you and calculates the weight progressin per training unit. the picture below shows an example of the generated training protocol.
![hst training protocol](https://github.com/phpanhey/hst_classic_workout_generator/blob/master/images/hst_training_protocol.jpg?raw=true)

## usage
the script depends on a `config.json` that defines progression percentage, exercises and the repetition maximum (rm) of 15,10 and 5 repetitions:

```json
{
    "progression_percentage": 4.17,
    "exercises": [
        {
            "title": "bankdrücken",
            "15RM": 21.25,
            "10RM": 25,
            "5RM": 26.25
        },
        {
            "title": "military press",
            "15RM": 10,
            "10RM": 12.5,
            "5RM": 15
        },
        {
            "title": "schulternheben",
            "15RM": 45,
            "10RM": 50,
            "5RM": 52.5
        },
        {
            "title": "rudern",
            "15RM": 90,
            "10RM": 95,
            "5RM": 100
        },
        {
            "title": "kniebeugen",
            "15RM": 20,
            "10RM": 22.5,
            "5RM": 25
        },
        {
            "title": "fersenheben",
            "15RM": 65,
            "10RM": 72.5,
            "5RM": 80
        },
        {
            "title": "armbeuge sz",
            "15RM": 15,
            "10RM": 20,
            "5RM": 21.25
        },
        {
            "title": "trizepsdrücken",
            "15RM": 30,
            "10RM": 35,
            "5RM": 40
        }
    ]
}
```
typing
```bash
python3 hst_classic_workout_generator.py
```
will generate a `training_protocol.pdf`.

