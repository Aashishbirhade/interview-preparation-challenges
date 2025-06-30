
//step1 npm i qrcode
const QRcode = require('qrcode')

const url = 'https://github.com/Aashishbirhade'
// QRcode.toFile('qr.png',url,(err)=>{
//     if(err){
//         console.log('error',err)
//     }
//     else{
//         console.log("qr code saved")
//     }
// })
QRcode.toFile('qr.png',url)