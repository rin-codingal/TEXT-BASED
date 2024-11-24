import random

def pick_ball():
    balls = ["Blue", "Red", "Green"]
    result = random.choice(balls)

    prob = balls.count("Red") / len(balls)
    print(f"Probability of picking Red Ball is: {prob}")

    if result == "Red":
        return " Red Ball was picked "
    else:
        return "Better Luck Next time"


res = pick_ball()
print(res)