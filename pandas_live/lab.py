import pandas as pd
import pandas_alive

elec_df = pd.read_csv("./assignment_mle.csv",thousands=',')

elec_df.fillna(0).plot_animated('examples/example-electricity-generated-australia.gif',period_fmt="%Y",
                                title='Australian Electricity Generation Sources 1980-2018', kind='line')
