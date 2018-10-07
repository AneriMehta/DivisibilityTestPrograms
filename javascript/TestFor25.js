function divisibleBy25(number){

    if(number === 1 || number === 5 || number === 25) { return true; }

    let res = number;

    if(number.length >= 3){
        let unid = number[number.length - 1];
        let dec = number[number.length - 2] * 10;
        res = unid + dec;
    }

    if(res - Math.floor(res / 25) * 25 === 0){ return true; }

    return false;
}

divisibleBy25(7650419);