function divisibleBy11(number){

    let par = 0;
    let impar = 0;

    if(number.length >= 2){

        let numbers = number.split('');
        for(let i = 0; i < number.length; i++){
            let bin = numbers[i].toString(2);
            if(bin[bin.length - 1] != 0){
                impar = impar + numbers[i];
            }else{
                par = par + numbers[i];
            }
        }

        number = par - impar;

        if(number === 0){
            return true;
        }
    }

    
    if(number - Math.floor(number / 11) * 11 === 0){
        return true
    }

    return false;
}

divisibleBy11(5863); // return true.