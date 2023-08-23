var fs = require('fs');

//readFileSync
console.log('A')
fs.readFile('sample.txt','utf8', function(err,result){
    console.log(result)
})
console.log('c')
// 비동기 