/* function a(){
    console.log('A')
}
 */

//JS 에서는 함수가 값이다 
var a = function(){
    console.log('A')
}

function slowfunc(callback){
    callback()
    console.log('B')
}
function fastfunc(hi){
    hi()
    console.log('C')
}

slowfunc(a)
fastfunc(a)