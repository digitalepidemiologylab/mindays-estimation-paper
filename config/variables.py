nutri_macro_vars = [
    "protein_eaten",
    "fat_eaten",
    "carb_eaten",
    "fiber_eaten",
    "alcohol_eaten",
]
personal_vars = [
    "age",
    "bmi",
    "bmr",
    "height",
    "weight",
    "cohabitants",
    "screen_hours",
    "stress_level",
    "defecate_quantity_per_day",
    "general_hunger_level",
    "morning_hunger_level",
    "evening_hunger_level",
    "mid_hunger_level",
]
amount_vars = ["eaten_quantity_in_gram", "energy_kcal_eaten", "energy_kj_eaten"]
nutri_micro_vars = [
    "beta_carotene_eaten",
    "folate_eaten",
    "iron_eaten",
    "magnesium_eaten",
    "niacin_eaten",
    "pantothenic_acid_eaten",
    "cholesterol_eaten",
    "fatty_acids_monounsaturated_eaten",
    "fatty_acids_polyunsaturated_eaten",
    "fatty_acids_saturated_eaten",
    "calcium_eaten",
    "phosphorus_eaten",
    "potassium_eaten",
    "sodium_eaten",
    "zinc_eaten",
    "vitamin_b1_eaten",
    "vitamin_b12_eaten",
    "vitamin_b2_eaten",
    "vitamin_b6_eaten",
    "vitamin_c_eaten",
    "vitamin_d_eaten",
    "salt_eaten",
    "sugar_eaten",
]
nutri_cfg_vars = [
    "dairy_products_meat_fish_eggs_tofu",
    "vegetables_fruits",
    "sweets_salty_snacks_alcohol",
    "non_alcoholic_beverages",
    "grains_potatoes_pulses",
    "oils_fats_nuts",
]
nutri_fg_vars = [
    "meat_fg_eaten",
    "fruits_fg_eaten",
    "vegetables_fg_eaten",
    "dairy_fg_eaten",
    "bread_fg_eaten",
    "oils_nuts_fg_eaten",
    "coffee_fg_eaten",
    "others_fg_eaten",
    "sugary_fg_eaten",
    "grains_cereals_fg_eaten",
    "fast_food_fg_eaten",
    "water_fg_eaten",
    "tea_fg_eaten",
    "alcohol_fg_eaten",
    "vegan_fg_eaten",
]
nutri_DI_vars = [
    "HEI",
    "aMED",
    "DASH",
    "mean_dds",
    "mean_berger_parker_kcal",
    "mean_simpson_diversity_kcal",
    "mean_gini_simpson_diversity_kcal",
    "mean_quantidd_kcal",
    # PDI_Quintile, hPDI_Quintile, mean_shannon_diversity_kcal, mean_mfad_jaccard_kcal
]

daynum_dict = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
daynum_dict_short = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
    4: "Fri",
    5: "Sat",
    6: "Sun",
}


def feature_color_assigner(feat):
    if feat in nutri_macro_vars:
        return "green"
    elif feat in nutri_micro_vars:
        return "cyan"
    elif feat in amount_vars:
        return "green"
    elif feat in nutri_cfg_vars:
        return "gold"
    elif feat in nutri_fg_vars:
        return "maroon"
    elif feat in nutri_DI_vars:
        return "purple"
    elif feat in personal_vars:
        return "red"
    else:
        return "black"
