"""
    Fonction BruteForce permettant d'avoir les meilleurs combinaisons
    d'action pouvant être acheté tout en respectant certainne condition:
    - Le montant maximum pouvant être mis est de 500 €

    Voici la configuration des data:
        Actions #  Coût par action (en euros) Bénéfice (après 2 ans)
    0    Action-1                          20                     5%
    1    Action-2                          30                    10%
    ---

    Nous constatons déja que le profit est correlé
    au prix de l'action * les bénéfice après 2 ans.
    Nous avons a disposition la formule suivante:
        profit = coût de l'action * (1 + bénéfice en pourcentage)
"""

import pandas as pd
from itertools import combinations


def benefice_after_two_years(action_cost, increase_rate):
    return action_cost * (1 + increase_rate)


def best_combinaison(data, cost_limite):
    actions = []

    for index, action in data.iterrows():
        action_name = action["Actions #"]
        cost_per_action = action["Coût par action (en euros)"]
        increase_rate = int(action["Bénéfice (après 2 ans)"]
                            .replace("%", "")) / 100
        future_benefice = benefice_after_two_years(
            cost_per_action, increase_rate)

        actions.append((action_name, cost_per_action, future_benefice))

    best_profit = 0
    best_combinaison_possible = []

    for i in range(1, len(actions) + 1):
        for combinaison in combinations(actions, i):
            total_cost = sum(action[1] for action in combinaison)
            total_profit = sum(action[2] for action in combinaison)

            if total_cost <= COST_LIMITE and total_profit > best_profit:
                best_profit = total_profit
                best_combinaison_possible = combinaison

    print("Action Name | Cost per action | increase after 2 years")
    for row in best_combinaison_possible:
        print(row)

    print(f"Profit :  {best_profit}€")


actions = pd.read_csv("liste_action.csv")
COST_LIMITE = 500
best_combinaison(actions, COST_LIMITE)
