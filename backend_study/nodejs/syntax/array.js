//CRUD 
var arr = ['A','B','C','D'];
//console.log(arr.length)
arr.push('E')
//console.log(arr)

var number = [1,400,12,34,5];
var i = 0;
var total = 0;
while (i<5){
    console.log(number[i])
    total = total + number[i]
    i = i+1
}
console.log(`total: ${total}`)