hours = input('Enter number of hours you worked this week: ')
# Python 3 output numeric value as a string in input () function
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9

if hours > 35:
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else:
    pay = hours * normal_rate

print(f'This weekly payment is: {pay}')

import yfinance

start = '2020-01-01'
end = None

tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

