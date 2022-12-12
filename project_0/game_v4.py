import numpy as np
def random_predict(number: int = np.random.randint(1, 101)) -> int:
   """Randomly guess a number
   Args:
       number (int, optional): Hidden number. Defaults to 1.
   Returns:
       int: Number of attempts
   """
 
   count = 0
   max_number = 100
   min_number = 0
   predict_number = np.random.randint(1, 101) # prospective number
 
   while True:
       count += 1
 
       if predict_number > number:
           max_number = predict_number - 1
           predict_number = (max_number + min_number) // 2
 
 
       elif predict_number < number:
           min_number = predict_number + 1
           predict_number = (max_number + min_number) // 2
 
       else:
           break # end of the game, exit from the cycle
 
   return count
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    