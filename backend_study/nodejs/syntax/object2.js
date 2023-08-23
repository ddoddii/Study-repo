// array, object
var f = function(){
    console.log(1+1)
    console.log(1+2)
}
console.log(f)
var a = [f] //배열의 원소로 함수가 존재할 수 있다
a[0]()

var o = {
    func:f //object 안에 함수가 존재할 수 있다
}
o.func() 