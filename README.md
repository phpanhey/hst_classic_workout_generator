# hypertrophy specific training (hst) workout generator
[hypertrophy specific training](https://fitoverfat.com/hypertrophy-specific-training/) constists of a macrocycle, divided into 3 microcycles (15rm,10rm,5rm). this project will help you to generate your optimal training protocol. It creates the microcycles for you and calculates the weight progressin per training unit. the picture below shows an example of the generated training protocol.


![hst training protocol](https://github.com/phpanhey/hst_classic_workout_generator/blob/master/images/hst_training_protocol.jpg?raw=true)

## usage
the script depends on a `config.json` that defines progression percentage, exercises and the repetition maximum (rm) of 15,10 and 5 repetitions:

```json
{
    "progression_percentage": 5,
    "exercises": [
        {
            "title":"bench press",
            "15RM": 62.5,
            "10RM": 70,
            "5RM": 72.5
        },
        {
            "title":"military press",
            "15RM": 40,
            "10RM": 45,
            "5RM": 50
        },
        {
            "title":"shoulder raise",
            "15RM": 110,
            "10RM": 120,
            "5RM": 125
        },
        {
            "title":"rowing",
            "15RM": 90,
            "10RM": 95,
            "5RM": 100
        },
        {
            "title":"squats",
            "15RM": 60,
            "10RM": 65,
            "5RM": 70
        },
        {
            "title":"heel raises",
            "15RM": 65,
            "10RM": 72.5,
            "5RM": 80
        },
        {
            "title":"curls",
            "15RM": 37,
            "10RM": 47,
            "5RM": 49.5
        },
        {
            "title":"triceps extension",
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

