import os
from PIL import Image
from flask import render_template, url_for, request, flash, redirect
from photoannotation import app
from photoannotation.forms import UploadForm, AlbumForm, SearchForm, LoginForm, RegistrationForm
from photoannotation.face_recogniser import FaceRecogniser
from photoannotation.HistoCluster import HistoCluster
import time
from photoannotation.ImageMetaData import ImageMetaData
import photoannotation.GPSDATA as GPSDATA
from werkzeug.utils import secure_filename
#from pathlib import Path
import shutil

#UPLOAD_FOLDER = r'E:/Study/12th sem/PhotoAnnotation/photoannotation/static/images/'
UPLOAD_FOLDER = os.path.join(app.root_path, "static/images/")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    print(os.path.join(app.root_path, "static/images/"))
    form = LoginForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('login.html', form=form)
        else:
            return redirect(url_for('search'), code=302)
        pass
    else:
        return render_template('login.html', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('registration.html', form=form)
        else:
            return redirect(url_for('search'), code=302)
        pass
    return render_template('registration.html', form=form)


@app.route('/album')
def album():
    dir_list = []
    form = AlbumForm()
    hist = HistoCluster(UPLOAD_FOLDER)
    cluster_data = hist.cluster_photos()
    # for index in cluster_data:
    #     print(index, cluster_data[index])
    #     for image in cluster_data[index]:
    #         print(image)
    # for root, directories, files in os.walk(UPLOAD_FOLDER):
    #     for dirs in directories:
    #         for file_list in os.listdir(os.path.join(root, dirs)):
    #             dir_list.append([dirs, file_list, len(dirs),])
    #             break
    #     break
    return render_template('user/album.html', form=form, dir_list=cluster_data)


@app.route('/album/<string:name>')
def show_album(name):
    image_list = []
    # for file in os.listdir(os.path.join(UPLOAD_FOLDER, name)):
    #     image_list.append(file)
    return render_template('user/show-album.html', form=form, album=name, image_list=image_list)


@app.route('/search')
def search():
    form = SearchForm()
    return render_template('user/search.html', form=form)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if request.method == 'POST':
        images = request.files.getlist("photo")
        for image in images:
            filename, ext = image.filename.split(".")
            if ext not in ['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG']:
                flash('Only images are allowed to upload')
                return render_template('user/upload.html', form=form)
            f = app.config['UPLOAD_FOLDER'] + filename + "_" + str(time.time()) + "." + ext
            image.save(f)
            print("Reached")
            # validImages = []
            # imgMeta = ImageMetaData(image)
            # imgExif = None
            # imgGPS = None
            # imgElevation = None
            # if imgMeta is not None:
            #     imgExif = imgMeta.get_exif_data()
            #     if imgExif is not None:
            #         '''Exif exists'''
            #         imgGPS = imgMeta.get_gps()
            #         '''imgGPS[0] = latitude
            #            imgGPS[1] = longitude'''
            #         if imgGPS[0] != 0:
            #             '''call GPSDATA functions for gps related data'''
            #             imgElevation = GPSDATA.get_elevation(imgGPS[0], imgGPS[1])
            #             #imgWeather = GPSDATA.get_weather_info(imgGPS[0], imgGPS[1], imgExif['DateTime'])
            #         else:
            #             '''no gps'''
            #             pass
            #
            #     else:
            #         '''Exif doesn't exist'''
            #         isExif = False
            # validImages.append({'ImgLocation': image, 'ExifData': imgExif, 'GpsData': imgGPS,
            #                     'ImgElevation': imgElevation})
            # print(validImages)

    return render_template('user/upload.html', form=form)


@app.route('/read-exif')
def read_exif():
    form = UploadForm()
    data = form.photoName.data
    return data


@app.route('/generate-caption', methods=['GET', 'POST'])
def generate_caption():
    if request.method == 'POST':
        try:
            img = Image.open(request.files['photo'])
            face = FaceRecogniser()
            response = face.face_recognise(img)
            return response
        except:
            return "Image file required"
    pass


@app.route('/change-caption', methods=['GET', 'POST'])
def changeCaption():
    if request.method == "POST":
        print(request)
    return "asdf"


