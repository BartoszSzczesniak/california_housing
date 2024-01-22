from sklearn.base import BaseEstimator, TransformerMixin
from types import FunctionType
from pandas import NA

class OutliersRemover(BaseEstimator, TransformerMixin):
    
    def __init__(self, outliers_config: dict[str, FunctionType], **kwargs) -> None:
        """---
        Tool for removing outliers.

        ## Parameters
        outliers_config: dictionary defining rules to identify outliers. Keys must contain feature names and values must contain filtering functions identifying outliers.
        """

        super().__init__()

        self.outliers_config = outliers_config

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):

        X_mod = X.copy()

        for col, cond in self.outliers_config.items():
            if col in X_mod.columns:
                X_mod.loc[cond, col] = NA

        return X_mod