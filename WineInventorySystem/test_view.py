from backend.wine_controller import get_all_wines

wines = get_all_wines()

for wine in wines:
    print(wine)
