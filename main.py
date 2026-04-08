from datetime import datetime


def get_gold_price():
    # пока заглушка (потом подключим API)
    return 2300.0


def predict_direction(price: float) -> str:
    if price > 2000:
        return "UP"
    return "DOWN"


def main():
    price = get_gold_price()
    direction = predict_direction(price)

    print(f"[{datetime.now()}]")
    print(f"Gold price: {price}")
    print(f"Prediction: {direction}")


if __name__ == "__main__":
    main()