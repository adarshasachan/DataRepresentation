from flask import Flask, jsonify, request, abort
#from studentDAO import studentDAO
from jobDAO import jobDAO
app = Flask(__name__, static_url_path='', static_folder='.')


@app.route('/jobs')
def getAll():
    results=jobDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/jobs"
@app.route('/jobs/<int:id>')
def findById(id):

    foundjob=jobDAO.findByID(id)

    return jsonify(foundjob)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"JobType\":\"hello\",\"Company\":\"someone\",\"Salary\":123}" http://127.0.0.1:5000/jobs
@app.route('/jobs', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    
    job = {
        
        "JobType": request.json['JobType'],
        "Company": request.json['Company'],
        "Salary": request.json['Salary'],
        "Location": request.json['Location'],
    }
    
    values=(job['JobType'],job['Company'],job['Salary'],job['Location'])
    newId= jobDAO.create(values)
    job['id']=newId
    return jsonify(job)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"JobType\":\"hello\",\"Company\":\"someone\",\"Salary\":123}" http://127.0.0.1:5000/jobs/1
@app.route('/jobs/<int:id>', methods=['PUT'])
def update(id):
    
    foundjob = jobDAO.findByID(id)
    if not foundjob:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Salary' in reqJson and type(reqJson['Salary']) is not int:
        abort(400)

    if 'JobType' in reqJson:
        foundjob['JobType'] = reqJson['JobType']
    if 'Company' in reqJson:
        foundjob['Company'] = reqJson['Company']
    if 'Salary' in reqJson:
        foundjob['Salary'] = reqJson['Salary']

    if 'Location' in reqJson:
        foundjob['Location'] = reqJson['Location']
    
    values=(foundjob['JobType'],foundjob['Company'],foundjob['Salary'],foundjob['Location'],foundjob['id'])
    jobDAO.update(values)
    return jsonify(foundjob)
        

    

@app.route('/jobs/<int:id>' , methods=['DELETE'])
def delete(id):

    jobDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)