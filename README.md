# Intelligent-character-recognition

<h3>How to run it</h3>
Install virtual environment on your pc, then run 
`pip install -r requirements.txt`
If you want to see how it works:
`python manage.py runserver`

If you need to prepopulate data, use this command:
`python manage.py populate`


<h5>Useful resources</h5>

[Image alignment and registration with OpenCV](https://www.pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/)

[OCR a document, form, or invoice with Tesseract, OpenCV, and Python](https://www.pyimagesearch.com/2020/09/07/ocr-a-document-form-or-invoice-with-tesseract-opencv-and-python/)

[OCR: Handwriting recognition with OpenCV, Keras, and TensorFlow](https://www.pyimagesearch.com/2020/08/24/ocr-handwriting-recognition-with-opencv-keras-and-tensorflow/)



For local run set next env
```
ICR_LOCAL_RUN="True"
ICR_DEBUG="True"
```

To use Google ICR you need to provide an absolute path to your credentials file. Set it to the next variable
```
GOOGLE_APPLICATION_CREDENTIALS=your_path_to_file.json
```

Sometimes you may need to see what images are sent to Google ICR. Set next env to do it
```
GOOGLE_ICR_SEE_IMAGE="True"
```
