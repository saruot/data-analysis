import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import variables

men_total = variables.men_total
women_total = variables.women_total
men_bench = variables.men_bench
women_bench = variables.women_bench
men_total_50kg = variables.men_total_50kg
women_total_50kg = variables.women_total_50kg
men_total_100kg = variables.men_total_100kg
women_total_100kg = variables.women_total_100kg
men_total_IPF = variables.men_total_IPF
men_total_WPC = variables.men_total_WPC
filtered_data = variables.filtered_data

st.title("Powerlifting Analysis")

# Sidebar to select the analysis task
analysis_task = st.sidebar.selectbox("Select Analysis Task", ["Men vs. Women TotalKg", "Men vs. Women Bench Press", "Men vs. Women by Bodyweight", "Men in IPF vs. WPC", "Lifter Country Impact"])

# Visualize data distributions
if analysis_task == "Men vs. Women TotalKg":
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=men_total, name="Men"))
    fig.add_trace(go.Histogram(x=women_total, name="Women"))
    fig.update_layout(barmode='overlay', title="TotalKg Distribution (Men vs. Women)")
    st.plotly_chart(fig)

if analysis_task == "Men vs. Women Bench Press":
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=men_bench, name="Men"))
    fig.add_trace(go.Histogram(x=women_bench, name="Women"))
    fig.update_layout(barmode='overlay', title="Bench Distribution (Men vs. Women)")
    st.plotly_chart(fig)    

if analysis_task == "Men vs. Women by Bodyweight":
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=men_total_50kg, name="Men 50-55kg"))
    fig.add_trace(go.Histogram(x=women_total_50kg, name="Women 50-55kg"))
    fig.add_trace(go.Histogram(x=men_total_100kg, name="Men 100-105kg"))
    fig.add_trace(go.Histogram(x=women_total_100kg, name="Women 100-105kg"))
    fig.update_layout(barmode='overlay', title="Total weight lifted in different weight classes (Men vs. Women)")
    st.plotly_chart(fig) 

if analysis_task == "Men in IPF vs. WPC":
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=men_total_IPF, name="IPF"))
    fig.add_trace(go.Histogram(x=men_total_WPC, name="WPC"))
    fig.update_layout(barmode='overlay', title="Mens totals in IPF vs. WPC")
    st.plotly_chart(fig) 

if analysis_task == "Lifter Country Impact":
    fig = px.histogram(filtered_data, x="Country", y="TotalKg", title="Weight lifted sorted by country", 
                  labels={"TotalKg": "Total Weight Lifted (kg)"}, histfunc="sum")
    st.plotly_chart(fig)  

# Perform statistical tests and display results
if analysis_task == "Men vs. Women TotalKg":
    t_stat, p_value = stats.ttest_ind(men_total, women_total)
    alpha = 0.05
    if p_value < alpha:
        st.write("Hypothesis 1: Men lift more than women (TotalKg) is supported.")
    else:
        st.write("Hypothesis 1: Men lift more than women (TotalKg) is not supported")

if analysis_task == "Men vs. Women Bench Press":
    t_stat, p_value = stats.ttest_ind(men_total, women_total)
    alpha = 0.05
    if p_value < alpha:
        st.write("Hypothesis 2: Men bench press more than women is supported.")
    else:
        st.write("Hypothesis 2: Men bench press more than women is not supported.")

if analysis_task == "Men vs. Women by Bodyweight":
    t_stat1, p_value1 = stats.ttest_ind(men_total_50kg, women_total_50kg)
    t_stat2, p_value2 = stats.ttest_ind(men_total_100kg, women_total_100kg)
    alpha = 0.05  
    if p_value1 < alpha:
        st.write("Hypothesis 3: Men lift more than women in the 50-55kg bodyweight range is supported.")
    else:
        st.write("Hypothesis 3: Men lift more than women in the 50-55kg bodyweight range is not supported.")

    if p_value2 < alpha:
        st.write("Hypothesis 4: Men lift more than women in the 100-105kg bodyweight range is supported.")
    else:
        st.write("Hypothesis 4: Men lift more than women in the 100-105kg bodyweight range is not supported.")

if analysis_task == "Men in IPF vs. WPC":
    t_stat, p_value = stats.ttest_ind(men_total_IPF, men_total_WPC)
    alpha = 0.05
    if p_value < alpha:
        st.write("Hypothesis 5: Men lift more in IPF than in WPC is supported.")
    else:
        st.write("Hypothesis 5: Men lift more in IPF than in WPC is not supported.")
    
if analysis_task == "Lifter Country Impact":
    model = ols('TotalKg ~ Country', data=filtered_data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    alpha = 0.05  
    p_value = anova_table['PR(>F)'][0]
    if p_value < alpha:
        st.write("Hypothesis 6: Lifter country affects TotalKg is supported. There is a significant difference in TotalKg among countries.")
    else:
        st.write("Hypothesis 6: Lifter country affects TotalKg is not supported. There is no significant difference in TotalKg among countries.")


st.sidebar.write("Switch between tasks to view results and visualizations.")