# # Downloads Qantas share price beginning 1 January 2020
# import yfinance                                           # (1)
# tic = "QAN.AX"                                            # (2)
# start = '2020-01-01'                                      # (3)
# end = None                                                # (4)
# df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
# print(df)                                                 # (6)
# df.to_csv('qan_prc_2020.csv')                             # (7)

# if __name__ == "__main__":
#     import os
#     import toolkit_config as cfg
#     tic = 'QAN.AX'
#     pth = os.path.join(cfg.DATADIR, 'qan_stk_prc.csv')
#     yf_prc_to_csv(tic, pth)


    def yf_prc_to_csv(tic, pth, start=None, end=None):
        """ Downloads analysts recommendation from Yahoo Finance and saves the
        information in a CSV file

        Parameters
        ----------
        tic : str
            Ticker

        pth : str
            Location of the output CSV file

        start: str, optional
            Download start date string (YYYY-MM-DD)
            If None (the default), start is set to '1900-01-01'

        end: str, optional
            Download end date string (YYYY-MM-DD)
            If None (the default), end is set to the most current date available
        """
        df = yf.download(tic, start=start, end=end)
        df.to_csv(pth)