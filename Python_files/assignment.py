import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import plotly.express as px
from scipy import stats
import variables

# Most of the data-analysis work is included in the notebook. This assignment.py was created for the streamlit 
# framework. The variables.py was created for lighten the load on the application, due to the large data size
# though this can also be fault of the use not being familiar with the environment, but regardless it seemed to work.


filtered_data = variables.filtered_data

st.title("Powerlifting Analysis")

analysis_task = st.sidebar.selectbox("Select Analysis Task", ["Men vs. Women TotalKg", "Men vs. Women Bench Press", "Men vs. Women by Bodyweight", "Men in IPF vs. WPC", "Lifter Country Impact"])

if analysis_task == "Men vs. Women TotalKg":
    men_total = variables.men_total
    women_total = variables.women_total
    
    # Create histograms for TotalKg
    st.markdown("#### Task 1 - TotalKg Comparison")
    
    # Create a Streamlit figure for plotting
    fig = plt.figure(figsize=(10, 6))
    
    # Plot using seaborn (but show it within Streamlit)
    sns.histplot(men_total, kde=True, label='Men')
    sns.histplot(women_total, kde=True, label='Women')
    plt.title("TotalKg Comparison")
    plt.xlabel("TotalKg")
    plt.legend()
    
    # Show the figure in Streamlit
    st.pyplot(fig)
    
    st.write(f"Men's Mean TotalKg: {men_total.mean()}")
    st.write(f"Women's Mean TotalKg: {women_total.mean()}")
    
    # Perform a t-test
    t_stat, p_value = stats.ttest_ind(men_total, women_total)
    st.write("t-statistic:", t_stat)
    st.write("p-value:", p_value)
    
    alpha = 0.05
    if p_value < alpha:
        st.write("Hypothesis 1: Men lift more than women (TotalKg) is supported.")
    else:
        st.write("Hypothesis 1: Men lift more than women (TotalKg) is not supported.")

elif analysis_task == "Men vs. Women Bench Press":
    men_bench = variables.men_bench
    women_bench = variables.women_bench
    
    # Create histograms for Bench Press
    st.markdown("#### Task 2 - Bench Press Comparison")
    
    # Create a Streamlit figure for plotting
    fig = plt.figure(figsize=(10, 6))
    
    # Plot using seaborn (but show it within Streamlit)
    sns.histplot(men_bench, kde=True, label='Men')
    sns.histplot(women_bench, kde=True, label='Women')
    plt.title("Bench Press Comparison")
    plt.xlabel("Bench Press")
    plt.legend()
    
    # Show the figure in Streamlit
    st.pyplot(fig)
    
    st.write(f"Men's Mean Bench Press: {men_bench.mean()}")
    st.write(f"Women's Mean Bench Press: {women_bench.mean()}")
    
    # Perform a t-test
    t_stat, p_value = stats.ttest_ind(men_bench.dropna(), women_bench.dropna())
    st.write("t-statistic:", t_stat)
    st.write("p-value:", p_value)
    
    alpha = 0.05
    if p_value < alpha:
        st.write("Hypothesis 2: Men bench press more than women is supported.")
    else:
        st.write("Hypothesis 2: Men bench press more than women is not supported.")

elif analysis_task == "Men vs. Women by Bodyweight":
    men_total_50kg = variables.men_total_50kg
    women_total_50kg = variables.women_total_50kg
    men_total_100kg = variables.men_total_100kg
    women_total_100kg = variables.women_total_100kg
    
    # Create histograms for 50-55kg weight class total comparison
    st.markdown("#### Task 3 - 50-55kg Weight Class Total Comparison")
    
    # Create a Streamlit figure for plotting
    fig = plt.figure(figsize=(10, 6))
    
    # Plot using seaborn (but show it within Streamlit)
    sns.histplot(men_total_50kg, kde=True, label='Men')
    sns.histplot(women_total_50kg, kde=True, label='Women')
    plt.title("50-55kg Weight Class Total Comparison")
    plt.xlabel("TotalKg")
    plt.legend()
    
    # Show the figure in Streamlit
    st.pyplot(fig)
    
    st.write(f"Men's Mean TotalKg: {men_total_50kg.mean()}")
    st.write(f"Women's Mean TotalKg: {women_total_50kg.mean()}")
    
    # Perform a t-test
    t_stat, p_value = stats.ttest_ind(men_total_50kg.dropna(), women_total_50kg.dropna())
    st.write("t-statistic:", t_stat)
    st.write("p-value:", p_value)
    
    alpha = 0.05
    if p_value < alpha:
        st.write("Hypothesis 3: Men lift more than women in the 50-55kg bodyweight range is supported.")
    else:
        st.write("Hypothesis 3: Men lift more than women in the 50-55kg bodyweight range is not supported.")

    
    st.markdown("---")


     # Create histograms for 100-105kg weight class total comparison
    st.markdown("#### Task 4 - 100-105kg Weight Class Total Comparison")
    
    # Create a Streamlit figure for plotting
    fig = plt.figure(figsize=(10, 6))
    
    # Plot using seaborn (but show it within Streamlit)
    sns.histplot(men_total_100kg, kde=True, label='Men')
    sns.histplot(women_total_100kg, kde=True, label='Women')
    plt.title("100-105kg Weight Class Total Comparison")
    plt.xlabel("TotalKg")
    plt.legend()
    
    # Show the figure in Streamlit
    st.pyplot(fig)
    
    st.write(f"Men's Mean TotalKg: {men_total_100kg.mean()}")
    st.write(f"Women's Mean TotalKg: {women_total_100kg.mean()}")
    
    # Perform a t-test
    t_stat, p_value = stats.ttest_ind(men_total_100kg.dropna(), women_total_100kg.dropna())
    st.write("t-statistic:", t_stat)
    st.write("p-value:", p_value)
    
    alpha = 0.05
    if p_value < alpha:
        st.write("Hypothesis 4: Men lift more than women in the 100-105kg bodyweight range is supported.")
    else:
        st.write("Hypothesis 4: Men lift more than women in the 100-105kg bodyweight range is not supported.")

elif analysis_task == "Men in IPF vs. WPC":
    men_total_WPC = variables.men_total_WPC
    men_total_IPF = variables.men_total_IPF
    
    # Create a Markdown subheading
    st.markdown("### Task 5 - IPF and WPC Total Comparison")
    
    # Create a Streamlit figure for plotting
    fig = plt.figure(figsize=(10, 6))
    
    # Plot using seaborn (but show it within Streamlit)
    sns.histplot(men_total_WPC, kde=True, label='WPC')
    sns.histplot(men_total_IPF, kde=True, label='IPF')
    plt.title("IPF and WPC Total Comparison")
    plt.xlabel("TotalKg")
    plt.legend()
    
    # Show the figure in Streamlit
    st.pyplot(fig)
    
    # Create another Markdown subheading
    st.markdown("#### Task 5 Results")
    st.write(f"WPC's Mean TotalKg: {men_total_WPC.mean()}")
    st.write(f"IPF's Mean TotalKg: {men_total_IPF.mean()}")
    
    # Perform a t-test
    t_stat, p_value = stats.ttest_ind(men_total_WPC.dropna(), men_total_IPF.dropna())
    
    # Create another Markdown subheading
    st.markdown("#### T-Test Results")
    st.write("t-statistic:", t_stat)
    st.write("p-value:", p_value)
    
    alpha = 0.05
    if p_value < alpha:
        st.write("Hypothesis 5: Men lift more in IPF than in WPC is supported.")
    else:
        st.write("Hypothesis 5: Men lift more in IPF than in WPC is not supported.")


elif analysis_task == "Lifter Country Impact":
    # Create a Markdown subheading
    st.markdown("### Hypothesis 6: Lifter Country Affects TotalKg")
    
    # Perform an ANOVA test to assess the impact of "Country" on "TotalKg"
    model = ols('TotalKg ~ Country', data=filtered_data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    alpha = 0.05  

    p_value = anova_table['PR(>F)'][0]
    
    # Display the ANOVA results
    st.write("ANOVA Results:")
    st.write(anova_table)
    
    if p_value < alpha:
        st.write("Hypothesis 6: Lifter country affects TotalKg is supported. There is a significant difference in TotalKg among countries.")
    else:
        st.write("Hypothesis 6: Lifter country affects TotalKg is not supported. There is no significant difference in TotalKg among countries.")
    
