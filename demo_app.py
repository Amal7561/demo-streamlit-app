import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt 
import requests
from streamlit_lottie import st_lottie
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg 
from matplotlib.figure import Figure

st.set_page_config(layout="wide")
sns.set_style("darkgrid")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def load_lottieurl(url: str): 
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json() 

lottie_amazon = load_lottieurl(
    "https://assets6.lottiefiles.com/private_files/lf30_zERHJg.json" 
)
st_lottie(lottie_amazon, speed=1, height=200, key="initial")

matplotlib.use("agg")
matplotlib.rcParams.update({"font.size": 14}) 
_lock = RendererAgg.lock
sns.set_style("darkgrid")

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (0.1, 2, 0.2, 1, 0.1)
)

row0_1.title("Analyzing Your LinkedIn Competitors")

with row0_2:
    st.write("")

row0_2.subheader("A Web App by [Team LegalEase](https://www.linkedin.com/company/legalease-solutions-llc)")

row1_spacer1, row1_1, row1_spacer2 = st.columns((0.1, 3.2, 0.1))

with row1_1:
    """
    Hey there! Introducing LinkedIn Competitor Analyzer: Unlock Your Professional Edge

    Introducing our revolutionary web application designed specifically for ambitious businesses like yours 
    With Competitor Analyzer, you gain the upper hand in understanding and analyzing your LinkedIn competitors, enabling you to make data-driven decisions and propel your business forward.
        
    Here's what makes Competitor Analyzer the ultimate tool for your daily business operations:
        Comprehensive Competitor Insights,
        Advanced Analytics,
        Real-Time Monitoring,
        Benchmarking and Comparison,
        Customized Reporting,
        User-Friendly Interface & 
        Data Privacy and Security. 

    🔥 Unleash the Power of Data: With Competitor Smackdown, you'll tap into a treasure trove of competitor insights like never before. It's like having a secret spy agent gathering intelligence on your adversaries 24/7. Get the upper hand with comprehensive data on their strategies, strengths, weaknesses, and more!

    💡 Battle-Ready Analytics: Leave no stone unturned! Competitor Smackdown arms you with powerful analytics capabilities that are nothing short of a superpower. Discover hidden patterns, unearth valuable trends, and identify the key moves that will make you the undisputed champion of your industry!

    🕐 Real-Time Rumble: Picture this: You're in the ring, gloves on, adrenaline pumping. That's the experience Competitor Smackdown brings you with its real-time monitoring feature. Stay in the loop with lightning-fast updates on your opponents' LinkedIn profiles, job postings, content engagement, and network growth. With this agility, you'll always be one step ahead!

    📈 KO-worthy Benchmarking: It's time to show off your strength! Competitor Smackdown lets you measure your business's performance against your foes, unleashing your inner Rocky Balboa. Identify areas where you're pummeling the competition and discover opportunities for improvement that will send them crashing to the canvas!

    📊 Jaw-Dropping Reports: Say goodbye to boring spreadsheets and hello to knockout presentations! Competitor Smackdown brings you customized reports that pack a punch. Stunning visuals, eye-catching metrics, and jaw-dropping insights will make you the hero of every boardroom meeting. Your colleagues won't know what hit them!

    🎮 User-Friendly Showdown: No need to be a heavyweight champion to use our web application! Competitor Smackdown's user-friendly interface will have you throwing punches like a pro in no time. Access and analyze data with ease, saving you precious time to focus on delivering the knockout blows your business needs.

    🔒 Ironclad Security: We take your data security seriously, so you can fight with confidence. Competitor Smackdown is built on an impenetrable fortress of privacy, ensuring your sensitive information stays locked down tighter than a championship belt.

    **To begin, please download [Here](https://www.linkedin.com/company/117133/admin/analytics/competitors/). Unlock the power of data-driven decision-making and gain a competitive advantage with Competitor Analyzer. 
    Seamlessly integrate it into your daily routine and experience the transformative impact it can have on your business's growth and success.
    Don't miss out on this opportunity to revolutionize the way you analyze your LinkedIn competitors. Get started with Competitor Analyzer today and embark on a journey towards outpacing your competition.**
    """ 

# Define a function to load the CSV file
def load_csv(file):
    return pd.read_csv(file, header=1) 

# Set page configuration
# st.set_page_config(layout="wide")  cd 

# Add a file uploader widget
file = st.file_uploader("Upload CSV file", type=["csv"]) 

# Check if a file is uploaded
if file is not None:
    # Load the CSV file
    df = load_csv(file) 

    # Data Cleaning
    df['Page'] = df['Page'].astype(str)
    df['Total Followers'] = df['Total Followers'].astype(int)
    df['New Followers'] = df['New Followers'].astype(int)
    df['Total post engagements'] = df['Total post engagements'].astype(int)
    df['Total post reactions'] = df['Total post reactions'].astype(int)
    df['Total post comments'] = df['Total post comments'].astype(int)
    df['Total reposts'] = df['Total reposts'].astype(int)
    df['Total posts'] = df['Total posts'].astype(int) 
    
    
    
    # Sort the DataFrame by 'Total Followers' and 'New Followers' in descending order
    
#_____________________________________________________________________________________________________________
    
    # Create the figures and axes for the bar plots
    fig1, ax1 = plt.subplots(figsize=(9, 5), dpi=900) 
    fig2, ax2 = plt.subplots(figsize=(9, 5), dpi=900)
    fig3, ax3 = plt.subplots(figsize=(9, 5), dpi=900)
    fig4, ax4 = plt.subplots(figsize=(9, 5), dpi=900)
    fig5, ax5 = plt.subplots(figsize=(9, 5), dpi=900)
    fig6, ax6 = plt.subplots(figsize=(9, 5), dpi=900)
    fig7, ax7 = plt.subplots(figsize=(9, 5), dpi=900)
    
    # Create bar plots for 'Total Followers' and 'New Followers' 
#1    
    df.sort_values(by=['Total Followers'], ascending=True, inplace=True)
    sns.barplot(data=df, x='Page', y='Total Followers', palette='viridis', ax=ax1)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
    ax1.set_xlabel('Page')
    ax1.set_ylabel('Total Followers') 
    ax1.set_title('Page vs Total Followers')
#2  
    df.sort_values(by=['New Followers'], ascending=True, inplace=True)
    sns.barplot(data=df, x='Page', y='New Followers', palette='magma', ax=ax2)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
    ax2.set_xlabel('Page')
    ax2.set_ylabel('New Followers')
    ax2.set_title('Page vs New Followers')
#3    
    df.sort_values(by=['Total post engagements'], ascending=True, inplace=True)
    sns.barplot(data=df, x='Page', y='Total post engagements', palette='YlGnBu', ax=ax3)
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=90)
    ax3.set_xlabel('Page')
    ax3.set_ylabel('Total post engagements')
    ax3.set_title('Page vs Total post engagements')
#4   
    df.sort_values(by=['Total post reactions'], ascending=True, inplace=True)
    sns.barplot(data=df, x='Page', y='Total post reactions', palette='Purples', ax=ax4)
    ax4.set_xticklabels(ax4.get_xticklabels(), rotation=90)
    ax4.set_xlabel('Page')
    ax4.set_ylabel('Total post reactions')
    ax4.set_title('Page vs Total post reactions')
#5  
    df.sort_values(by=['Total post comments'], ascending=True, inplace=True) 
    sns.barplot(data=df, x='Page', y='Total post comments', palette='Oranges', ax=ax5)
    ax5.set_xticklabels(ax5.get_xticklabels(), rotation=90)
    ax5.set_xlabel('Page')
    ax5.set_ylabel('Total post comments')
    ax5.set_title('Page vs Total post comments')
#6  
    df.sort_values(by=['Total reposts'], ascending=True, inplace=True) 
    sns.barplot(data=df, x='Page', y='Total reposts', palette='BuGn', ax=ax6)
    ax6.set_xticklabels(ax6.get_xticklabels(), rotation=90)
    ax6.set_xlabel('Page')
    ax6.set_ylabel('Total Total reposts')
    ax6.set_title('Page vs Total reposts')
    
#7  
    df.sort_values(by=['Total posts'], ascending=True, inplace=True) 
    sns.barplot(data=df, x='Page', y='Total posts', palette='BuGn', ax=ax7) 
    ax7.set_xticklabels(ax6.get_xticklabels(), rotation=90)
    ax7.set_xlabel('Page')
    ax7.set_ylabel('Total posts')
    ax7.set_title('Page vs Total posts') 

    # Add data labels to the bar plots 
    for p1 in ax1.patches:
        ax1.annotate(int(p1.get_height()), (p1.get_x() + p1.get_width() / 4., p1.get_height()),
                     ha='center', va='center', xytext=(0, 3), textcoords='offset points', fontsize=13)
        
    for p2 in ax2.patches:
        ax2.annotate(int(p2.get_height()), (p2.get_x() + p2.get_width() / 4., p2.get_height()),
                     ha='center', va='center', xytext=(0, 3), textcoords='offset points', fontsize=13)
        
    for p3 in ax3.patches:
        ax3.annotate(int(p3.get_height()), (p3.get_x() + p3.get_width() / 4., p3.get_height()),
                     ha='center', va='center', xytext=(0, 3), textcoords='offset points', fontsize=13)
        
    for p4 in ax4.patches:
        ax4.annotate(int(p4.get_height()), (p4.get_x() + p4.get_width() / 4., p4.get_height()),
                     ha='center', va='center', xytext=(0, 3), textcoords='offset points', fontsize=13)
        
    for p5 in ax5.patches:
        ax5.annotate(int(p5.get_height()), (p5.get_x() + p5.get_width() / 4., p5.get_height()),
                     ha='center', va='center', xytext=(0, 3), textcoords='offset points', fontsize=13)
        
    for p6 in ax6.patches:
        ax6.annotate(int(p6.get_height()), (p6.get_x() + p6.get_width() / 4., p6.get_height()),
                     ha='center', va='center', xytext=(0, 3), textcoords='offset points', fontsize=13)
    
    for p7 in ax7.patches:
        ax7.annotate(int(p7.get_height()), (p7.get_x() + p7.get_width() / 4., p7.get_height()),
                     ha='center', va='center', xytext=(0, 3), textcoords='offset points', fontsize=13)
        
#___________________________________________________________________________________________________________
    
    # Display the figures and associated text
    st.write("## **Breaking Down in Report**")
    st.write("-------------------")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.pyplot(fig1)
        st.write("Understand the Purpose: Identify the purpose of the bar chart and what data it represents, such as comparisons, trends, or distributions.")
    
    with col2:
        st.pyplot(fig2)
        st.write("Read Axes and Labels: Examine the y-axis for data values and the x-axis for categories or time periods to understand the scale and context of the data.")
    
    col3, col4 = st.columns(2)

    with col3:
        st.pyplot(fig3)
        st.write("Interpret Bar Height: Analyze the height of each bar, as it represents the value or quantity of data for a specific category or time period.")
    
    with col4:
        st.pyplot(fig4)
        st.write("Compare and Identify Patterns: Compare the bar heights to identify relationships between categories and observe any trends or patterns in the data.")
        
    col5, col6 = st.columns(2)

    with col5:
        st.pyplot(fig5)
        st.write("Use Data Labels and Legend: Check for data labels on or above the bars to get precise numerical information, and refer to the legend for color or pattern meanings if the chart includes multiple data series.") 
    
    with col6:
        st.pyplot(fig6)
        st.write("Understand the Purpose: Identify the purpose of the bar chart and what data it represents, such as comparisons, trends, or distributions.")
        
    col7,col8 = st.columns(2)
    
    with col7:
         st.pyplot(fig7)
         st.write("Practice and familiarize yourself with various types of bar charts to build proficiency.")
     
     #with col6:
         #st.pyplot(fig6)
         #st.write(
             #"For me, this graph was useful because I could see two big upticks, once when I graduated high")
