function bmi(cm,kg){
    let check = kg / (cm/100)**2
    if (check>=26){
        return '비만'
    }
    else if(check>=24){
        return '과체중'
    }
    else if(check>=18.5){
        return '정상'
    }
    else{
        return '저체중'
    }
}

console.log(bmi(150,45))