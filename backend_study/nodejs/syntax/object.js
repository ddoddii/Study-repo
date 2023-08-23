//Array(순서O) -> 배열 
var members = ['soeun','uhm','ddoddii']

var i = 0
while(i<members.length){
    console.log(members[i])
    i = i + 1
}
//Object(순서x) -> 마치 dictionary (key:value)
var roles = {'soeun':'name','ddoddii':'githubid'}
for (var n in roles){
    console.log('object =>',n,'value=>',roles[n]);
    
}
console.log(roles['soeun'])