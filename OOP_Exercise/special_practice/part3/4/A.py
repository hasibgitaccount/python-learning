# 4. SOLID Principles (ML Relevance):

# A. Apply SOLID principles to your codebase. For example, in a Model class for ML, ensure it follows the Single Responsibility Principle by keeping model training separate from evaluation.

class Model:

    def __init__(self):
        self.layers = 'neural network layers'
    
    def predict(self, data):
        print('making predictions on the data')
        return [0]* len(data)

class ModelTrainer:
    def __init__(self, model):
        self.model = model

    def train(self, data, labels):
        print('training model')
        print('data trained successfully')

class ModelEvaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, data, labels):
        predictions = self.model.predict(data)
        accuracy = self.calculate_accuracy(predictions, labels)
        print(f'model accuracy: {accuracy}%')

    def calculate_accuracy(self, predictions, labels):
        correct_predictions = sum(p == 1 for p,1 in zip(predictions, labels))
        return (correct_predictions / len(labels)) * 100
    


model = Model()
trainer = ModelTrainer(model)
evaluator = ModelEvaluator(model)

# Training phase
trainer.train([1, 2, 3], [0, 1, 1])

# Evaluation phase
evaluator.evaluate([1, 2, 3], [0, 1, 1])