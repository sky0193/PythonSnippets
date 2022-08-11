#https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

#!flask/bin/python
from flask import Flask, request, jsonify
from multiprocessing import Value
#from transcribe_file import transcribe
import time

counter = Value('i', 0)


app = Flask(__name__)

#curl -X GET  http://localhost:5000/transcription
@app.route('/transcription', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': "test"})


#curl -X PUT --form-string 'body={ "locale": "de" }' -F 'audio=@/home/call.wav' http://localhost:5000/transcription/order

@app.route('/transcription/order', methods=['PUT'])
def update_task():
    body = request.form['body']
    audio = request.files["audio"]

    new_file_path = "test.wav" 
    audio.save(new_file_path)
    
    with counter.get_lock():
        counter.value += 1
        request_id = counter.value

    st = time.time()
    #transcribe(new_file_path)
    et = time.time() 
    elapsed_time = et - st
    print(f"audio: {audio}\n")
    print(f"id: {request_id}\n 'Execution time:', {elapsed_time}, 'seconds'\n")
    return f"id: {request_id}\n 'Execution time:', {elapsed_time}, 'seconds'\n"

if __name__ == '__main__':
    app.run(debug=True)