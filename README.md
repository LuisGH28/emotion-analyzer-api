## Emotion Analyzer API

A **FastAPI-based backend** that detects human emotions from images using **DeepFace** and  **OpenCV** .

It returns the dominant emotion (e.g., happy, sad, angry, surprised, etc.) and is designed for integration with **mobile apps (Flutter)** or  **AI-driven projects** .

---

### Features

* Emotion detection via [DeepFace](https://github.com/serengil/deepface)
* Built with **FastAPI** for speed and easy REST integration
* Ready to connect with your **Flutter frontend**
* Modular structure for scaling and containerization (Docker ready)
* Uses RetinaFace or OpenCV as detection backend

---

### Project Structure

```
.
├── app
│   ├── __pycache__
│   │   ├── config.cpython-310.pyc
│   │   ├── main.cpython-310.pyc
│   │   └── routes.cpython-310.pyc
│   ├── config.py
│   ├── main.py
│   ├── routes.py
│   └── services
│       ├── __pycache__
│       │   └── emotion_service.cpython-310.pyc
│       └── emotion_service.py
├── Dockerfile
├── README.md
└── requirement.txt
```

---

### Setup

1.- Clone the repository

```
git clone  https://github.com/LuisGH28/emotion-analyzer-api.git
cd emotion-analyzer-api
```

2.- Create and activate a virtual environment

```
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# or
.venv\Scripts\activate      # Windows
```

3.- install dependencies

```
pip install -r requirements.txt
```

4.- Run the API

```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

### Testing the API

```
curl -X POST "http://127.0.0.1:8000/analyze_emotion" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/Users/usuario/Downloads/tests.jpeg;type=image/jpeg"
```

---

### Example Response

```
{
    "ok": true,
    "emotion_en": "happy",
    "emotion_es": "feliz",
    "score": 98.6928482055664
}
```

---

### Docker Support

```
docker build -t emotion-analyzer-api .
docker run -p 8000:8000 emotion-analyzer-api
```

---

### Tech Stack

| Layer         | Technology                |
| ------------- | ------------------------- |
| API Framework | FastAPI                   |
| AI/ML Backend | DeepFace, OpenCV          |
| Model         | RetinaFace, VGG-Face, FER |
| Language      | Python 3.10+              |
| Deployment    | Docker / Uvicorn          |
| Client        | Flutter (mobile)          |

---

### Enviroment Variables

```
ALLOWED_ORIGINS=["*"]
DETECTOR_BACKEND=retinaface
```

---

### Author

**Luis Ángel González Hernández**

Backend Developer & AI Enthusiast

 [github.com/LuisGH28](https://github.com/LuisGH28)

 [luigidev28.netlify.app]()
