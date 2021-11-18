const express = require("express")
const bodyParser = require("body-parser")
const fs = require('fs');
const app = express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }));
const routes = require('./router/todolist')
app.use('/todo', routes)
app.listen(5000, ()=>{
    console.log("listeniing at port:5000")
}) 