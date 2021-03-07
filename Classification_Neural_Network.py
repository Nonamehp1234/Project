'''
    Solving problem Classification_Neural_Network about Pima Indians Diabetes.
    And we have a 768 observations with eight input and one output,
    One output have value is zero or one. (yes or no) check patient have sick??
    - Eight input is : 
        + Number of times pregnant. (type : int)
        + Plasma glucose concertration a 2 hours in an oral glucose tolerance test
        + Diastolic blood pressure (mm Hg)
        + Triceps skinfold thickness (mm)
        + 2-Hour serum insulin (mm U/ml)
        + Body mass index
        + Age (years)
    - Method to Problem Solving is : FeedForWard and Backpropagation.
        + FeedForWard use function sigmoid. (1/(1+e^-x))
        + Backpropagation : Chain Rule
    - There ara 2 layers is : one output layer + one hidden layer.
    - Optimize Weights and Bias. 
    - Learning rate : 0.1
    - Show Accuracy data train, data test to compare pylot.
    - Stop epechs to unoverfitting.  
    - f(x) = 1/(1+np.exp(-x)) = > f'(x) = f(x)*(1-f(x))
'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# Sigmoid function have value 0 - > 1.
def sigmoid_function(x):
    return 1/(1+np.exp(-x))
# Derivative sigmoid function (1/(1+np.exp(-x)))'
def derivative_sigmoid_function(x):
    return (1-1/(1+np.exp(-x)))*(1/(1+np.exp(-x)))
# Show figure and see draw line Accuracy of tranning and test.
def draw():
    pass
def create_Neural_Network():
    Units = 5
    layers = 2
    return Units , layers
# Create value Weights and Bias.
def Weights_Bias(units_hidden, layers, input_train):
    Weights = []
    Bias = []
    Weights.append(np.random.randn(len(input_train.T), units_hidden))
    Weights.append(np.random.randn(units_hidden, 1))
    _Weights = np.array(Weights)
    Bias.append(np.ones((len(input_train) ,units_hidden)))
    Bias.append(np.ones((1,1)))
    _Bias = np.array(Bias)
    return _Weights , _Bias
'''
    Processing data divide data_tranning to caculator Weights and Bias, data_test to test accuracy program.
'''
def Processing_data(file):
    # Convert to value at file csv to value numpy help caculator easy.
    tranning = file[0:int(0.7*len(file))].values
    test = file[int(0.7*len(file)):].values
    _input = tranning[:,:8]
    _output = tranning[:,8:]
    input_ = test[:,:8]
    output_ = test[:,8:]
    # Convert value to 0 -> 1 to imblance between data cols.
    for index in range(0,8):
        _input[:,index] = _input[:,index]/max(_input[:,index])
        input_[:,index] = input_[:,index]/max(input_[:,index])
    return _input , _output , input_ , output_
# Train to specific is : optimize Wights , Bias
def train(Weights , Bias , input_train , output_train , input_test , output_test):
    learning_rate = 0.01
    iteration = 1000
    for i in range(iteration):
        # Feedforward
        Z1 = np.dot(input_train , Weights[0])
        A1 = sigmoid_function(Z1)
        Z2 = np.dot(A1 , Weights[1])
        output_predict = sigmoid_function(Z2)
        # Backpropagation
        E2 = derivative_sigmoid_function(Z2)*(output_predict - output_train)
        dW2 = np.dot(E2.T, A1).T
        E1 = np.dot(Weights[1] , E2.T).T*derivative_sigmoid_function(Z1)
        dW1 = np.dot(E1.T, input_train).T
        # Learning rate
        Weights[1] -= learning_rate*dW2
        Weights[0] -= learning_rate*dW1
        count = accuracy(Weights[0] , Weights[1] , input_test , output_test)
        if i%100 == 0:
            print("train accuracy :" , count/len(output_test) )
def accuracy(W1 , W2 , input_test , output_test):
    Z1 = np.dot(input_test , W1)
    A1 = sigmoid_function(Z1)
    Z2 = np.dot(A1 , W2)
    output_predict = sigmoid_function(Z2)
    count = 0
    for index  in range(0 , len(output_predict)):
        if output_predict[index] >= 0.5:
            output_predict[index] = 1
        else:
            output_predict[index] = 0
        # Accuracy.
        if output_predict[index] == output_test[index]:
            count += 1
    return count
# Function main
if __name__ == "__main__":
    # Hidden layer = 1, Output layer = 1 and units hidden layer = 5
    csv_file = pd.read_csv("C:/Users/Administrator/Downloads/pima-indians-diabetes.csv")
    input_train , output_train , input_test, output_test = Processing_data(csv_file)
    # Explain variable UH_layers is units of hidden layers, layers = 2 because one hidden + output layer
    UH_layers , layers = create_Neural_Network()
    Weights , Bias = Weights_Bias(UH_layers , layers, input_train)
    train(Weights,Bias,input_train,output_train,input_test,output_test)