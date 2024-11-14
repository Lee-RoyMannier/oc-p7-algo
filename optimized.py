import csv
from typing import List, Tuple


def get_actions(file: str) -> List[Tuple[str, float, float]]:
    actions = []
    with open(file, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            price = float(row["price"])
            if price < 0:
                continue  # Ignorer les actions dont le prix est négatif
            profit_percentage = float(row["profit"])
            # Calcul du profit en euros
            profit = price * (profit_percentage / 100)
            actions.append((name, price, profit))
    return actions


def knapsack(actions: List[Tuple[str, float, float]], limit: float):
    n = len(actions)
    dp = [[0.0] * (int(limit * 100) + 1) for _ in range(n + 1)]

    # Remplissage de la table dp
    for i in range(1, n + 1):
        name, price, profit = actions[i - 1]
        for j in range(int(limit * 100) + 1):
            if int(price * 100) <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1]
                               [j - int(price * 100)] + profit)
            else:
                dp[i][j] = dp[i - 1][j]

    # Retrouver les actions choisies pour le profit maximal
    max_profit = dp[n][int(limit * 100)]
    total_cost = 0
    selected_actions = []
    j = int(limit * 100)

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:  # Cela signifie que l'action i a été ajoutée
            name, price, profit = actions[i - 1]
            selected_actions.append(actions[i - 1])
            j -= int(price * 100)
            total_cost += price

    return selected_actions, max_profit, total_cost


def main():
    actions = get_actions("dataset2_Python.csv")
    budget = 500
    selected_actions, max_profit, total_cost = knapsack(actions, budget)

    print("Meilleure combinaison d'actions pour un budget de 500€:")
    for action in selected_actions:
        print(f"{action[0]} - Coût: {action[1]
              :.2f}€ - Profit: {action[2]:.2f}€")
    print(f"\nCoût total de la meilleure combinaison: {total_cost:.2f}€")
    print(f"Profit total après 2 ans: {max_profit:.2f}€")


if __name__ == "__main__":
    main()
