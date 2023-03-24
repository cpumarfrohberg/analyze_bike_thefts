<h1 align="center">Analyze bike thefts in Berlin.</h1>
<p align="center">Project Description</p>
This project has the main objective to analyze bike thefts in Berlin, including an example dashboard of what a later deployment could look like. It includes data reported by the Berlin Police Department here: https://www.internetwache-polizei-berlin.de/vdb/Fahrraddiebstahl.csv and spans over the time period between January first 2022 and February 19th, 2023.

## Content of the project
* 1. data directory
* 2. `utils.py`: define classes for data transformation and plotting
* 3. `app.py` (`streamlit` app)
* 4. `transform.py`: transform data for running analysis 
* 4. `requirements.txt`

## For running the analysis in designated environment
- clone repo locally
- run `transform.py`for transforming data and using transformed data for example dashboard
- create an environment with the contents of the requirements.txt file (if you are using conda: install pip first via "conda install pip" and then "pip install -r requirements.txt")
- run `streamlit run app.py` for seeing an example dashboard for the analysis.

## For running the app in a docker container
- clone repo locally
- build image with
`docker build -t streamlitchurnapp:latest -f docker/Dockerfile .`
- run image with
`docker run -p 8501:8501 streamlitchurnapp:latest`
- in your web browser: map your localhost to port 8501 in container

## Next steps
- [ ] extract population data for each district and concatenate it with current version of transformed data in order to normalize bike thefts' counts
- [ ] plot data with interactive map
- [ ] extract weather data in order concatenate it with current version of transformed data
- [ ] predict number of bike thefts with an ensemble model
- [ ] forecast number of bike thefts with time series (e.g. `AR`) model
- [ ] predict number of bike thefts with ensemble method (e.g. `RandomForest`) model

## Author

**Carlos Pumar-Frohberg**

- [Profile](https://github.com/cpumarfrohberg)
- [Email](mailto:cpumarfrohberg@gmail.com?subject=Hi "Hi!")


## 🤝 Support

Comments, questions and/or feedback are welcome!
