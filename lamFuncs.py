def favorite_foods(*foods):
    print("Your favorite foods are:")
    for food in foods:
        print("-", food)

favorite_foods("Pizza", "Sushi", "Ice Cream")
favorite_foods("Banana", "Avocado")