# Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System

### 1. Abstract
Portfolio management is a behavior that continuously allocates funds to different assets, and adjusts the proportion of funds that should be allocated to each asset in a timely manner according to market conditions. The topic of our project is a visualization system for portfolio management, which is based on my master's thesis: Explainable Uncertainties-based Deep Reinforcement Learning in Portfolio Management. The main purpose is to present the decision-making results of the deep learning model in asset management tasks so that users can monitor the decision made by the model so that users can trust the decision of the model more. When an abnormality occurs in the model, users can directly intervene with their knowledge to achieve expected results such as reducing losses. Because the system requires domain knowledge when an exception occurs, the system is mainly targeted at funding managers.

### 2. How to use the system

Install the requirements of the project
```
pip install -r requirements.txt
```

And then run the main function
```
python app.py
```
### 3. Model structure 
![Architecture of the model](https://github.com/a303990366/Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System/blob/main/Fig/model%20structure.png) 
<p align="center">Fig. 1 Architecture of the model</p>

In our system, we set up a hierarchical model to perform decision-making behavior, which contains several low-level deep reinforcement learning models, which we call local agents, to extract high-level features from the market and provide these features for high-level models. Each local agent only judges a buying or selling signal for one stock, outputs two types of uncertainties: market uncertainty and model uncertainty, which measure market volatility and model robustness, respectively.
In asset management tasks, it is crucial to consider the dependencies between assets. We judge the similarity based on the output of local agents and generate a similarity matrix, which is also provided to the high-level model. The detailed model architecture is shown in Fig. 1.

### 4. Demo
Users can enter the home page after entering their account and password, which is shown in Fig. 2. If the login fails, we will return to the login page.
<div align="center"> <img src="https://github.com/a303990366/Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System/blob/main/Fig/Login_demo.jpg" /></div>
<p align="center">Fig.2 Login Page</p>

The home page (Fig. 3) will be shown after users input the correct account and password. The navigation bar on the left is divided into local agents and global agents. The category of local agents has 4 types of visualization, which contain asset correlation, trading signal, and uncertainty; the category of the global agent has 1 type of visualization, which contains the global decision. 
![Demo of Home Page](https://github.com/a303990366/Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System/blob/main/Fig/dashboard_V3.jpg)
<p align="center">Fig.3 Demo of Home Page</p>

In Fig. 4, we showed the structure of the user interface. This map to our Fig.3's navigation bar.
<div align="center"> <img src="https://github.com/a303990366/Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System/blob/main/Fig/system_structure.png" /></div>
<p align="center">Fig. 4 Structure of User Interface</p>

In the trading signal(Fig. 5), we visualize the buying and selling signals as elements. In this picture, each local agent's overall buying and selling signals in a specific period will be summarized, allowing users to roughly see the summary of each model's buying and selling signals.
![Demo of trading Signal](https://github.com/a303990366/Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System/blob/main/Fig/Trading_signal_demo.jpg)
<p align="center">Fig. 5 Demo of trading Signal</p>
 
In the uncertainty (Fig. 6), we visualize two kinds of uncertainties as elements, in this figure we present the relative uncertainty change of local agents as a heat map.
![Demo of Aleatoric & epistemic uncertainty](https://github.com/a303990366/Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System/blob/main/Fig/Uncertainty_demo.jpg)
<p align="center">Fig.6 Demo of Aleatoric & epistemic uncertainty </p>

In Fig. 7, we visualize asset correlation as an element, and we present the asset correlation matrix as a heat map.
![Demo of Correlation module](https://github.com/a303990366/Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System/blob/main/Fig/Correlation_demo.jpg)
<p align="center">Fig.7 Demo of Correlation module </p>

In decision global agent (Fig.8), when presenting the decision of the high-level model, we expect to present the decision-making behavior of the high-level model in the form of a pie chart.
![Demo of Global Agent's decision](https://github.com/a303990366/Portfolio-Management-Deep-Reinforcement-Learning-Monitor-System/blob/main/Fig/PieChart_demo.jpg)
<p align="center">Fig.8 Demo of Global Agent's decision</p>

### 5. Conclusion:
In this project, we try to build a visualization system based on the results of deep learning models in portfolio management tasks, in order to allow users to understand the model's decision. However, the existing deep learning model is difficult to explain, therefore we divide the problem into several small problems through the hierarchical model. When we find that there is an abnormal situation in the small problem, we can roughly understand the cause of the system error. We try to use the hierarchical architecture to explain model decisions as much as possible, hoping to make users more trustworthy in the decision-making behavior of our system.

Note: Above data is for demo!
