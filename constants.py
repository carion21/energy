
MODE = "dev"
#MODE = "pro"

MODEL_PATH = './models/'

MODEL_PATH_DEV = MODEL_PATH + 'model_dev.joblib'
MODEL_PATH_PRO = MODEL_PATH + 'model_pro.joblib'

MODEL_PATHS = {
    "dev": MODEL_PATH_DEV,
    "pro": MODEL_PATH_PRO
}
