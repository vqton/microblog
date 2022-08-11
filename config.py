import os


class Config(object):
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "bb%:yICj|OB//etji2y.s-Em;:7cP@#G~*JaFc<L-!e6qX8o0rQn{QlyR]:r8-4"
    )
