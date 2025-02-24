import pingouin as pg
import pandas as pd
from tqdm import tqdm
from itertools import combinations


def calculate_icc(data, targets="subject_key", raters="day_of_week", ratings="target"):
    """
    Calculate the Intra-class Correlation (ICC) for the given dataset.

    Parameters:
    data (pd.DataFrame): The input DataFrame with columns 'subject_key', 'days_of_week', and 'target'.

    Returns:
    pd.DataFrame: A DataFrame with the ICC results.
    """
    icc_result = pg.intraclass_corr(
        data=data, targets=targets, raters=raters, ratings=ratings
    )

    return icc_result


def compute_icc_nk(
    df,
    columns_to_exclude=[
        "subject_key",
        "day_of_week",
        "energy_kj_eaten",
        "alcohol_fg_eaten",
    ],
):
    icc_3k_res = {}

    for col in tqdm(df.columns):
        if col in columns_to_exclude:
            continue

        per_col_daywise_icc = []
        for daynum in range(1, 7):
            icc_computed_df = calculate_icc(
                df[df["day_of_week"] <= daynum],
                targets="subject_key",
                raters="day_of_week",
                ratings=col,
            )
            icc_val = round(
                icc_computed_df[icc_computed_df["Type"] == "ICC3k"]["ICC"].values[0], 2
            )
            per_col_daywise_icc.append(icc_val)

        icc_3k_res[col] = per_col_daywise_icc

    return pd.DataFrame(icc_3k_res)


def calculate_icc_for_day_combinations(
    data, targets="subject_key", raters="day_of_week", ratings="target", num_days=2
):

    res_icck_comb = {}

    for day_comb in combinations([0, 1, 2, 3, 4, 5, 6], num_days):
        icc_computed_df = calculate_icc(
            data[data["day_of_week"].isin(day_comb)],
            targets="subject_key",
            raters="day_of_week",
            ratings=ratings,
        )
        icc_val = icc_computed_df[icc_computed_df["Type"] == "ICC3k"]["ICC"].values[0]
        icc_val = round(float(icc_val), 2)
        res_icck_comb[str(day_comb)] = icc_val

    return res_icck_comb


def calculate_icc_for_day_combinations_wrapper(
    df, col_of_interest, day_range=range(2, 8)
):
    """
    Calculate ICC for day combinations and concatenate results into a single DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    col_of_interest (str): The name of the column for which to calculate ICC.
    day_range (range): The range of days for which to calculate ICC. Default is range(2, 7).

    Returns:
    pd.DataFrame: A DataFrame containing the ICC results for each day combination.
    """
    allnum_daywise_comb_icc_per_feat = pd.DataFrame()

    for numday in tqdm(day_range):
        daywise_comb_icc_per_feat_dict = calculate_icc_for_day_combinations(
            df,
            targets="subject_key",
            raters="day_of_week",
            ratings=col_of_interest,
            num_days=numday,
        )
        daywise_comb_icc_per_feat = pd.DataFrame(
            [daywise_comb_icc_per_feat_dict], index=["ICC"]
        ).T
        daywise_comb_icc_per_feat["numdays"] = numday
        daywise_comb_icc_per_feat["feature"] = col_of_interest
        allnum_daywise_comb_icc_per_feat = pd.concat(
            [allnum_daywise_comb_icc_per_feat, daywise_comb_icc_per_feat]
        )

    return allnum_daywise_comb_icc_per_feat


def icc_daywise_combinations(df, feature, mean_of_feat_per_user, threshold=0.8):
    """
    Calculate ICC values for different combinations of days until a threshold is reached.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing the data
    feature (str): Name of the feature column to calculate ICC for
    mean_of_feat_per_user (pd.DataFrame): DataFrame containing mean values per user
    threshold (float): ICC threshold value to stop calculation, default 0.8

    Returns:
    list: List of lists containing [feature, day_combination, num_days, icc_value]
          for each combination tested until threshold is reached
    """
    threshold_achieved = False
    res = []

    for numday in range(1, 7):
        daywise_combinations = combinations([0, 1, 2, 3, 4, 5, 6], numday)

        for comb in daywise_combinations:
            df_subset = df[df["day_of_week"].isin(comb)][
                ["subject_key", "day_of_week", feature]
            ].copy()
            df_subset["judge"] = "B"

            df_subset_and_mean_data = pd.concat([mean_of_feat_per_user, df_subset])

            icc_val = calculate_icc(
                df_subset_and_mean_data,
                targets="subject_key",
                raters="judge",
                ratings=feature,
            )["ICC"].values[2]

            res.append([feature, comb, numday, round(float(icc_val), 2)])

            if icc_val >= threshold:
                threshold_achieved = True

        if threshold_achieved:
            break

    return res


def icc_daywise_combinations_allcombos(
    df, feature, mean_of_feat_per_user, threshold=0.8
):
    """
    Calculate ICC values for all possible combinations of days from 1 to 6 days.
    Unlike icc_daywise_combinations(), this function continues calculating ICC values
    even after reaching the threshold.

    Requires:
    - DataFrame with day_of_week and feature columns
    - Feature name to analyze
    - Pre-calculated mean values per user
    - Optional threshold (though not used for early stopping)
    """
    # threshold_achieved = False
    res = []

    for numday in range(1, 7):
        daywise_combinations = combinations([0, 1, 2, 3, 4, 5, 6], numday)

        for comb in daywise_combinations:
            df_subset = df[df["day_of_week"].isin(comb)][
                ["subject_key", "day_of_week", feature]
            ].copy()
            df_subset["judge"] = "B"

            df_subset_and_mean_data = pd.concat([mean_of_feat_per_user, df_subset])

            icc_val = calculate_icc(
                df_subset_and_mean_data,
                targets="subject_key",
                raters="judge",
                ratings=feature,
            )["ICC"].values[2]

            res.append([feature, comb, numday, round(float(icc_val), 2)])

        #     if icc_val >= threshold:
        #         threshold_achieved = True

        # # if threshold_achieved:
        # #     break

    return res
