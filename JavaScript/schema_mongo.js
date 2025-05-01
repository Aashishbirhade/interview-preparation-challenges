const mongo = require('mongoes')
mongo.connect('mongodb://localhost:27017/test')
const user = mongo.Userschema({
    name: String,
    age: Number,
    email: String,
    password: String
}) 
module.exports = mongo.model('user', user)