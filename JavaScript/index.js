const express = require("express")
const app = express()
const UserModel = require('./schema_mongo')

app.get("/",(req,res)=>{
    res.send("Hello Buddy")
})

app.post("/create",async(req,res)=>{
 const user = await UserModel.Create({
    name:"veer",
    age: 22,
    email:"veer@gmail.com"
 })
 res.send(user)
})
app.get("/read",async(req,res)=>{
    const user = await UserModel.find()
    res.send(user)
})

app.listen(3000)