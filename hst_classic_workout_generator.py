import json


def main():
    config = get_config()    
    workout_routine_dict = create_training_protocol(config)
    # create_pdf(workout_routine_dict)


def get_config():
    return json.loads(open("config.json", "r").read())


def create_training_protocol(config):
    return {"15RM": 20.0, "10RM": 25.0, "5RM": 27.0}


def create_training_protocol_by_excercise(rm_type, excercise):
    progression_percentage = get_config()["progression_percentage"]
    training_unit_weights = get_training_unit_weights(excercise[rm_type], progression_percentage)
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


def create_pdf(workout_routine_dict):
    pass


if __name__ == "__main__":
    main()
