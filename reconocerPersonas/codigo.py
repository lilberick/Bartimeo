import face_recognition
import picamera
import numpy as np
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)
# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")
obama_image = face_recognition.load_image_file("modelos/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
biden_image = face_recognition.load_image_file("modelos/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
stallman_image= face_recognition.load_image_file("modelos/richard.jpg")
stallman_face_encoding = face_recognition.face_encodings(stallman_image)[0]
chupetin_image= face_recognition.load_image_file("modelos/chupetin.jpg")
chupetin_face_encoding = face_recognition.face_encodings(chupetin_image)[0]
known_face_encodings = [obama_face_encoding,biden_face_encoding,stallman_face_encoding,chupetin_face_encoding]
# Initialize some variables
face_locations = []
face_encodings = []
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Richard Stallman",
    "Chupetin Trujillo"
]
while True:
    print("Capturando imagen.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Encontradas {} caras en la imagen.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
    # Loop over each face found in the frame to see if it's someone we know.
    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        #match = face_recognition.compare_faces([obama_face_encoding], face_encoding)
        match = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Persona Desconocida"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if match[best_match_index]:
            name = known_face_names[best_match_index]
            print("PERSONA DETECTADA: ",name)
        #face_names.append(name)
