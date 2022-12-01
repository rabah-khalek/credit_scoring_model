import wandb
import credit_scoring_model as model

wandb.login()
wandb.init(project="credit_scoring_model")

# Visualize all classifier plots
wandb.sklearn.plot_classifier(model.clf_logistic_regression,
                              model.X_train,
                              model.X_test,
                              model.Y_train,
                              model.Y_test,
                              model.clf_logistic_regression.predict(model.X_test),
                              model.clf_logistic_regression.predict_proba(model.X_test),
                              model.X_train.columns.values,
                              model_name='credit_scoring_model', feature_names=model.clf_logistic_regression.classes_)
