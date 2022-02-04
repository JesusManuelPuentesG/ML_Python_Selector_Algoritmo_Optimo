…

# Librería necesaria para utilizar AutoSKLearn con Clasificación
import autosklearn.classification

# Librería necesaria para utilizar AutoSKLearn con Regresión
import autosklearn.regression

…

# Ejemplo de utilización con Clasificación
automl = autosklearn.classification.AutoSklearnClassifier()
    
automl.fit(X, y)
    
y_predicted = automl.predict(X_test)

…