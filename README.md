# Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System

### 1. Abstract
Portfolio management is a behavior that continuously allocates funds to different assets, and adjusts the proportion of funds that should be allocated to each asset in a timely manner according to market conditions. The topic of our project is a visualization system for portfolio management, which is based on Gary's master's thesis: Explainable Uncertainties-based Deep Reinforcement Learning in Portfolio Management. The main purpose is to present the decision-making results of the deep learning model in asset management tasks so that users can monitor the decision made by the model so that users can trust the decision of the model more. When an abnormality occurs in the model, users can directly intervene with their knowledge to achieve expected results such as reducing losses. Because the system requires domain knowledge when an exception occurs, the system is mainly targeted at funding managers.

### 2. How to use the system
!! Adding installment and cide for performing it

### 3. Model structure 
Fig. 1 architecture of the model
In our system, we set up a hierarchical model to perform decision-making behavior, which contains several low-level deep reinforcement learning models, which we call local agents, to extract high-level features from the market and provide these features for high-level models. Each local agent only judges a buying or selling signal for one stock, and outputs two types of uncertainties: market uncertainty and model uncertainty, which measure market volatility and model robustness, respectively.
In asset management tasks, it is important to consider the dependencies between assets. We judge the similarity based on the output of local agents, and generate a similarity matrix, which is also provided to the high-level model. The detailed model architecture is shown in Fig. 1.

### 4. Demo
Users can enter the home page after entering their account and password. If the login fails, we will return to the login page(fig.2). The home page (fig.3) will be completed in the future. The menu on the left is divided into local agent and global agent, local agent has asset correlation, trading signal and uncertainty, global agent has decision global agent. Structure of user interface shows on fig.4.
  
Fig.2 Login page                     Fig.3 home page
 
Fig. 4 Structure of user interface

	In the trading signal(fig.5), we visualize the buying and selling signals as elements. In this picture, the overall buying and selling signals of each local agent in a specific period will be summarized, allowing users to roughly see the summary of the buying and selling signals of each model. 
Fig.5 trading signal
	In the uncertainty (fig. 6&7), we visualize two kinds of uncertainty as elements, in this figure we present the relative uncertainty change of local agents as a heat map.
 
Fig.6 Aleatoric uncertainty
 
Fig.7 Epistemic uncertainty
In fig.8, we visualize asset correlation as an element, and we present the asset correlation matrix as a heat map.
 
Fig.8
		In decision global agent (Fig.9), when presenting the decision of the high-level model, we expect to present the decision-making behavior of the high-level model in the form of a pie chart.
 
Fig.9 Global Agent

### 5. Conclusion:
In this project, we try to build a visualization system based on the results of deep learning models in portfolio management tasks, in order to allow users to understand the model's decision. However, the existing deep learning model is difficult to explain, therefore we divide the problem into several small problems through the hierarchical model. When we find that there is an abnormal situation in the small problem, we can roughly understand the cause of the system error. We try to use the hierarchical architecture to explain model decisions as much as possible, hoping to make users more trustworthy in the decision-making behavior of our system.
