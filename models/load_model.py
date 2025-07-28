import os
import joblib

def load_latest_model(model_dir='models/'):
    model_files = [f for f in os.listdir(model_dir) if f.endswith('.pkl')]
    
    if not model_files:
        raise FileNotFoundError("No model files found in the models directory.")
    
    # Get full paths and find the most recently modified file
    model_paths = [os.path.join(model_dir, f) for f in model_files]
    latest_model_path = max(model_paths, key=os.path.getmtime)

    print(f"Loading latest model from: {latest_model_path}")
    return joblib.load(latest_model_path)

def save_model(model_result, model_path='models/garch_model.pkl'):
    joblib.dump(model_result, model_path)
