from flask import Flask,render_template,request,redirect 
import os
app = Flask(__name__,template_folder='template')
app.config["IMAGE_UPLOADS"] = r"C:\Users\arsha"
@app.route('/')
def index():
    return render_template('OCRindex.html')
@app.route('/convert',methods = ['POST','GET'])
def convert():
    if request.method=='POST':
        if request.files:
            image = request.files['image']
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))       
            import pytesseract 
            from PIL import Image
            a= image.filename
            img = Image.open(a)
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            t = pytesseract.image_to_string(img)
            return t            
if __name__=='__main__':
    app.run()