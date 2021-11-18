const express = require("express")
const router = express.Router();
const fs = require('fs');
const dataPath = './DB/todolist.json'

const saveAccountData = (data) => {
    const stringifyData = JSON.stringify(data)
    fs.writeFileSync(dataPath, stringifyData)
}
const getAccountData = () => {
    const jsonData = fs.readFileSync(dataPath)
    return JSON.parse(jsonData)    
}
  router.post('/', (req, res) => {
   
    var existAccounts = getAccountData()
    const newAccountId = Math.floor(100000 + Math.random() * 900000)
    existAccounts[newAccountId] = req.body
    console.log(existAccounts);
    saveAccountData(existAccounts);
    res.send({success: true, msg: 'Данные были добавлены'})
})

router.get('/', (req, res) => {
  const accounts = getAccountData()
  res.send(accounts)
})

router.put('/:id', (req, res) => {
   var existAccounts = getAccountData()
   fs.readFile(dataPath, 'utf8', (err, data) => {
    const accountId = req.params['id'];
    existAccounts[accountId] = req.body;
    saveAccountData(existAccounts);
    res.send(`Заметка с ${accountId} ID была изменен`)
  }, true);
});

router.delete('/:id', (req, res) => {
   fs.readFile(dataPath, 'utf8', (err, data) => {
    var existAccounts = getAccountData()
    const userId = req.params['id'];
    delete existAccounts[userId];  
    saveAccountData(existAccounts);
    res.send(`Заметка с ${userId} ID была удалена`)
  }, true);
})
module.exports = router