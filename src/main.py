from typing import Annotated

from fastapi import FastAPI, Form

from topic_modeler import inference

app = FastAPI()


@app.post("/predict/tp_modeler")
async def topic_modeling(text: Annotated[str, Form()]):
    res = inference(text)
    return {
        "text": text,
        "predictions": res
    }
