# Model Card

## Model Details
* Machine learning model using decision trees for predicting salary, served as an API.

## Intended Use
* Intended use: Just for fun.

## Training Data
* X data = 'age', 'workclass', 'fnlgt', 'education', 'education-num',
       'marital-status', 'occupation', 'relationship', 'race', 'sex',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country'
* y_data = 'salary'
* 26048 entries for training

## Validation Data
* Data consisted of 6513 entries.

## Metrics
Metrics used in this model:
* The precision of this model is 0.7444113263785395
* The recall of this model is 0.6359007001909611
* The fbeta of this model 0.685890834191555

## Ethical Considerations
* Using the model does not pose any ethical consideration. However, it raises some ethical concerns about how minorities generally have less income that caucasicans.

## Caveats and Recommendations
* Model could be improved, but the main objective is to deploy a model using API.
* Folder structure is unclear, but it is how it was provided. 
  * If it was for me I would include a src and put all files there.