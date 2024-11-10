import csv
from itertools import combinations
from typing import List


def calculate_profit(actions):
    # Calcule uniquement le profit net sans inclure le coût initial
    return sum(cost * (profit / 100) for _, cost, profit in actions)


def getActions(file: str) -> List:
    actions = []
    with open(file, "r") as f:
        action = csv.DictReader(f)
        for item in action:
            action_name = item["Actions #"]
            action_cost = int(item["Coût par action (en euros)"])
            profit_after_two_years = float(
                item["Bénéfice (après 2 ans)"].replace("%", ""))
            actions.append((action_name, action_cost, profit_after_two_years))
    return actions


def createActionsCombination(data, limit=500):
    max_profit = 0
    min_cost = float('inf')  # Initialise le coût minimum à l'infini
    best_investissement = []
    n = len(data)

    for i in range(1, n + 1):
        for action_comb in combinations(data, i):
            sum_actions_cost = sum(cost for _, cost, _ in action_comb)

            if sum_actions_cost <= limit:
                profit = calculate_profit(action_comb)
                if profit > max_profit or (profit == max_profit and sum_actions_cost < min_cost):
                    max_profit = profit
                    min_cost = sum_actions_cost
                    best_investissement = action_comb

    print(f"Profit maximum: {max_profit}€, Coût: {min_cost}€")
    for action in best_investissement:
        print(f"{action[0]} - Coût: {action[1]}€ - Bénéfice: {action[2]}%")


# Utilisation du programme avec un fichier CSV
actions_list = getActions("liste_action.csv")
createActionsCombination(actions_list)
