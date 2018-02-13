
## Heroes of Pymoli Data Anaysis
- Out of the total population of 573 players, a significant majority of the players are male (81%). Although females are a much smaller segment of the population, they still comprise of one fifth of players (18%).
- The largest purchasing age demographic are players that fall in the 20-24 age range (305 purchases), while the smallest purchasing age demographic are players in the 40+ age range (3 purchases). 
- The most popular games, "Betrayal, Whisper of Grieving Widows" and "Arcane Gem," were both purchased 11 times each, while "Retribution Axe" was the most profitable game (total purchase value of $37.26). Further, there was no overlap between the top5 most popular games and the top 5 most profitable games.



```python
import pandas as pd
import numpy as np
import os
```


```python
# import and read the json purchase data file 
purchase_data = os.path.join('Resources','purchase_data.json')

purchase_data_df = pd.read_json(purchase_data)

```


```python
# Player Count
# Total Number of Players
total_unique_players = purchase_data_df["SN"].nunique()

## Output
total_players_df = pd.DataFrame([{"Total Players": total_unique_players}])
total_players_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Purchasing Analysis (Total)
# Number of Unique Items
num_unique_items = purchase_data_df["Item ID"].nunique()

# Average Purchase Price
avg_purchase_price = purchase_data_df["Price"].mean()
avg_purchase_price = np.round(avg_purchase_price, 2)

# Total Number of Purchases
total_num_purchases = purchase_data_df["Price"].count()


# Total Revenue
total_revenue = purchase_data_df["Price"].sum()
total_revenue = np.round(total_revenue, 2)

# Create data frame
purchasing_analysis = pd.DataFrame([{"Number of Unique Items": num_unique_items, 
                                     "Average Purchase Price": avg_purchase_price,
                                     "Total Number of Purchases": total_num_purchases,
                                     "Total Revenue": total_revenue
                                    }])

# Format dataframe
purchasing_analysis["Average Purchase Price"] = purchasing_analysis["Average Purchase Price"].map("${:,.2f}".format)
purchasing_analysis["Total Revenue"] = purchasing_analysis["Total Revenue"].map("${:,.2f}".format)

purchasing_analysis = purchasing_analysis.loc[:, ["Number of Unique Items", "Average Purchase Price", "Total Number of Purchases", "Total Revenue"]]

## Output
purchasing_analysis
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Purchase Price</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Gender Demographics

# Percentage and Count of Male Players
unique_players = purchase_data_df.loc[:, ["Gender", "SN", "Age"]]
unique_players = unique_players.drop_duplicates()
total_player_count = unique_players.count()["SN"]

male_count = unique_players[unique_players["Gender"]=="Male"].count()["Gender"]
male_percentage = (male_count/total_player_count) * 100
male_percentage = np.round(male_percentage, 2)

# Percentage and Count of Female Players
female_count = unique_players[unique_players["Gender"]=="Female"].count()["Gender"]
female_percentage = (female_count/total_player_count) * 100
female_percentage = np.round(female_percentage, 2)

# Percentage and Count of Other / Non-Disclosed
other_count = unique_players[(unique_players["Gender"]!="Female") & (unique_players["Gender"]!="Male")].count()["Gender"]
other_percentage = (other_count/total_player_count) * 100
other_percentage = np.round(other_percentage, 2)

## Output report
gender_demographics = pd.DataFrame({"Percentage of Players": [male_percentage, female_percentage, other_percentage], 
                                    "Total Count": [male_count, female_count, other_count],
                                    "Gender": ["Male", "Female", "Other / Non-Disclosed"]
                                   })

gender_demographics = gender_demographics.set_index("Gender")
gender_demographics.index.name = None 
gender_demographics

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Purchasing Analysis (Gender)
## The below each broken by gender:

# Purchase Count
male_pur_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Male"]
female_pur_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Female"]
other_pur_df = purchase_data_df.loc[(purchase_data_df["Gender"]!="Female") & (purchase_data_df["Gender"]!="Male")]

male_pur_count = male_pur_df["Price"].count()
female_pur_count= female_pur_df["Price"].count()
other_pur_count = other_pur_df["Price"].count()

# Average Purchase Price
male_avg_price = np.round((male_pur_df["Price"].mean()),2)
female_avg_price = np.round((female_pur_df["Price"].mean()),2)
other_avg_price = np.round((other_pur_df["Price"].mean()),2)

# Total Purchase Value
total_male_pur_value = male_pur_df["Price"].sum()
total_female_pur_value = female_pur_df["Price"].sum()
total_other_pur_value = other_pur_df["Price"].sum()

# Normalized Totals
total_male_normal = np.round((total_male_pur_value / male_count), 2)
total_female_normal = np.round((total_female_pur_value / female_count), 2)
total_other_normal = np.round((total_other_pur_value / other_count), 2)

# Create dataframe from above variables/calculations
pur_analysis_gen = pd.DataFrame({"Purchase Count": [male_pur_count, female_pur_count, other_pur_count], 
                                    "Average Purchase Price": [male_avg_price, female_avg_price, other_avg_price],
                                    "Total Purchase Value": [total_male_pur_value, total_female_pur_value, total_other_pur_value],
                                    "Normalized Total": [total_male_normal, total_female_normal, total_female_normal],
                                    "Gender": ["Male", "Female", "Other / Non-Disclosed"]
                                   })

pur_analysis_gen = pur_analysis_gen.set_index("Gender")

# Format dataframe 
pur_analysis_gen["Average Purchase Price"] = pur_analysis_gen["Average Purchase Price"].map("${:,.2f}".format)
pur_analysis_gen["Total Purchase Value"] = pur_analysis_gen["Total Purchase Value"].map("${:,.2f}".format)
pur_analysis_gen["Normalized Total"] = pur_analysis_gen["Normalized Total"].map("${:,.2f}".format)

pur_analysis_gen = pur_analysis_gen.loc[:, ["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Total"]]

## Output 
pur_analysis_gen
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Total</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$3.83</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Age Demographics
# The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)

#---create bins, bin names, and relevant grouping
bins = [0, 10, 15, 20, 25, 30, 35, 40, 45]
bin_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

age_pur_df = pd.DataFrame(purchase_data_df)
age_pur_df["Age Range"] = pd.cut(age_pur_df["Age"], bins, labels = bin_names)

age_group = age_pur_df.groupby("Age Range")

#--- find # of unique players per age bin
age_group_unique = pd.DataFrame(unique_players)
age_group_unique["Age Range"] = pd.cut(age_pur_df["Age"], bins, labels = bin_names)
age_group_unique = age_group_unique.groupby("Age Range")
age_group_vcount = age_group_unique["Age Range"].value_counts()
#print(age_group_vcount)

# Purchase Count
age_group_count = age_group["Price"].count()

pur_count_bin0 = age_group_count[0]
pur_count_bin1 = age_group_count[1]
pur_count_bin2 = age_group_count[2]
pur_count_bin3 = age_group_count[3]
pur_count_bin4 = age_group_count[4]
pur_count_bin5 = age_group_count[5]
pur_count_bin6 = age_group_count[6]
pur_count_bin7 = age_group_count[7]

# Average Purchase Price
age_group_avg_pur = age_group["Price"].mean()

avg_pur_bin0 = np.round(age_group_avg_pur[0], 2)
avg_pur_bin1 = np.round(age_group_avg_pur[1], 2)
avg_pur_bin2 = np.round(age_group_avg_pur[2], 2)
avg_pur_bin3 = np.round(age_group_avg_pur[3], 2)
avg_pur_bin4 = np.round(age_group_avg_pur[4], 2)
avg_pur_bin5 = np.round(age_group_avg_pur[5], 2)
avg_pur_bin6 = np.round(age_group_avg_pur[6], 2)
avg_pur_bin7 = np.round(age_group_avg_pur[7], 2)

# Total Purchase Value
total_group_pur = age_group["Price"].sum()

total_pur_bin0 = total_group_pur[0]
total_pur_bin1 = total_group_pur[1]
total_pur_bin2 = total_group_pur[2]
total_pur_bin3 = total_group_pur[3]
total_pur_bin4 = total_group_pur[4]
total_pur_bin5 = total_group_pur[5]
total_pur_bin6 = total_group_pur[6]
total_pur_bin7 = total_group_pur[7]

#print(total_pur_bin2/pur_count_bin2)

# Normalized Totals
total_normal_bin0 = np.round((total_pur_bin0 / age_group_vcount[0]), 2)
total_normal_bin1 = np.round((total_pur_bin1 / age_group_vcount[1]), 2)
total_normal_bin2 = np.round((total_pur_bin2 / age_group_vcount[2]), 2)
total_normal_bin3 = np.round((total_pur_bin3 / age_group_vcount[3]), 2)
total_normal_bin4 = np.round((total_pur_bin4 / age_group_vcount[4]), 2)
total_normal_bin5 = np.round((total_pur_bin5 / age_group_vcount[5]), 2)
total_normal_bin6 = np.round((total_pur_bin6 / age_group_vcount[6]), 2)
total_normal_bin7 = np.round((total_pur_bin7 / age_group_vcount[7]), 2)

# Create dataframe based on above variables/calculations
age_demographics = pd.DataFrame({"Purchase Count": [pur_count_bin0, pur_count_bin1,pur_count_bin2,pur_count_bin3,pur_count_bin4,pur_count_bin5,pur_count_bin6, pur_count_bin7], 
                                    "Average Purchase Price": [avg_pur_bin0, avg_pur_bin1, avg_pur_bin2, avg_pur_bin3, avg_pur_bin4, avg_pur_bin5, avg_pur_bin6, avg_pur_bin7],
                                    "Total Purchase Value": [total_pur_bin0, total_pur_bin1, total_pur_bin2, total_pur_bin3, total_pur_bin4, total_pur_bin5, total_pur_bin6, total_pur_bin7],
                                    "Normalized Total": [total_normal_bin0, total_normal_bin1, total_normal_bin2, total_normal_bin3, total_normal_bin4, total_normal_bin5, total_normal_bin6, total_normal_bin7],
                                    "Bins": bin_names
                                   })


age_demographics = age_demographics.set_index("Bins")
age_demographics.index.name = None 

# Format dataframe
age_demographics["Average Purchase Price"] = age_demographics["Average Purchase Price"].map("${:,.2f}".format)
age_demographics["Total Purchase Value"] = age_demographics["Total Purchase Value"].map("${:,.2f}".format)
age_demographics["Normalized Total"] = age_demographics["Normalized Total"].map("${:,.2f}".format)

age_demographics = age_demographics.loc[:, ["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Total"]]

#output
age_demographics

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>78</td>
      <td>$2.87</td>
      <td>$224.15</td>
      <td>$4.15</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>184</td>
      <td>$2.87</td>
      <td>$528.74</td>
      <td>$3.80</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>305</td>
      <td>$2.96</td>
      <td>$902.61</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>76</td>
      <td>$2.89</td>
      <td>$219.82</td>
      <td>$4.23</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>58</td>
      <td>$3.07</td>
      <td>$178.26</td>
      <td>$4.05</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>44</td>
      <td>$2.90</td>
      <td>$127.49</td>
      <td>$5.10</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>3</td>
      <td>$2.88</td>
      <td>$8.64</td>
      <td>$2.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Top Spenders
## Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
# SN
# Purchase Count
# Average Purchase Price
# Total Purchase Value

##-----

# Create initial variables and perform basic calculations
user_total = purchase_data_df.groupby(["SN"]).sum()["Price"]
user_avg = purchase_data_df.groupby(["SN"]).mean()["Price"]
user_count = purchase_data_df.groupby(["SN"]).count()["Price"]

# Create dataframe based on above variables/calculations
user_data = pd.DataFrame({"Total Purchase Value": user_total, 
                          "Average Purchase Price": user_avg, 
                          "Purchase Count": user_count})

# Post-dataframe formatting
user_data["Average Purchase Price"] = user_data["Average Purchase Price"].map("${:,.2f}".format)
user_data["Total Purchase Value"] = user_data["Total Purchase Value"].map("${:,.2f}".format)

user_data = user_data.loc[:,["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]


## Output Table via sorting data frame on descending Total Purchase Value
user_data.sort_values("Total Purchase Value", ascending=False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Qarwen67</th>
      <td>4</td>
      <td>$2.49</td>
      <td>$9.97</td>
    </tr>
    <tr>
      <th>Sondim43</th>
      <td>3</td>
      <td>$3.13</td>
      <td>$9.38</td>
    </tr>
    <tr>
      <th>Tillyrin30</th>
      <td>3</td>
      <td>$3.06</td>
      <td>$9.19</td>
    </tr>
    <tr>
      <th>Lisistaya47</th>
      <td>3</td>
      <td>$3.06</td>
      <td>$9.19</td>
    </tr>
    <tr>
      <th>Tyisriphos58</th>
      <td>2</td>
      <td>$4.59</td>
      <td>$9.18</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Most Popular Items
## Identify the 5 most popular items by purchase count, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value

##-----

# Extract relevant columns from original data frame
item_data = purchase_data_df.loc[:,["Item ID", "Item Name", "Price"]]

# Create initial variables and perform basic calculations
total_item_pur = item_data.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")
avg_item_pur = item_data.groupby(["Item ID", "Item Name"]).mean()["Price"]
item_count = item_data.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")

# Create new dataframe based on above variable-setting and calculations
item_data_df = pd.DataFrame({"Total Purchase Value": total_item_pur, 
                             "Item Price": avg_item_pur, 
                             "Purchase Count": item_count})

#print(item_data_df["Total Purchase Value"].max())
#print(total_item_pur.max())

# Post-dataframe formatting
item_data_df["Item Price"] = item_data_df["Item Price"].map("${:,.2f}".format)
item_data_df["Total Purchase Value"] = item_data_df["Total Purchase Value"].map("${:,.2f}".format)

item_data_df = item_data_df.loc[:,["Purchase Count", "Item Price", "Total Purchase Value"]]

## Output a table via sorting the item dataframe based on descending Purchase Count
item_data_df.sort_values("Purchase Count", ascending=False).head(5)


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>$1.24</td>
      <td>$11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Most Profitable Items
## Identify the 5 most profitable items by total purchase value, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value

##-----

# Extract relevant columns from original data frame
item_data2 = purchase_data_df.loc[:,["Item ID", "Item Name", "Price"]]

# Create initial variables and perform basic calculations
total_item_pur2 = item_data2.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")
avg_item_pur2 = item_data2.groupby(["Item ID", "Item Name"]).mean()["Price"]
item_count2 = item_data2.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")

# Create new dataframe based on above variable-setting and calculations
item_data_df2 = pd.DataFrame({"Total Purchase Value": total_item_pur2, 
                             "Item Price": avg_item_pur2, 
                             "Purchase Count": item_count2})

# Post-dataframe formatting
item_data_df = item_data_df.loc[:,["Purchase Count", "Item Price", "Total Purchase Value"]]

item_data_profit_df = item_data_df2.sort_values("Total Purchase Value", ascending=False)
item_data_profit_df["Item Price"] = item_data_profit_df["Item Price"].map("${:,.2f}".format)
item_data_profit_df["Total Purchase Value"] = item_data_profit_df["Total Purchase Value"].map("${:,.2f}".format)

## Output a table sorted by descending Total Purchase Value
item_data_profit_df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>$4.14</td>
      <td>9</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>$4.25</td>
      <td>7</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>$4.95</td>
      <td>6</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>$4.87</td>
      <td>6</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>$3.61</td>
      <td>8</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


