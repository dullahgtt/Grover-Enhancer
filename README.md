# Grover-Enhancer

**Team:** 
- Abdullah Kamal
- Zaid Jamal
- Brian Robinson
- Gabriel Rosales
- Zachary Sotny

Our project focuses on optimizing the training model of the already developed NLP network, Grover, to increase its accuracy in recognizing examples of fake news in the hopes of preventing the widespread transmission of fallacious news content.

To approach this, we propose manipulating the coefficients of the connecting edges of the hidden layers to better calibrate the network for any commonalities between human written facts to machine written fake news. With our limited resources, we are hoping to test our model on generated articles from other AI models like ChatGPT and Rytr. 

In our initial tests, Grover experienced issues in recognizing clearly falsified articles generated by superior AI models. Our approach aims to minimize the reccurence of this phenomenon. 


*Below is a proposed Convolutional Neural Network that could be used to subtitute the AdaFactor Optimization algorithm used by Grover:*

```C
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the dataset
data = pd.read_csv('news_dataset.csv')
X = data['text'].values
y = data['label'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert the text data into numerical data using Tokenization and Padding
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)
vocab_size = len(tokenizer.word_index) + 1
maxlen = 200
X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

# Define the CNN model
model = Sequential()
model.add(Embedding(vocab_size, 128, input_length=maxlen))
model.add(Conv1D(32, 5, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), batch_size=32)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Test Accuracy: {accuracy:.3f}')
```

# Proposed Changes:

The activation function sigmoid is a logistic function and only good for a yes/no scenarios for a positive or negative detection of a specific element, hence if there is any indecisiveness in any output from Grover (in other words, Grover isn't sure if an article is real or fake), we would come up with a rather inaccurate answer. Looking at other activation functions like *SoftMax* would be a good way of testing which functions provide for a more accurate model and a smaller error rate.

*SoftMax:*

Sources: https://www.andreaperlato.com/aipost/cnn-and-softmax/

$y_i = \frac{e^{x_i}}{\sum\limits_{j=1}^ne^{x_j}}$

```
import numpy as np

def softmax(x):
    """Compute softmax values for each row of x."""
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)
```

# Training the Model:

To properly train the model for better outcomes, we would need to generate an inclusive database that would cover a wide range of possibilities regarding real and fake news. This would include fake articles generated by AI models similar to GPT4. We would also include many articles from noteworthy news sites to differentiate. Producing a dataset that would produce accurate readings could be challenging, as the size would be quite expansive. 
