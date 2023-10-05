for(let i= 1; i<=9; i++){
    for(let j = 0; j<=9; j++){
        for(let k = 0; k<= 9; k++){

            if(i**3+j**3+k**3 == `${i}${j}${k}`){
                console.log(`${i}${j}${k}`)
            }
        }
    }
}