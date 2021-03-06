import sys
import nltk
import re
nltk.download(['punkt', 'wordnet'])
import warnings
import pandas as pd
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.externals import joblib
from sklearn.metrics import classification_report, accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

def load_data(database_filepath):
    '''In this function we are loading the data from the database.'''
    engine = create_engine('sqlite:///'+ database_filepath)
    df = pd.read_sql_table('FigureEight', engine)
    X = df.message.values
    Y = df[df.columns[4:]].values
    category_names = list(df.columns[4:])
    return X, Y, category_names

def tokenize(text):
    ''' Tokenizing the text received.'''
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens


def build_model():
    '''creating pipelines to parse the TEXT, It will be passed through
    various pipelines to tokenize, transform and generate output'''
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(OneVsRestClassifier(LinearSVC(random_state = 0))))
    ])
    parameters = {
                'tfidf__smooth_idf':[True, False],
                'clf__estimator__estimator__C': [1, 2, 5]
             }
    cv = GridSearchCV(pipeline, param_grid=parameters, scoring='precision_samples', cv = 5)
    return cv

def evaluate_model(model, X_test, Y_test, category_names):
    ''' Model Evaluation function'''
    Y_pred = model.predict(X_test)
    print(classification_report(Y_test, Y_pred, target_names = category_names))
    for i in range(Y_test.shape[1]):
        print('%25s accuracy : %.2f' %(category_names[i], accuracy_score(Y_test[:,i], Y_pred[:,i])))

def save_model(model, model_filepath):
    '''To save the model.'''
    joblib.dump(model, model_filepath)


def main():
    '''To pass the Path to Database and Model. '''
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        model = build_model()
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('missing paths!!')


if __name__ == '__main__':
    main()
