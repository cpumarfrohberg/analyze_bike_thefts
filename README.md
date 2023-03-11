<h1 align="center">Predicting Customer Churn for a Savings Bank in Peru</h1>
<p align="center">Project Description</p>
This project is based on a cooperation with a Savings Bank ("Caja Municipal de Ahorro y Crédito") in Peru. Its main objective consists in predicting the likelihood that "Small and Medium Enterprise (SME)" clients of the Savings Bank will leave the institution 3 months into the future. 

<img src ="images/CMAC.jpg" width = "100">

* Initial features used can be grouped into three categories:
* 1. socioeconomic features
* 2. variables related to the Loan Officers (LO) attending SME clients and 
* 3. variables related to the so-called "RFM"- methodology often used in practice for classifying customers into different groups. 

* However, and based on model fit of a Random Forest Classifier, the following features resulted as having greatest importance
* 1. employment status of the LO 6 months prior?
* 2. expectations regarding the employment status of the LO 3 months into the future?
* 3. expectation regarding the employment status of the LO 6 months into the future?

## Content of the project
* 1. data directory
* 2. EDA (including feature importance)
* 3. model fit 
* 4. artifacts folder containing pickled model
* 5. `utils.py`
* 6. streamlit app

## For running the models locally in designated environment
- clone repo locally
- create an environment with the contents of the requirements.txt file (if you are using conda: install pip first via "conda install pip" and then "pip install -r requirements.txt")

## For running the app in a docker container
- clone repo locally
- build image with
`docker build -t streamlitchurnapp:latest -f docker/Dockerfile .`
- run image with
`docker run -p 8501:8501 streamlitchurnapp:latest`
- in your web browser: map your localhost to port 8501 in container


## Future Updates
- [ ] Feature engineer for retraining `Logistic Regression`
- [ ] train a model based on predictive features for churn of **Loan Officers** (instead of clients themselves)

## Author

**Carlos Pumar-Frohberg**

- [Profile](https://github.com/cpumarfrohberg)
- [Email](mailto:cpumarfrohberg@gmail.com?subject=Hi "Hi!")


## 🤝 Support

Comments, questions and/or feedback are welcome!
