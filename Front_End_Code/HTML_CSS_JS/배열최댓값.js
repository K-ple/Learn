const arr = [10,120,30,50,20];
answer = 0
for(let i = 0; i< arr.length; i++){
    if(answer < arr[i]){
        answer = arr[i]
    }
}
console.log(answer);

console.log(Math.max(...arr))