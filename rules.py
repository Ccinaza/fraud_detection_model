import pandas as pd

def is_suspicious(row, df):
    # Rule 1: Regulatory Requirements
    if (row['transaction_amount'] >= 5_000_000 and row['account_type'] == 'Personal') or \
       (row['transaction_amount'] >= 10_000_000 and row['account_type'] == 'Business'):
        return 1

    # Rule 2: Frequent Transactions to Same Account over 3 times within 1 hour
    if row['transaction_frequency_same_account'] > 3 and \
       row['time_delta_same_account'] <= pd.Timedelta(hours=1):
        return 1

    # Rule 3: High Total Daily Transaction Amount
    if row['daily_transaction_amount'] > 5_000_000:
        return 1

    # Rule 4: Unusually High Transaction Frequency
    if row['transaction_frequency'] > 8 and row['transaction_type'] == 'Bank Transfer' and \
       row['time_delta_same_account'] <= pd.Timedelta(hours=1):
        return 1

    # Rule 5: Late-Night Bank Transfers
    if row['transaction_date_time'].strftime('%H:%M:%S') >= '23:00:00' and \
       row['transaction_date_time'].strftime('%H:%M:%S') <= '05:00:00' and \
       row['transaction_type'] == 'Bank Transfer':
        if row['previous_transaction_time'] is not None and \
           row['previous_transaction_time'] < row['transaction_date_time']:
            return 1

    # Rule 6: Early-Morning Bank Transfers with High Amounts
    if row['transaction_date_time'].strftime('%H:%M:%S') >= '00:00:00' and \
       row['transaction_date_time'].strftime('%H:%M:%S') <= '05:00:00' and \
       row['transaction_type'] == 'Bank Transfer' and row['transaction_amount'] > 49_000:
        return 1

    # Rule 7: New Account Restrictions for Bank Transfers
    if row['account_age_days'] <= 14 and row['transaction_frequency'] > 3 and \
       row['transaction_amount'] > 99_000 and row['transaction_type'] == 'Bank Transfer':
        return 1

    # Rule 8: New Account Restrictions for VAS (Sport Betting)
    if row['account_age_days'] <= 14 and row['transaction_type'] == 'Sport Betting' and \
       row['transaction_amount'] > 30_000:
        recent_sport_betting = df[(df['account_id'] == row['account_id']) & 
                                  (df['transaction_type'] == 'Sport Betting') & 
                                  (df['transaction_date_time'] >= row['transaction_date_time'] - pd.Timedelta(hours=3))]
        if recent_sport_betting['transaction_id'].count() > 3:
            return 1

    # Rule 9: New Account Restrictions for VAS (Airtime)
    if row['account_age_days'] <= 14 and row['transaction_type'] == 'Airtime' and \
       row['transaction_amount'] > 4_999:
        recent_airtime_purchase = df[(df['account_id'] == row['account_id']) & 
                                     (df['transaction_type'] == 'Airtime') & 
                                     (df['transaction_date_time'] >= row['transaction_date_time'] - pd.Timedelta(hours=1))]
        if recent_airtime_purchase['transaction_id'].count() > 3:
            return 1

    return 0
