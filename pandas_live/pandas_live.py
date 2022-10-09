#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# # Horizontal Bar Chart Races
# 

# In[1]:


from IPython.core.interactiveshell import InteractiveShell
import warnings
warnings.filterwarnings("ignore")
InteractiveShell.ast_node_interactivity = "all"


# In[2]:


import pandas_alive

covid_df = pandas_alive.load_dataset()


def current_total(values):
    total = values.sum()
    s = f'Total : {int(total)}'
    return {'x': .85, 'y': .2, 's': s, 'ha': 'right', 'size': 11}


covid_df.plot_animated(
    filename='examples/summary-func-example.gif', period_summary_func=current_total)


# In[3]:


from IPython.display import Image
Image(url='examples/summary-func-example.gif')


# In[4]:


import pandas as pd
import pandas_alive

elec_df = pd.read_csv("data/Aus_Elec_Gen_1980_2018.csv",
                      index_col=0, parse_dates=[0], thousands=',')

elec_df.fillna(0).plot_animated('examples/example-electricity-generated-australia.gif', period_fmt="%Y",
                                title='Australian Electricity Generation Sources 1980-2018')


# In[5]:


from IPython.display import Image
Image(url='examples/example-electricity-generated-australia.gif')


# In[6]:


import pandas as pd
import pandas_alive

elec_df = pd.read_csv("data/Aus_Elec_Gen_1980_2018.csv",
                      index_col=0, parse_dates=[0], thousands=',')

elec_df.fillna(0).plot_animated('examples/fixed-example.gif', period_fmt="%Y",
                                title='Australian Electricity Generation Sources 1980-2018', fixed_max=True, fixed_order=True)


# In[7]:


from IPython.display import Image
Image(url='examples/fixed-example.gif')


# In[8]:


import pandas_alive

covid_df = pandas_alive.load_dataset()

covid_df.plot_animated(
    filename='examples/perpendicular-example.gif', perpendicular_bar_func='mean')


# In[9]:


from IPython.display import Image
Image(url='examples/perpendicular-example.gif')


# # Vertical Bar Chart Races
# 

# In[10]:


import pandas_alive

covid_df = pandas_alive.load_dataset()

covid_df.plot_animated(
    filename='examples/example-barv-chart.gif', orientation='v')


# In[11]:


from IPython.display import Image
Image(url='examples/example-barv-chart.gif')


# # Line Charts
# With as many lines as data columns in the DataFrame.

# In[12]:


import pandas_alive

covid_df = pandas_alive.load_dataset()

covid_df.diff().fillna(0).plot_animated(filename='examples/example-line-chart.gif',
                                        kind='line', period_label={'x': 0.25, 'y': 0.9})


# In[13]:


from IPython.display import Image
Image(url='examples/example-line-chart.gif')


# # Bar Charts
# Similar to line charts with time as the x-axis.
# 
# 
# 

# In[15]:


get_ipython().system('pip install tqdm')


# In[16]:


import pandas_alive

covid_df = pandas_alive.load_dataset()

covid_df.sum(axis=1).fillna(0).plot_animated(filename='examples/example-bar-chart.gif', kind='bar',
                                             period_label={'x': 0.1, 'y': 0.9},
                                             enable_progress_bar=True, steps_per_period=2, interpolate_period=True, period_length=200
                                             )


# In[17]:


from IPython.display import Image
Image(url='examples/example-bar-chart.gif')


# # Scatter Charts
# 

# In[18]:


import pandas as pd
import pandas_alive

max_temp_df = pd.read_csv(
    "data/Newcastle_Australia_Max_Temps.csv",
    parse_dates={"Timestamp": ["Year", "Month", "Day"]},
)
min_temp_df = pd.read_csv(
    "data/Newcastle_Australia_Min_Temps.csv",
    parse_dates={"Timestamp": ["Year", "Month", "Day"]},
)

merged_temp_df = pd.merge_asof(max_temp_df, min_temp_df, on="Timestamp")

merged_temp_df.index = pd.to_datetime(
    merged_temp_df["Timestamp"].dt.strftime('%Y/%m/%d'))

keep_columns = [
    "Minimum temperature (Degree C)", "Maximum temperature (Degree C)"]

merged_temp_df[keep_columns].resample("Y").mean().plot_animated(
    filename='examples/example-scatter-chart.gif', kind="scatter", title='Max & Min Temperature Newcastle, Australia')


# In[19]:


from IPython.display import Image
Image(url='examples/example-scatter-chart.gif')


# # Pie Charts
# 

# In[21]:


import pandas_alive

covid_df = pandas_alive.load_dataset()


covid_df.plot_animated(filename='examples/example-pie-chart.gif',
                       kind="pie", rotatelabels=True, period_label={'x': 0, 'y': 0})


# In[22]:


from IPython.display import Image
Image(url='examples/example-pie-chart.gif')


# # Bubble Charts
# Bubble charts are generated from a multi-indexed dataframes. Where the index is the time period (optional) and the axes are defined with x_data_label & y_data_label which should be passed a string in the level 0 column labels.
# 
# See an example multi-indexed dataframe at: https://github.com/JackMcKew/pandas_alive/tree/master/data/multi.csv
# 
# When you set color_data_label= to a df column name, pandas_alive will automatically add a colorbar.
# 
# 

# In[23]:


import pandas_alive

multi_index_df = pd.read_csv("data/multi.csv", header=[0, 1], index_col=0)

multi_index_df


# In[24]:


multi_index_df.index = pd.to_datetime(multi_index_df.index, dayfirst=True)

map_chart = multi_index_df.plot_animated(
    kind="bubble",
    filename="examples/example-bubble-chart.gif",
    x_data_label="Longitude",
    y_data_label="Latitude",
    size_data_label="Cases",
    color_data_label="Cases",
    vmax=5, steps_per_period=3, interpolate_period=True, period_length=500,
    dpi=100
)


# In[25]:


from IPython.display import Image
Image(url='examples/example-bubble-chart.gif')


# # Multiple Charts
# pandas_alive supports multiple animated charts in a single visualisation.
# 
# Create a list of all charts to include in animation
# 
# Use animate_multiple_plots with a filename and the list of charts (this will use matplotlib.subplots)
# 
# Done!

# In[26]:


import pandas_alive

covid_df = pandas_alive.load_dataset()

animated_line_chart = covid_df.diff().fillna(0).plot_animated(
    kind='line', period_label=False, add_legend=False)

animated_bar_chart = covid_df.plot_animated(n_visible=10)

pandas_alive.animate_multiple_plots('examples/example-bar-and-line-chart.gif', [animated_bar_chart, animated_line_chart],
                                    enable_progress_bar=True)


# In[27]:


from IPython.display import Image
Image(url='examples/example-bar-and-line-chart.gif')


# # My data

# In[31]:


import pandas as pd
import pandas_alive
col_list = ["date"  , "Blood colour index",'covid infection probability']
elec_df = pd.read_csv("./assignment_mle.csv",
                      thousands=',', index_col="date",  
                      nrows=100 , 
                      usecols=col_list)

elec_df.columns
elec_df.describe().T

elec_df.head()
elec_df.plot_animated(filename='examples/example-barv-chart_elec_df.gif'
, title='Covid 19')


# In[29]:


from IPython.display import Image
Image(url='./examples/example-barv-chart_elec_df.gif')

