import csv
import pandas as pd

account_data = pd.read_csv("Life and Death Account Data.csv")

account_data["Merits"] = account_data["Merits"].astype(int)
account_data["Demerits"] = account_data["Demerits"].astype(int)

account_data["Final Karma"] = account_data["Merits"] + account_data["Demerits"]


def merit_calculator(final_karma):
    if final_karma <= -100:
        return ("You will automatically be reincarnated into a beast with a below average life.")
    elif final_karma > -100 and final_karma <= 0:
        return ("You will automatically be reincarnated into a beast with an average life.")
    elif final_karma > 0 and final_karma <= 100:
        return ("You will automatically be reincarnated into a human with a less than average life.")
    elif final_karma > 100 and final_karma <= 300:
        return ("You will automatically be reincarnated into a human with an average life.")
    elif final_karma> 300 and final_karma <= 500:
        return ("You will automatically be reincarnated into a human with an above average life.")
    elif final_karma > 500: 
        return ("You will automatically be reincarnated into a human with a luxorious life! Congratulations!")
    else:
        return ("Error.")

account_data["Next Reincarnation"] = account_data["Final Karma"].apply(merit_calculator)


print(account_data)

# individual_stats = {}
# stat_names = ["Date of death", "Age of death", "Cause of death", "Merits", "Demerits"]



# def load_data(output, keys):
#     with open("Life and Death Account Data.csv") as life_and_death_data:
#         for line in csv.DictReader(life_and_death_data):
#             output[line["Name"]] = [line[key] for key in keys]


# load_data(individual_stats, stat_names)


