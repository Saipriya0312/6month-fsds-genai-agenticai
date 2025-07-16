import streamlit as st
import seaborn as sns 
import matplotlib.pyplot as plt

sns.set_theme(style= 'whitegrid')

tips = sns.load_dataset('tips')

st.title('Saipriya data visualiza tion app by SEABORN')
st.write('Saipriya A very great AI developer and Data scientist')

#function to create and display plot

def display_plot(title,plot_func):
    st.subheader(title)
    fig , ax =  plt.subplots(figsize = (6,4))
    plot_func(ax=ax)
    st.pyplot(fig)
    plt.close(fig)
    
#To plot the grph

def scatter_plot(ax):
    sns.scatterplot(data=tips,x = 'total_bill',y = 'tip',hue='time',size='size',palette='deep',ax=ax)
    ax.set_title("Scatter plot of total bill vs tip")
    

def line_plot(ax):
    sns.lineplot(data=tips,x = 'size',y = 'total_bill',hue='sex',marker='o',ax=ax)
    ax.set_title("Line plot of total _bill vs gender")
    
def bar_plot(ax):
    sns.barplot(data=tips,x = 'day',y = 'total_bill',hue='sex',palette='muted',ax = ax)
    ax.set_title("Bar plot of total bill bsaed on day")

def box_plot(ax):
    sns.boxplot(data=tips,x= 'day',y ='tip',hue = 'smoker',palette='dark',ax=ax)
    ax.set_title("Box plot of smoker base don day and tip")
    
def violin_plot(ax):
    sns.violinplot(data= tips,y ='total_bill',x = 'day',hue= 'time',split= True,palette='pastel',ax=ax)
    ax.set_title("violin plot of total bill based on day and time")
    
def count_plot(ax):
    sns.countplot(data= tips,x = 'day',hue='smoker',palette= 'dark',ax=ax)
    ax.set_title("count plot of smoker based on tips")
    
def reg_plot(ax):
    sns.regplot(data= tips,x = 'total_bill',y = 'tip',scatter_kws={'s':50},line_kws={'color':'Red'},ax=ax)
    ax.set_title("Regression plot of total bill base don tip")
    
def hist_plot(ax):
    sns.histplot(data = tips,x = 'total_bill',bins= 20,kde=True,color= 'blue',ax=ax)
    ax.set_title("Histogram plot of total bill og tips")
    
def pair_plot(ax):
    pp = sns.pairplot(data = tips, hue='sex', vars=['total_bill', 'tip', 'size'], palette='husl')
    st.pyplot(pp.fig)
    
    
def cat_plot(ax):
    g = sns.catplot(data=tips, x='day', y='tip', hue='sex', palette='bright')
    g.fig.suptitle("cat plot of tip given on day by gender")
    st.pyplot(g.fig)
    
def joint_plot(ax):
    j = sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex', palette='coolwarm', kind='scatter')
    j.fig.suptitle("Joint plot of bill tip given by gender")
    st.pyplot(j.fig)
    
    
def facetGrid(ax):
    g = sns.FacetGrid(tips, col='time', row='smoker', margin_titles=True)
    g.map(sns.histplot, 'total_bill', bins=20, kde=True, color='blue').add_legend()
    g.fig.suptitle("FacetGrid plot of smoker vs time")
    st.pyplot(g.fig)
    
def strip_plot(ax):
    sns.stripplot(data= tips,x = 'day',y = 'tip',hue= 'sex',jitter= True,palette= 'Set1',ax=ax)
    ax.set_title("strip_plot of tip by day based on gender")
    
def kde_plot(ax):
    sns.kdeplot(data = tips,x = 'total_bill',hue = 'sex',fill = True,palette= 'tab10',ax=ax)
    ax.set_title("Kde plot of total bill based on gender")
    
display_plot("Scatter Plot",scatter_plot)
display_plot("Bar plot",bar_plot)
display_plot("Line Plot",line_plot)
display_plot("FacetGrid",facetGrid)
display_plot("kde plot",kde_plot)
display_plot("strip plot",strip_plot)
display_plot("joint plot",joint_plot)
display_plot("cat plot",cat_plot)
display_plot("Paired plot",pair_plot)
display_plot("Histogram plot",hist_plot)
display_plot("Regression plot",reg_plot)
display_plot("Count plot",count_plot)
display_plot("Violin plot",violin_plot)
display_plot("Box plot",box_plot)