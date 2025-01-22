from src.models.model import ModelFactory

model = ModelFactory.create_model('random_forest_regressor')
print(model)