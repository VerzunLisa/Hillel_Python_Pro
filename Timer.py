default_time = 60


def training_session(number_of_training: int):
    time_per_round = default_time

    def adjust_time(new_time):
        nonlocal time_per_round
        time_per_round = new_time

    for number_of_round in range(1, number_of_training+1):
        print(f'Раунд {number_of_round} : {time_per_round} хвилин.')
        time_per_round -= 5
    return adjust_time


print(training_session(3))
